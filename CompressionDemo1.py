from CreateWState import CreateWStateCircuit

# |W8> state preparation
n = 8
qc = CreateWStateCircuit(n)
qc.barrier()

# compression
qc.cx(0,7)
qc.cx(0,6)
qc.ccx(6,7, 0)
qc.barrier()

qc.cx(1,5)
qc.cx(1,6)
qc.ccx(5,6, 1)
qc.barrier()

qc.cx(4,5)
qc.cx(4, 7)
qc.ccx(5,7, 4)
qc.barrier()

qc.cx(3, 5)
qc.cx(3, 6)
qc.cx(3, 7)
qc.mcx([5,6,7], 3)
qc.barrier()

qc.x(0)
qc.x(1)
qc.x(3)
qc.x(4)
qc.x(5)
qc.x(6)
qc.x(7)
qc.mcx([0,1,3,4,5,6,7], 2)
qc.x(0)
qc.x(1)
qc.x(3)
qc.x(4)
qc.x(5)
qc.x(6)
qc.x(7)