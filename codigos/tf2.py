import sympy as sp

# Símbolos
s = sp.symbols('s')
La_s, Ra_s, Kt, Ke, J, b = sp.symbols('La_s Ra_s Kt Ke J b')
Vt, Ia, Omega, tau_ele, tau_L = sp.symbols('Vt Ia Omega tau_ele tau_L')

# === Equações ===
eq7 = sp.Eq(Vt, (La_s*s + Ra_s)*Ia + Ke*Omega)
eq8 = sp.Eq(tau_ele, Kt*Ia)
eqM = sp.Eq(tau_ele - tau_L, (J*s + b)*Omega)  # Equação mecânica

# === Substituições passo a passo ===
# 1. Isolar Ia em função de Vt e Omega
Ia_expr = sp.solve(eq7, Ia)[0]

# 2. Substituir Ia em tau_ele = Kt*Ia
tau_expr = eq8.subs(Ia, Ia_expr).rhs

# 3. Substituir tau_ele na equação mecânica e resolver para Omega
Omega_expr = sp.solve(eqM.subs(tau_ele, tau_expr), Omega)[0]

# === Separar em termos de Vt e tau_L ===
Omega_Vt = sp.simplify(sp.diff(Omega_expr, Vt))
Omega_TL = sp.simplify(sp.diff(Omega_expr, tau_L))

# === Expressões das funções de transferência ===
Gv = sp.simplify(Omega_Vt)
Gl = sp.simplify(Omega_TL)

print("Função de transferência da tensão para a velocidade Ω/Vt:")
sp.pprint(Gv)
print("\nFunção de transferência do torque de carga para a velocidade Ω/TL:")
sp.pprint(Gl)

