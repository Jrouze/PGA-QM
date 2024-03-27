# PGA-QM

[WORK IN PROGRESS]

## Description
This repository aims at providing all the necessary ressources and instructions to reproduce the results presented in [LINK TO PAPER TO ADD]. It constains the following files and folders :

- PGA-QM.py provides an implement of how to use the parallel genetic algorithm (PGA) to map a quantum circuit to some hardware. Running it writes a "bench_..._.txt" file that can be used to study the performance of the algorithms
- PGA-QM_Speedup.py provides the same code, but running it returns a "speedup_..._.txt" file that can be used to study the scalabity of the algorithm
- Benchmarks is a folder containing all the circuits studied in the paper. They were taken from https://www.cda.cit.tum.de/mqtbench/.

## Installation instruction
The python codes provided in this repository rely on several python libraries, namely pygad and qiskit.
They can be installed using pip : `pip install pygad` and `pip install qiskit==0.43.3`.
Note that all codes have been implemented and tested using qiskit 0.43.3 only.  There is no guarentee that older or newer version would be compatible with this code. However, pygad's lastest version should work fine.

## How to use
PGA-QM.py can be executed using `python3 PGA-QM.py -c CIRCUIT SIZE --pga PGA -s STOP` where CIRCUIT is the type of circuit to be used (ex : ghzall, ghz, dj, qft) and SIZE is the number of qubits of the circuit. Note
