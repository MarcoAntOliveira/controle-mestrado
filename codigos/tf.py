import sympy as sp
from param import *  # importa os parâmetros numéricos

# === Variáveis de tempo ===
t = sp.symbols('t')

# === Corrente e tensão ===
ia = sp.Function('ia')(t)
Vt = sp.Function('Vt')(t)
Ea = sp.Function('Ea')(t)

# === Velocidade e posição ===
omega = sp.Function('omega')(t)
theta = sp.Function('theta')(t)

# === Torque ===
tau_ele = sp.Function('tau_ele')(t)
tau_L = sp.Function('tau_L')(t)

# === Constantes simbólicas ===
La_s, Ra_s = sp.symbols('La Ra')
Ke_s, J_s, b_s = sp.symbols('Ke J b')
Kt_s = sp.symbols('Kt')
Jl_s, bl_s = sp.symbols('Jl bl')

# === Domínio de Laplace
S = sp.symbols('S')


# === Corrente e tensão ===
Ia = sp.Function('Ia')(S)
Vt = sp.Function('Vt')(S)
Ea = sp.Function('Ea')(S)

# === Velocidade e posição ===
Omega = sp.Function('Omega')(S)
Theta = sp.Function('Theta')(S)


# === Torque ===
tau_ele = sp.Function('tau_ele')(S)
tau_L = sp.Function('tau_L')(S)


# === Equações ===
eq1 = sp.Eq(Vt, La_s*ia.diff(t) + Ra_s*ia + Ea)
eq2 = sp.Eq(Ea, Ke_s*omega)
eq3 = sp.Eq(omega, theta.diff(t))
eq4 = sp.Eq(tau_ele - tau_L, J_s*omega.diff(t) + b_s*omega)
eq5 = sp.Eq(tau_ele, Kt_s*ia)
eq6 = sp.Eq(tau_L, Jl_s*omega.diff(t) + bl_s*omega)
# === Equações no domínio de Laplace
eq7 = sp.Eq(Vt, (La_s*S + Ra_s)*Ia + Ea )
eq8 = sp.Eq(tau_ele, Kt*Ia)

equations = [eq1, eq2, eq3, eq4, eq5, eq6]

# === Substituir valores numéricos ===
subs_dict = {
    La_s: La,
    Ra_s: Ra,
    Ke_s: Ke,
    Kt_s: Kt,
    J_s: J,
    b_s: b,
    Jl_s: Jl,
    bl_s: bl
}

# # Exemplo: substituindo nas equações
# eqs_num = [eq.subs(subs_dict) for eq in equations]

# # === Exibir ===
# for i, eq in enumerate(eqs_num, 1):
#     print(f"\nEquação {i}:")
#     sp.pprint(eq)
eq_num7 = eq7.subs(subs_dict)
sp.pprint(eq8)