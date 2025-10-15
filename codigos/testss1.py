import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Parâmetros do sistema
m = 1.0
c = 0.5
k = 2.0

# Matrizes do espaço de estados
A = np.array([[0, 1],
              [-k/m, -c/m]])
B = np.array([[0],
              [1/m]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Sistema no espaço de estados
sys = ctl.ss(A, B, C, D)

# --- Projeto do controlador por alocação de polos ---
# Queremos colocar os polos em -2 e -3 (mais rápidos e estáveis)
desired_poles = [-2, -3]
K = ctl.place(A, B, desired_poles)

print("Matriz de realimentação K:", K)

# Novo sistema em malha fechada: (A - BK)
A_cl = A - B @ K
sys_cl = ctl.ss(A_cl, B, C, D)

# Simulação com entrada degrau
t = np.linspace(0, 10, 500)
t, y = ctl.forced_response(sys_cl, T=t, U=np.ones_like(t))

# --- Plot ---
plt.figure(figsize=(8,4))
plt.plot(t, y, label="Saída controlada")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (x)")
plt.title("Controle por realimentação de estados (place)")
plt.grid(True)
plt.legend()
plt.show()
