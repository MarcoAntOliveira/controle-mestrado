import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

# Parâmetros do sistema
m = 1.0   # massa
c = 0.5   # amortecimento
k = 2.0   # rigidez

# Matrizes do espaço de estados
A = np.array([[0, 1],
              [-k/m, -c/m]])
B = np.array([[0],
              [1/m]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Criação do sistema
sys = StateSpace(A, B, C, D)

# Tempo de simulação
t = np.linspace(0, 10, 1000)

# Entrada: degrau unitário
u = np.ones_like(t)

# Simulação
t, y, x = lsim(sys, U=u, T=t)

# Plot
plt.figure(figsize=(8,4))
plt.plot(t, y, label="Resposta y(t)")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.title("Sistema Massa-Mola-Amortecedor em Espaço de Estados")
plt.grid(True)
plt.legend()
plt.show()
