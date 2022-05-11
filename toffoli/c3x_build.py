from qiskit import transpile
from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def c3x(circuit, control1, control2, control3, target):
    theta = np.pi()/8

    circuit.p(+theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 0)], [0.39269908169872414]
    circuit.p(+theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 1)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 0), Qubit(QuantumRegister(3, 'q_in'), 1)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 1)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 0), Qubit(QuantumRegister(3, 'q_in'), 1)], []
    circuit.p(+theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 2)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 1), Qubit(QuantumRegister(3, 'q_in'), 2)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 2)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 0), Qubit(QuantumRegister(3, 'q_in'), 2)], []
    circuit.p(+theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 2)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 1), Qubit(QuantumRegister(3, 'q_in'), 2)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(3, 'q_in'), 2)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 0), Qubit(QuantumRegister(3, 'q_in'), 2)], []
    circuit.h(,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 2), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 1), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(+theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 2), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 0), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(+theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 2), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 1), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(+theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 2), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.p(-theta,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], [-0.39269908169872414]
    circuit.cx(,, )   [Qubit(QuantumRegister(3, 'q_in'), 0), Qubit(QuantumRegister(1, 'q_out'), 0)], []
    circuit.h(,, )   [Qubit(QuantumRegister(1, 'q_out'), 0)], []


# Init Circuit
qc = QuantumCircuit()
q_i = QuantumRegister(3, 'q_in')
q_o = QuantumRegister(1, 'q_out')
qc.add_register(q_i)
qc.add_register(q_o)

qc.mcx([q_i[0],q_i[1],q_i[2]],q_o[0])
qc = qc.decompose()

for gate in qc.data:
    # print('\ngate name:', gate[0].name)
    # print('qubit(s) acted on:', gate[1])
    # print('other paramters (such as angles):', gate[0].params)

    print('circuit.',gate[0].name,'( , , )  ',gate[1],',' ,gate[0].params)