# -*- coding: utf-8 -*-
"""
@author: Jérôme Rouzé, jerome.rouze@umons.ac.be
"""

import numpy as np
import pygad as gad
import time
from qiskit import QuantumCircuit,transpile,ClassicalRegister
from qiskit.transpiler import Layout
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
import argparse
parser = argparse.ArgumentParser(description="My Python Script")

##-------------------------------------------------------
##      Fitness definition
##-------------------------------------------------------
def fitness_GA(ga_instance,layout, layout_idx):
    return fitness(layout)

def fitness(layout):
    init_layout={qr[i]:layout[i] for i in range(len(layout))}
    init_layout=Layout(init_layout)

    pm = generate_preset_pass_manager(3,backend,initial_layout=init_layout)
    pm.layout.remove(1)
    pm.layout.remove(1)

    QC=pm.run(qc)
    return -QC.depth()

##-------------------------------------------------------
##      Circuit selector
##-------------------------------------------------------
def circuit_selector(name,nb_qubit):
    if name=="ghzall":
        qc=QuantumCircuit(nb_qubit)
        qc.h(0)
        for i in range(1,nb_qubit):
            qc.cx(0,i)
        qc.measure_all()
          
        qr=qc.qregs[0]

        name="ghzall"
    else:
        filename=f"{name}_indep_qiskit_{nb_qubit}"
        qasmfile=f"./Benchmarks/{filename}.qasm"
        qc=QuantumCircuit().from_qasm_file(qasmfile)
        qr=qc.qregs[0]
    return qc,qr

parser.add_argument("-c", "--circuit", nargs=2, default=["ghzall", "80"], help="Name and number of qubits of the circuit")

##-------------------------------------------------------
##      Reading GA parameters
##------------------------------------------------------- 
parser.add_argument("--pga", type=int, default=1, help="PGA set of parameters", choices=[1,2,3])
parser.add_argument("-s","--stop_crit", type=int, default=0, help="Specifies the stopping criteria. n<=0 means None, n>0 means saturate_n")
parser.add_argument("-t","--nb_threads", type=int, default=30, help="Number of parallel threads")


args = parser.parse_args()
num_pga = args.pga
nb_threads = args.nb_threads

def pga_param_selec(num_pga):
    if num_pga==3:
        num_gen = 35
        num_mating = 15
        pop = 20
    elif num_pga==2:
        num_gen = 30
        num_mating = 20
        pop = 30
    else:   ### Includes num_pga==1 or any other values (mistake)
        num_gen = 30
        num_mating = 20
        pop = 40
    return num_gen,num_mating,pop

num_gen,num_mating,pop = pga_param_selec(num_pga)
parent_selec = "random"
cross_type = "two_points"
cross_prob = 0.5
muta_type = "random"
muta_prob = 0.1

if args.stop_crit<=0:
    stop_criteria=None
else:
    stop_criteria=f"saturate_{args.stop_crit}"

##-------------------------------------------------------
##      Circuit & Backend selection
##-------------------------------------------------------
### Backend
# from qiskit_ibm_runtime.fake_provider import FakeLimaV2,FakeSingaporeV2,FakeWashingtonV2
from qiskit.providers.fake_provider import FakeLimaV2,FakeSingaporeV2,FakeWashingtonV2

backend = FakeWashingtonV2()
# backend = FakeSingaporeV2()

### Circuit
name = args.circuit[0]
nb_qubit = int(args.circuit[1])

qc,qr=circuit_selector(name, nb_qubit)

##-------------------------------------------------------
##      Create a GA instance
##-------------------------------------------------------    
ga_instance = gad.GA(num_generations = num_gen,
                        num_parents_mating = num_mating,
                        stop_criteria=stop_criteria,
                        fitness_func = fitness_GA,
                        sol_per_pop = pop,
                        num_genes = nb_qubit,
                        gene_type = int,
                        gene_space = range(0,backend.num_qubits),
                        parent_selection_type = parent_selec,
                        crossover_type = cross_type,
                        crossover_probability = cross_prob,
                        mutation_type = muta_type,
                        mutation_probability = muta_prob,
                        mutation_by_replacement = True,
                        allow_duplicate_genes = False,
                        parallel_processing = ['process',nb_threads])

##-------------------------------------------------------
##      Time measurement
##------------------------------------------------------- 
### Measuring GA time
start = time.time()
ga_instance.run()
end = time.time()

### Extracting information and transpile the chosen solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
# QC_ga=transpile(qc,backend,initial_layout=list(solution),optimization_level=3)
# ga_instance.plot_fitness()

##-------------------------------------------------------
##      Writing some result
##------------------------------------------------------- 
stop_crit_name=""
if stop_criteria:
    stop_crit_name=stop_criteria
with open(f"speedup_{name}_{nb_qubit}_{pop}_{num_mating}_{stop_crit_name}.txt","a") as fout:
    fout.write(f"{name}_{nb_qubit} {-solution_fitness} {end - start} {nb_threads}\n")