from qiskit import QuantumCircuit
import numpy as np
import math

def qft_rotate_single(c: QuantumCircuit, i):
    c.h(i)
    for q in reversed(range(0, i)):
        c.cp(np.pi/2**(i - q), q, i)

def iqft_rotate_single(c: QuantumCircuit, i):
    for q in range(0, i):
        c.cp(-np.pi/2**(i - q), q, i)
    c.h(i)

def iqft_rotate_single2(c: QuantumCircuit, i):
    c.h(i)
    for q in reversed(range(0, i)):
        c.cp(-np.pi/2**(i - q), q, i)

def qft(c: QuantumCircuit):
    for i in reversed(range(c.num_qubits)):
        qft_rotate_single(c, i)
    for i in range(math.floor(c.num_qubits/2)):
        c.swap(i, c.num_qubits - i - 1)

def iqft(c: QuantumCircuit):
    for i in range(math.floor(c.num_qubits/2)):
        c.swap(i, c.num_qubits - i - 1)
    for i in range(c.num_qubits):
        iqft_rotate_single(c, i)
        
def iqft2(c: QuantumCircuit):
    for i in range(math.floor(c.num_qubits/2)):
        c.swap(i, c.num_qubits - i - 1)
    for i in range(c.num_qubits):
        iqft_rotate_single2(c, i)
        