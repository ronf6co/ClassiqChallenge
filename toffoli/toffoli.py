# BACKGROUND
# Many quantum operations include multi-controlled Toffoli (MCX) gates.
# Among the most notable are: Grover Operator, logical AND operator, various state preparation algorithms,
# and arithmetic comparators.
#
# This task focuses on the implementation of the MCX gate with a limited qubit count and circuit depth.
#
# THE PROBLEM
# Decompose an MCX gate with 14 control qubits into single-qubit and double-qubit CX gates.
# You may use up to 5 clean auxiliary qubits and should release (uncompute) them at the end of the circuit.
# Thus, the circuit can use no more than 20 total qubits:
#   14 control qubits,
#   one target qubit,
#   and up to five auxiliary qubits.
#
# Important: Make sure that when you submit a circuit, the order of the qubits is indeed as follows:
#   first the 14 control qubits,
#   then the target qubit,
#   then any auxiliary.
# This will help us validate the circuit.
#
# METRIC
# The winning solution will achieve this using a circuit of minimal depth.

import qiskit

qiskit.circuit.QuantumCircuit.mcx
