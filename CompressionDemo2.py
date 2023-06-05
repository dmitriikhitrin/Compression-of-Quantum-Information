from CreateWState import CreateWStateCircuit

n = 8
qc1 = CreateWStateCircuit(n)
qc1.barrier()

qc1.cx(1,0)
qc1.cx(2,0)
qc1.cx(3,0)
qc1.cx(4,0)
qc1.cx(5,0)
qc1.cx(6,0)
qc1.cx(7,0)
qc1.barrier()

qc1.cx(2,1)
qc1.cx(2,3)
qc1.ccx(1,3,2)
qc1.barrier()

qc1.cx(4,1)
qc1.cx(4,5)
qc1.ccx(1,5,4)
qc1.barrier()

qc1.cx(6,1)
qc1.cx(6,7)
qc1.ccx(1,7,6)
qc1.barrier()

qc1.cx(5,3)
qc1.cx(5,7)
qc1.ccx(3,7,5)
qc1.barrier()

# Unnecessary operation (see README)
qc1.x(0)
qc1.cx(1,6)
qc1.cx(6,1)
qc1.cx(1,6)
qc1.barrier()
qc1.cx(3,5)
qc1.cx(5,3)
qc1.cx(3,5)