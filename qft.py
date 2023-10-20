from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer
import lib
import matplotlib.pyplot as plt

N = 3

if __name__ == '__main__':
    qc = QuantumCircuit(N, N)
    lib.qft(qc)
    lib.iqft2(qc)
    #qc.draw(output='mpl')
    #plt.show()
    
    sim = Aer.get_backend('statevector_simulator')
    result = execute(qc, sim).result()
    state_vec = result.get_statevector(qc)
    print(state_vec)
    
    pass