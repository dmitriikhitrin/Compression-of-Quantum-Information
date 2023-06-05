# Compression-of-Quantum-Information

The ultimate goal of the project is to find a sequence of unitary operations to compress any quantum state $\ket{\psi}$ into some other state $\ket{\psi_1}$ that conveys the same information utilizing smaller number of qubits. The general idea and mathematical formalism is described in (1).

## Theory
The number of qubits used to describe the initial state does not matter as much as the number of basis states in the superposition. If there are N basis states, $ket{\psi}$ can be described using $ceil(\log_2{N})$ qubits without losing any information. <br />

Quantum Information is enclosed in amplitudes of basis states, so we do not want to change this amplitudes by creating or collapsing superposition. Thus, the compression should be done using Pauli X, CNOT, and multi-controll X (MCX) gates.

Since unitaries are inversable, we can always proceed back to the initial state by applying $U^\dagger $

## Demos
To demonstrate the precedure, I show the compression of $\ket{W_8}$ state. Since there are 8 basis states in the superposition, it can be compressed into $\log_{2}(8) = 3$ qubit state. The transformation $U$ must satisfy:

$U\frac{1}{\sqrt{8}}\sum\ket{2^{i}} = \frac{1}{\sqrt{8}}\ket{00000} \otimes \sum\ket{i}$, <br />
where i ranges from 0 to 7 in my case.

# Demo 1
It is relatively easy to eyeball the right sequence of gates to compress $\ket{W_8}$. In the first demo, I came up with the following circuit:


## Acknowledgements
1) https://doi.org/10.48550/arXiv.1612.02806
2) https://web.wpi.edu/Pubs/E-project/Available/E-project-051620-220950/unrestricted/Constructions_and_Applications_of_W-States.pdf
