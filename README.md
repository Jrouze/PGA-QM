# PGA-QM

In this repository, the Makefile is used to simplify the execution of PGA-GM.py.

Using the command "make PGAi CIRCUIT=circuit SIZE=size", with i in {1, 2, 3}, circuit in {ghzall, dj, ghz} and size in {80, 120}, one can reproduce the experiment of [LINK TO PAPER TO ADD].

Note that in order to function properly, a folder called "Benchmarks" should be placed in the same folder as PGA-QM.py, otherwise the path in line 48 of PGA-QM.py will need to be modified accordingly. The "Benchmarks" folder contains of the necessary files (taken from https://www.cda.cit.tum.de/mqtbench/) to reproduce the experiments.

Important note : All codes have been implemented and tested using Qiskit 0.43.3. There is no guarentee that newer version would be compatible with this code.
