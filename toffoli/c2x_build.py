from qiskit import transpile
from qiskit import QuantumCircuit, QuantumRegister

# def c2x(circuit, q_c0, q_c1, q_t):
#     circuit.h(q_t)
#     circuit.cx(q_c1, q_t)
#     circuit.tdg(q_t)
#     circuit.cx(q_c0, q_t)
#     circuit.t(q_t)
#     circuit.cx(q_c1, q_t)
#     circuit.tdg(q_t)
#     circuit.cx(q_c0, q_t)
#     circuit.t(q_t)
#     circuit.h(q_t)
#     circuit.t(q_c1)
#     circuit.cx(q_c0, q_c1)
#     circuit.t(q_c0)
#     circuit.tdg(q_c1)
#     circuit.cx(q_c0, q_c1)


# Init Circuit
qc = QuantumCircuit()
q_i = QuantumRegister(2, 'q_c')
q_o = QuantumRegister(1, 'q_t')
qc.add_register(q_i)
qc.add_register(q_o)

qc.ccx(q_i[0],q_i[1],q_o[0])
qc = qc.decompose()

c2x(qc,q_i[0],q_i[1],q_o[0])
qc.draw()

# for gate in qc.data:
#     # print('\ngate name:', gate[0].name)
#     # print('qubit(s) acted on:', gate[1])
#     # print('other paramters (such as angles):', gate[0].params)
#
#     # print('circuit.',gate[0].name,'(',gate[0].params,')')
#
#     if gate[0].name == 'cx':
#         print('circuit.cx(',
#               gate[1][0].register.name+str(gate[1][0].index),',',
#               gate[1][1].register.name+str(gate[1][1].index) , ')')
#
#     if gate[0].name == 'tdg' or gate[0].name == 't' or gate[0].name == 'h':
#         print('circuit.'+gate[0].name+'(',
#               gate[1][0].register.name+str(gate[1][0].index),')')