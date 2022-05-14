
"(x0 != x1) and"
"(x2 + 2 != x3) and"
"(x3 != x4) and"
"(x1 != x3) and"
"(x3 != x5) and"
"(x5 != x6) and"
"(x0 != x2) and"
"(x1 != x5) and"
"(x4 != x6) and"
"(x3 == 2) and"
"(x2 + x4 + x3 == 3)"


from qiskit import QuantumCircuit, QuantumRegister

kakuru = QuantumCircuit()
control_qubits = QuantumRegister(14, 'q_c')
target_qubit = QuantumRegister(1, 'q_t')
ancilla_qubits = QuantumRegister(5, 'q_a')

def not_equal(circuit, control1, control2, ancilla):
    circuit.x(control1)
    circuit.ccx(control1, control2, ancilla)
    circuit.x(control2)
