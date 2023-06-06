# Compression-of-Quantum-Information

The ultimate goal of the project is to find a sequence of unitary operations to compress any quantum state $\ket{\psi}$ into some other state $\ket{\psi_1}$ that conveys the same information utilizing a smaller number of qubits. The general idea and mathematical formalism are described in (1).

## Theory
The number of qubits used to describe the initial state does not matter as much as the number of basis states in the superposition. If there are N basis states, $\ket{\psi}$ can be described using $ceil(\log_2{N})$ qubits without losing any information. <br />

Quantum Information is enclosed in amplitudes of basis states, so we do not want to change these amplitudes by creating or collapsing superposition. Thus, the compression should be done using Pauli X, CNOT, and multi-control X (MCX) gates.

Since unitaries are invertible, we can always proceed back to the initial state by applying $U^\dagger $

## Demos
To demonstrate the procedure, I show the compression of $\ket{W_8}$ state using Qiskit. Since there are 8 basis states in the superposition, it can be compressed into $\log_{2}(8) = 3$ qubit state. The transformation $U$ must satisfy:

$U\frac{1}{\sqrt{8}}\sum\ket{2^{i}} = \frac{1}{\sqrt{8}}\ket{00000} \otimes \sum\ket{i}$, <br />
where i ranges from 0 to 7 in my case.

### Demo 1
It is relatively easy to eyeball the right sequence of gates to compress $\ket{W_8}$. In the first demo, I came up with the following circuit: <br />
<img width="700" alt="image" src="https://github.com/dmitriikhitrin/Compression-of-Quantum-Information/assets/122756262/fc92da36-c759-4d58-8d9c-baecd52c40f1">

Here, the first block of the circuit evolves $\ket{0}^{\otimes8}$ to $\ket{W_8}$ according to the method described in (2). The probability distributions before and after applying all the gates after the first barrier are:

 $\ket{W_8}$ (10000 runs)|  Compressed state (10000 runs)
:-------------------------:|:-------------------------:
<img width="473" alt="image" src="https://github.com/dmitriikhitrin/Compression-of-Quantum-Information/assets/122756262/e606c836-2354-43cf-8404-d22e5cfd1727"> | <img width="475" alt="image" src="https://github.com/dmitriikhitrin/Compression-of-Quantum-Information/assets/122756262/9f701e83-440b-40c1-8801-28ee05c91ee4"> <br />

After the compression, only qubits 5,6, and 7 are used while 0,1,2,3,4 remain in $\ket{0}$ and are ready to be utilized further.

### Demo 2
In the second demo, I only used CNOT and Toffoli gates for compression:
<img width="700" alt="image" src="https://github.com/dmitriikhitrin/Compression-of-Quantum-Information/assets/122756262/811b0404-8995-490d-b211-8b58bf22ac74"> <br />
The probability distributions before and after applying all the gates after the first barrier are:
 $\ket{W_8}$ (10000 runs) | Compressed state (10000 runs)
:-------------------------:|:-------------------------:
<img width="470" alt="image" src="https://github.com/dmitriikhitrin/Compression-of-Quantum-Information/assets/122756262/4b8a9171-b051-4058-9843-0375638dba55">  | <img width="465" alt="image" src="https://github.com/dmitriikhitrin/Compression-of-Quantum-Information/assets/122756262/2d5207f1-0933-46e0-8f78-eb2e2141051f"> <br />

After the compression, only qubits 1,3, and 7 are used while 2,4,5,6 remain in $\ket{0}$ and 0 is in $\ket{1}$ (which can be easily changed to 0 by applying X gate)

## Further Research
My theory is that the compression can be done using only X, CNOT, and Toffoli

## Acknowledgements
1) https://doi.org/10.48550/arXiv.1612.02806
2) https://web.wpi.edu/Pubs/E-project/Available/E-project-051620-220950/unrestricted/Constructions_and_Applications_of_W-States.pdf
