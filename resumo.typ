
== Controlador PID
 - O controlador PID tem oseguinte formato:
 $G_C(S) = K_p + K_i/S + K_d S arrow G_c(S) = K_p [1 + 1/(T_i s) + T_d S]$

 - $K_p$ -  A ação proporcional sobre o sinal de erro no tempo atual, enviando uma
ação de comando proporcional ao erro apurado;
- É óbvio que quanto maior o erro apurado, mais efetiva será a ação de
controle devida e este termo;
- Note também que esta ação de controle não leva em conta condições
passadas do sinal de erro $(u(t) = K_p e(t))$, apenas o que ocorre no
momento atual;
- A ação proporcional tem efeito tanto na velocidade quanto na precisão
do sistema. Entrentanto, ela pode causar considerável redução nas
margens de estabilidade

- $G_c(S) = K_i/S = u(t) = \u{222b}_(t) K_i e(t)$
- Essa ação opera sobre a integral do sinal de erro. Assim, ela atua sobre
erros remanescentes de períodos anteriores, ainda não corrigidos;
- Sua principal função é, então, corrigir erros persistentes. Pode ser vista
como uma correção sobre a história “passada” do erro do sistema, com
foco no regime estacionário;
- Seu principal efeito colateral é reduzir a velocidade de
resposta do sistema.
$G_C(S) =K_d S arrow u(t) = d e(t)/d t $
A ação opera sobre a derivada do sinal de erro. Então, ela atuando sobre a tendáncia de evolução deste sinal; Pode ser vista como uma correção sobre a história “futura” do erro do sistema de controle, já que
atua sobre sua tendéncia de evolução.
Tem forte influéncia na resposta transitória. Deve ser utilizada com critério, pois afeta fortemente as margens de estabilidade e contribui para a amplificação de ruídos presentes na malha.

== Controlador PID salto de referencia
Em consequncia do controlador não ser implementavel na sua versão original, devido não ser próprio e conseque
ntemente causal\
$G_(c-d e r v) = (T_d S)/(1 + gamma T_d S $

com $gamma < 0.1$ isso cria um polo adicionalno controlador, mas que é dominado pela dinâmica 
do PID

