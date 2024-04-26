# PGA-QM

[WORK IN PROGRESS]

## Description
This repository aims to provide all the necessary resources and instructions to reproduce the results presented in [LINK TO PAPER TO ADD]. It contains the following files and folders:

- PGA-QM.py provides an implementation of how to use the parallel genetic algorithm (PGA) to map a quantum circuit to some hardware. Running it writes a "bench_..._.txt" file that can be used to study the performance of the algorithms.
- PGA-QM_Speedup.py provides the same code, but running it returns a "speedup_..._.txt" file that can be used to study the scalability of the algorithm.
- Benchmarks is a folder containing all the circuits studied in the paper. They were taken from https://www.cda.cit.tum.de/mqtbench/.

## Installation Instructions
The Python codes provided in this repository rely on several Python libraries, namely pygad and qiskit.
They can be installed using pip: `pip install pygad` and `pip install qiskit==0.43.3`.
Note that all codes have been implemented and tested using qiskit 0.43.3 only. There is no guarantee that older or newer versions would be compatible with this code. However, pygad's latest version should work fine.

## How to Use
- PGA-QM.py can be executed using `python3 PGA-QM.py -c CIRCUIT SIZE --pga PGA -s STOP`. The arguments are as follows:
  - CIRCUIT is the type of circuit to be used (e.g., ghzall, ghz, dj, qft).
  - SIZE is a strictly positive integer, the number of qubits of the circuit.
  - PGA is either 1, 2, or 3 and selects which PGA parameters are wanted (see [LINK TO PAPER TO ADD]).
  - STOP is an integer indicating the stopping criterion of the PGA. Values <= 0 will result in stopping the PGA after a number of generations (30 or 35 here). Values > 0 mean that the PGA may stop earlier if the best solution didn't improve for n consecutive generations.
  
Note that not every circuit is available for every size. Unless one downloads more benchmarks from https://www.cda.cit.tum.de/mqtbench/, the only sizes available are 80 and 120 qubits for both dj and ghz circuits, and 40 qubits for the qft circuit. The ghzall circuit, another way to write the ghz circuit, is the only one available for all sizes, which can be beneficial for small tests to ensure that everything works properly.

Example: `python3 PGA-QM.py -c ghzall 80 --pga 1 -s 0`

- PGA-QM_Speedup.py can be executed using `python3 PGA-QM.py -c CIRCUIT SIZE --pga PGA -s STOP -t THREADS`. The arguments are the same as before, with the added THREADS being the number of parallel threads to use. By changing this value, one can study the scalability of the parallel genetic algorithm.

Example: `python3 PGA-QM_Speedup.py -c ghzall 80 --pga 1 -s 0 -t 32`
