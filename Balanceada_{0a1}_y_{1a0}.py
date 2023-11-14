#Juan Sebastian Buitrago Piñeros
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Inicializar el simulador, matriz y diccionario (servira mas adelante)
simulator, matriz, ayuda_posiciones_matriz = Aer.get_backend('qasm_simulator'), [[0 for _ in range(4)] for _ in range(4)], {"00": 0, "01": 1, "10": 2, "11": 3}

def Analizar_Circuito(circuit, n_circuito):
    """
    Analiza los circuitos dados
    """
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    if n_circuito != None:
        # Obtener la única clave del diccionario "counts"
        clave = list(counts.keys())[0]
        matriz[n_circuito][ayuda_posiciones_matriz[clave]] = 1
        print("\nCircuito #", n_circuito + 1)
    else:
        # Dice explicitamente si es Balanceada o Constante
        if "00" in counts.keys():
            print("\nEs Constante")
        else:
            print("\nEs Balanceada")
    print("\nTotal count for 00 and 11 are:", counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

# Circuito de Entrada 00
circuit = QuantumCircuit(2, 2)
circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()
circuit.measure(0,1)
circuit.measure(1,0)
Analizar_Circuito(circuit, 0)

# Circuito de Entrada 01
circuit = QuantumCircuit(2, 2)
circuit.x(1)
circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()
circuit.measure(0,1)
circuit.measure(1,0)
Analizar_Circuito(circuit, 1)

# Circuito de Entrada 10
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()
circuit.measure(0,1)
circuit.measure(1,0)
Analizar_Circuito(circuit, 2)

# Circuito de Entrada 11
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()
circuit.measure(0,1)
circuit.measure(1,0)
Analizar_Circuito(circuit, 3)

# Imprimir Matriz
print("\nMatriz Correspondiente")
for fila in matriz:
    print(fila)

# Algoritmo de Deutsch para comprobar si la funcion es balanceada o constante.
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.x(1)
circuit.h(1)
circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()
circuit.h(0)
circuit.barrier()
circuit.measure(0,0)
Analizar_Circuito(circuit, None)