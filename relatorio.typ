#set math.equation(numbering: "(1)")

= Modelo do Motor CC

Queremos encontrar a função de transferência entre a **tensão de armadura** 
(entrada) e a **velocidade angular** (saída):

$ H(s) = Ω(s) / V_t(s) $

== Equações no tempo

1. Equação elétrica:
$ V_t(t) = L_a \dot{i}_a(t) + R_a i_a(t) + E_a(t) $

com $ E_a(t) = K_e ω(t) $

2. Equação mecânica:
$ T_ele(t) - T_L(t) = J \dot{ω}(t) + b ω(t) $

assumindo $ T_L = 0 $:
$ T_ele(t) = J \dot{ω}(t) + b ω(t) $

3. Torque eletromagnético:
$ T_ele(t) = K_t i_a(t) $

== No domínio de Laplace

1. Elétrica:
$ V_t(s) = (L_a s + R_a) I_a(s) + K_e Ω(s) $

2. Mecânica:
$ K_t I_a(s) = (Js + b) Ω(s) $

== Eliminação de $I_a(s)$

De (2):
$ I_a(s) = \frac{(Js+b)}{K_t} Ω(s) $

Substituindo em (1):

$ V_t(s) = \left(\frac{(L_a s + R_a)(Js+b)}{K_t} + K_e\right) Ω(s) $

== Função de transferência

$ H(s) = \frac{Ω(s)}{V_t(s)} 
= \frac{K_t}{(L_a s + R_a)(Js+b) + K_t K_e} $


