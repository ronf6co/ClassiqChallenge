# ----------------------------------------------------------------------------------------------------------------------
# Created By  : Ron Cohen
# Created Date: 14/05/2022
# ----------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------

from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

print("____________________________________________________________")
print("|            The CLASSIQ Coding Competition                |")
print("|                   The Challenge :                        |")
print("|      DECOMPOSING A MULTI-CONTROLLED TOFFOLI GATE         |")
print("|           Submitted by : Ron Cohen                       |")
print("____________________________________________________________ \n")


def c2x(circuit, q_c0, q_c1, q_t):
    """CCX circuit - the most known efficient way for CCX

    Parameters:
    q_c0, q_c1 : First 2 control qubits
    q_t        : Target qubit

   """
    circuit.h(q_t)
    circuit.cx(q_c1, q_t)
    circuit.tdg(q_t)
    circuit.cx(q_c0, q_t)
    circuit.t(q_t)
    circuit.cx(q_c1, q_t)
    circuit.tdg(q_t)
    circuit.cx(q_c0, q_t)
    circuit.t(q_t)
    circuit.h(q_t)
    circuit.t(q_c1)
    circuit.cx(q_c0, q_c1)
    circuit.t(q_c0)
    circuit.tdg(q_c1)
    circuit.cx(q_c0, q_c1)


def c3x(circuit, q_c0, q_c1, q_c2, q_t):
    """CCCX circuit - using gray code

    Parameters:
    q_c0, q_c1, q_c2 : First 2 control qubits
    q_t              : Target qubit

   """
    theta = np.pi/8
    circuit.p(theta, q_c0)
    circuit.p(theta, q_c1)
    circuit.cx(q_c0, q_c1)
    circuit.p(-theta, q_c1)
    circuit.cx(q_c0, q_c1)
    circuit.p(theta, q_c2)
    circuit.cx(q_c1, q_c2)
    circuit.p(-theta, q_c2)
    circuit.cx(q_c0, q_c2)
    circuit.p(theta, q_c2)
    circuit.cx(q_c1, q_c2)
    circuit.p(-theta, q_c2)
    circuit.cx(q_c0, q_c2)
    circuit.h(q_t)
    circuit.p(theta, q_t)
    circuit.cx(q_c2, q_t)
    circuit.p(-theta, q_t)
    circuit.cx(q_c1, q_t)
    circuit.p(theta, q_t)
    circuit.cx(q_c2, q_t)
    circuit.p(-theta, q_t)
    circuit.cx(q_c0, q_t)
    circuit.p(theta, q_t)
    circuit.cx(q_c2, q_t)
    circuit.p(-theta, q_t)
    circuit.cx(q_c1, q_t)
    circuit.p(theta, q_t)
    circuit.cx(q_c2, q_t)
    circuit.p(-theta, q_t)
    circuit.cx(q_c0, q_t)
    circuit.h(q_t)


def c14x_solution(circuit, q_con, q_target, q_ancilla):
    """C14X circuit - solution of C14X using 5 ancilla
    explanation in prints

    Parameters:
    q_con       : 14 qubits control register
    q_target    : Target qubit
    q_ancilla   : 5 ancilla qubits
   """
    print("We want to maximize the usage of ancilla")
    print("First we use the first 3 ancilla with C3X gate "
          "\nwhich cost only 27 depth (gray code):")
    print("C3X c0,c1,c2 -> a0")
    print("C3X c3,c4,c5 -> a1")
    print("C3X c6,c7,c8 -> a2")
    c3x(c14x, q_con[0], q_con[1], q_con[2], q_ancilla[0])
    c3x(c14x, q_con[3], q_con[4], q_con[5], q_ancilla[1])
    c3x(c14x, q_con[6], q_con[7], q_con[8], q_ancilla[2])
    # c14x.barrier() - save 0
    print("\nThan again C3X which is only 27 depth from those "
          "(2 ancilla)+(left 4 controls) to the remaining ancilla")
    print("C3X a0,c9 ,c10 -> a3")
    print("C3X a1,c11,c12 -> a4")
    c3x(c14x, q_ancilla[0], q_con[9], q_con[10], q_ancilla[3])
    c3x(c14x, q_ancilla[1], q_con[11], q_con[12], q_ancilla[4])
    # c14x.barrier() - save 1
    print("\nThan C2X which is only 11 depth from those 2 ancilla to target")
    print("C2X a3,a4 -> t")
    c2x(c14x, q_ancilla[3], q_ancilla[4], q_target)

    print("\nNow only need to return ancilla with performing again in reverse order:")
    print("C3X a1,c11,c12 -> a4")
    print("C3X a0,c9 ,c10 -> a3")
    print("And (order here doesn't matter):")
    print("C3X c6,c7,c8 -> a2")
    print("C3X c3,c4,c5 -> a1")
    print("C3X c0,c1,c2 -> a0")
    # c14x.barrier() - save 9
    c3x(c14x, q_ancilla[1], q_con[11], q_con[12], q_ancilla[4])
    c3x(c14x, q_ancilla[0], q_con[9], q_con[10], q_ancilla[3])
    # c14x.barrier() - save 10
    c3x(c14x, q_con[6], q_con[7], q_con[8], q_ancilla[2])
    c3x(c14x, q_con[3], q_con[4], q_con[5], q_ancilla[1])
    c3x(c14x, q_con[0], q_con[1], q_con[2], q_ancilla[0])


print("____________________________________________________________")
print("|                        Solution:                         |\n")

print("Init Circuit - 14 Controls, 1 Target, 5 Ancilla\n")
c14x = QuantumCircuit()
control_qubits = QuantumRegister(14, 'q_c')
target_qubit = QuantumRegister(1, 'q_t')
ancilla_qubits = QuantumRegister(5, 'q_a')
c14x.add_register(control_qubits)
c14x.add_register(target_qubit)
c14x.add_register(ancilla_qubits)

c14x_solution(c14x, control_qubits, target_qubit, ancilla_qubits)

print("|________________________________________________________________|\n")

print("__________________________________________________________________")
print("|                        Compiling to QASM :                     |")
print("QASM file: attached toffoli.qasm")
qasm_str = c14x.qasm(formatted=False, filename='toffoli.qasm')
print("|________________________________________________________________|\n")

print("__________________________________________________________________")
print("|                 Depth Results from QASM file:                  |")
qc = QuantumCircuit.from_qasm_file("toffoli.qasm")
print(" Total depth in QASM is: ", qc.depth(), "\n")
print(" With only gates of :\n", qc.count_ops())
print(" \nDepth calculation : # 2*depth(C3X)*2 + depth(C2X) - Overlaps  = ")
print("                    # 2*(   27   )*2 + (   11   ) - (0+1+9+10)=")
print("                    # 99")
print("|________________________________________________________________|\n")

print("__________________________________________________________________")
print("|                          Circuit:                              |")
print(c14x.draw(output='text'))
print("|________________________________________________________________|\n")

