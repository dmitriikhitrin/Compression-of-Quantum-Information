from qiskit import QuantumCircuit
import qiskit.quantum_info as qi
from math import sqrt


def CreateWStateCircuit(n):
    operators = [qi.Operator([[sqrt(n-1)/sqrt(n), 1/sqrt(n)], 
                    [1/sqrt(n),        -sqrt(n-1)/sqrt(n)]])
         for n in range(1,n+1)]

    gates = []

    qcUse = QuantumCircuit(1)
    qcUse.x(0)

    gate = qcUse.to_gate(label = 'CS' + str(1) + 'X').control(1)
    gates.append(gate)


    for i in range(1,n-1):
        qcUse = QuantumCircuit(1)

        qcUse.unitary(operators[i], 0)
        qcUse.x(0)

        gate = qcUse.to_gate(label = 'CS' + str(i+1) + 'X').control(1)
        gates.append(gate)


    qcUse = QuantumCircuit(1)
    qcUse.unitary(operators[n-1], 0)
    qcUse.x(0)
    gate = qcUse.to_gate(label = 'CS' + str(n) + 'X')
    gates.append(gate)
    
    
    qc = QuantumCircuit(n)

    qc.append(gates[n-1], [0])

    for i in range(n-1):
        qc.append(gates[n-2-i], [i, i+1])

    for i in range(n-2):
        qc.cx(n-i-3, n-i-2)

    qc.x(0)
    
    return qc