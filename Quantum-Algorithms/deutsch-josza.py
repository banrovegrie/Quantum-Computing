import qiskit
import numpy as np
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, transpile, Aer


def oracle(circuit, n):
    case = np.random.randint(2)

    # consider the function to be constant
    if case == 1:
        print("Example Constant:")
        output = np.random.randint(2)
        if output == 1:
            circuit.x(n)
        return circuit

    # example of a balanced function
    else:
        print("Example Balanced:")
        circuit.cx(0, n)
        return circuit


def deutsch_josza(n):
    circuit = QuantumCircuit(n + 1, n + 1)
    for i in range(0, n):
        circuit.h(i)
    circuit.x(n)
    circuit.h(n)
    circuit = oracle(circuit, n)
    for i in range(0, n):
        circuit.h(i)

    for i in range(0, n):
        circuit.measure(i, i)

    print(circuit)
    return circuit


circ = deutsch_josza(3)
simulator = Aer.get_backend('aer_simulator')
circ = transpile(circ, simulator)
result = simulator.run(circ).result()
counts = result.get_counts(circ)
print(counts)
plot_histogram(counts, title='Bell-State counts')
