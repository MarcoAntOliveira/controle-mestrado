import sympy as sp
from param import *
# === Variáveis de tempo ===
t = sp.symbols('t')

# Corrente e tensão
ia = sp.Function('ia')(t)        # corrente de armadura
Vt = sp.Function('Vt')(t)        # tensão terminal
Ea = sp.Function('Ea')(t)        # força contra-eletromotriz

# Velocidade e posição
omega = sp.Function('omega')(t)  # velocidade angular
theta = sp.Function('theta')(t)  # posição angular

# Torque
tau_ele = sp.Function('tau_ele')(t)    # torque elétrico
tau_L= sp.Function('tau_L')(t)        # torque de carga

# === Constantes ===
La, Ra = sp.symbols('La Ra')        # indutância e resistência da armadura
Ke, J, b = sp.symbols('Ke J b')     # constante construtiva, inércia e amortecimento motor
Kt = sp.symbols('Kt')                # constante construtiva torque
JL, bL = sp.symbols('JL bL')        # inércia e amortecimento da carga

# === Equações do sistema ===
eq1 = sp.Eq(Vt, La*ia.diff(t) + Ra*ia + Ea)
eq2 = sp.Eq(Ea, Ke*omega)
eq3 = sp.Eq(omega, theta.diff(t))
eq4 = sp.Eq(tau_ele - tau_L, J*omega.diff(t) + b*omega)
eq5 = sp.Eq(tau_ele, Kt*ia)
eq6 = sp.Eq(tau_L, JL*omega.diff(t) + bL*omega)

# === Mostrar equações ===
equations = [eq1, eq2, eq3, eq4, eq5, eq6]
for i, eq in enumerate(equations, 1):
    sp.pprint(eq)
