O artigo "The dilemma of PID tuning" (O dilema da sintonia PID) é um artigo de revisão publicado na *Annual Reviews in Control*, volume 52 (2021), páginas 65–74. Os autores são Oluwasegun Ayokunle Somefun, Kayode Akingbade e Folasade Dahunsi.

Abaixo está a tradução integral do artigo com base nos excertos fornecidos nas fontes a.

***

## Annual Reviews in Control 52 (2021) 65–74

### Artigo de Revisão
### O dilema da sintonia PID
Oluwasegun Ayokunle Somefun a,∗, Kayode Akingbade b, Folasade Dahunsi a
a Departamento de Engenharia da Computação, Universidade Federal de Tecnologia Akure, Nigéria
b Departamento de Engenharia Elétrica e Eletrônica, Universidade Federal de Tecnologia Akure, Nigéria

**Palavras-chave:** Controle PID, Sintonia PID, Otimização, Sistema Dinâmico, Identificação do tempo de assentamento, Identificação do sistema.

### Resumo

Muitas tarefas de controle de feedback automático e aprendizado realizadas em muitos sistemas dinâmicos ainda dependem fundamentalmente de uma forma de **lei de controle Proporcional–Integral–Derivativo (PID)**. A lei PID é frequentemente vista como um algoritmo de controle computacional simplista. No entanto, assim como todos os problemas de otimização não convexa, a sintonia do algoritmo PID para um controle de malha fechada preciso e estável se torna um **Problema NP-Hard**.

Isto leva a um dilema de complexidade e custo, tanto para usuários quanto para projetistas, especialmente na prática. Não é de admirar, então, que **softwares de sintonia** sejam um grande negócio no setor de automação industrial.

Nesta revisão, apresentamos e classificamos os métodos de sintonia PID até o momento em três áreas gerais. Finalmente, apresentamos uma proposta para minimizar o dilema de complexidade e custo que se associou à sintonia dos três principais parâmetros da lei de controle PID. Espera-se que tentativas contínuas de minimização deste dilema possam levar tanto a um investimento de economia de dinheiro quanto a uma melhoria significativa no campo do projeto de controle PID.

### 1. Introdução

O controlador em *software* é conhecido como um **algoritmo de controle**, e é o cérebro de um sistema de controle automático. A teoria do projeto de sistemas de controle estuda como os algoritmos de controle são projetados sistematicamente e como garantir seu desempenho estável e preciso (Guo, 2020). Um conceito central na teoria de controle é o **princípio de feedback**. O principal objetivo do feedback é lidar com a influência de fatores internos incertos do sistema e fatores externos na estabilidade e precisão do desempenho da(s) saída(s) medida(s) de um sistema, comumente chamada de variável de processo.

Uma motivação central no projeto do controlador é a necessidade de **desempenho garantido estável e preciso em malha fechada** de sistemas dinâmicos. O desempenho de malha fechada é crítico em termos de precisão e estabilidade, especialmente em tarefas de controle de motor. Um controlador de feedback bem projetado é um investimento real de economia de dinheiro e de vida (Yang, 2020). Tanto a otimalidade quanto, mais importante, a **robustez** são importantes (Keel, & Bhattacharyya, 2016) diante da incerteza. Na prática, muitas tarefas de automação ainda dependem fundamentalmente de uma forma de controle **Proporcional–Integral–Derivativo (PID)** (Abramovitch, Hoen, & Workman, 2008; Guo, 2020).

Nesta revisão, os métodos de projeto (sintonia) de controle PID são apresentados a partir da perspectiva de serem **baseados em modelo da planta**, **livres de modelo da planta** ou um **híbrido** de ambos. O foco é dar uma revisão concisa do **dilema de complexidade e custo** na sintonia da lei de controle PID. Apesar do crescimento de *softwares* de sintonia industrial, a maioria das malhas PID em tempo real ainda se comporta mal após algum tempo e precisa de ressintonia (*retuning*), aumentando os custos de manutenção (Díaz-Rodríguez, Oliveira, & Bhattacharyya, 2015; Koelsch, 2014).

Um pré-requisito principal para o projeto de controle sistemático é que alguma forma de modelo é sempre necessária para o controle garantido (Campestrini et al., 2017; Gevers, 1996; Van Den Hof, & Schrama, 1995). Concluímos esta revisão propondo uma teoria para simplificar os custos e as complexidades da identificação de modelo demorada e da otimização computacionalmente cara envolvida na sintonia PID. Argumentamos que a informação de tempo, especificamente o **tempo de assentamento de entrada-saída de malha fechada** (*closed-loop input–output settling-time*), pode ser uma propriedade de dinâmica de sistema suficiente para modelar sistemas de feedback. O desenvolvimento de métodos automáticos e robustos para esta identificação de tempo de assentamento é um problema em aberto.

### 2. Lei de Controle PID

O trabalho seminal de Minorsky (1922) realizou a lei PID como uma **mímica computacional do princípio natural de controle percepção–ação**. A estrutura do PID usa informações de erro passadas, presentes e futuras estimadas (Bennett, 2001).

Hoje, uma representação geral é uma estrutura de controle de **dois graus de liberdade (2DOF)** (Abdelaty et al., 2018; Araki, & Taguchi, 2003; Aström, & Hägglund, 1995; Viteckova, & Vitecek, 2015; Wang, 2012), visando a rejeição simultânea de distúrbios e o rastreamento do ponto de ajuste.

A estrutura 2DOF é dada por:
$$u = \mathcal{G}(r, \text{sat}(y)) = K_p (u_p + u_i + u_d)$$

Onde os termos contribuintes são:
$$u_p = e_p, \quad u_i = T_i^{-1} e_i, \quad u_d = T_d e_d$$

E os erros são:
$$e_p = b r - y^*$$
$$e_i = \int (r - y^*) dt = \int e dt \equiv s^{-1}e$$
$$e_d = c \dot{r} - \dot{y}^* \equiv s (c r - y^*)$$

$K_p \in \mathbb{R}$ é o ganho proporcional, $T_i \in \mathbb{R}$ é a constante de tempo integral, $T_d \in \mathbb{R}$ é a constante de tempo derivativa, e $e \in \mathbb{R}$ é o sinal de erro total. $b$ e $c \in \mathbb{R}^{+}$ são os pesos do ponto de ajuste.

**Formalismo PID Moderno:** Em uma dissertação recente (Somefun, 2021), o PID foi redefinido em uma **forma crítica** (6), introduzindo pesos críticos ($\lambda_p, \lambda_i, \lambda_d \in \mathbb{R}^{+}$) no ganho proporcional:
$$u = \mathcal{G}(r, \text{sat}(y)) = K_p (\lambda_p u_p + \lambda_i u_i + \lambda_d u_d)$$

**Motivações e Sucessos:** Qualquer estrutura de controle ou aprendizado que envolva feedback de erro é uma forma da lei PID. O controle PID é considerado **onipresente** (Aström & Hägglund, 1995; Johnson & Moradi, 2005; Samad, 2017; Wang, 2020) e continua a fornecer um desempenho de controle robusto, simples, de menor custo e satisfatório (Bucz, & Kozáková, 2018; Li, & Wang, 2016; Peretz, 2018; Wang, 2020; Yu, 2018).

Mais recentemente, o PID tem sido aplicado como um **otimizador no treinamento de pesos de redes neurais profundas** (Wang et al., 2020). Teorias robustas como o Controle com Atraso de Tempo (TDC) (Roy, & Kar, 2020) e a Estimação de Distúrbio Incerto (UDE) (Zhong, Kuperman, & Stobart, 2011) foram demonstradas como redutíveis a uma forma específica de controle PID (Chang, & Jung, 2009; Nam, 2016).

Embora se esperasse que métodos avançados como MPC e redes neurais o tornassem obsoleto (Aström & Hägglund, 2018; Johnson & Moradi, 2005), a lei PID não é uma lembrança do século passado (Aström & Hägglund, 2018). A comunidade de controle tem tido sucesso limitado em obter robustez através de otimização quadrática nas últimas seis décadas, pois leva a controladores de alta ordem e frágeis (Keel, & Bhattacharyya, 1997; Keel & Bhattacharyya, 2016).

O nível mais baixo de todas as arquiteturas de sistemas complexos ainda é uma **malha regulatória PID** (Katebi, 2007). O PID goza de uso popular em muitas indústrias, como a química, alimentícia, de petróleo e gás, e eletrônica (Diaz-Rodriguez et al., 2019).

Os problemas de desempenho do PID são rastreados para **parâmetros operacionais mal escolhidos** ou **variações adversas** (incerteza) na dinâmica do sistema. Um grande percentual de controladores PID em operação está no modo manual, e a maioria das malhas em automático se comporta pior após algum tempo do que em malha aberta (Koelsch, 2014).

### 3. Representações: Ordem Inteira ou Ordem Fracionária

Equações diferenciais (EDs) são a linguagem universal para descrever sistemas dinâmicos (Li, Zheng, & Wang, 2019). Há um crescente corpo de pesquisa sobre controladores PID de ordem fracionária (FOPID).

Na forma fracionária, as equações se tornam:
$$e_i = \mathbf{D}^{-\mu}e(t) \equiv s^{-\mu}e$$
$$e_d = \mathbf{D}^{\delta}(c r - y^*) \equiv s^{\delta}(c r - y^*)$$

O interesse nos FOPIDs é atribuído ao grau extra de liberdade de sintonia, permitindo a **modelagem da resposta em frequência** (Dastjerdi et al., 2019; Tepljakov et al., 2021; Vinagre et al., 2007). No entanto, é difícil validar a vantagem custo-benefício, pois são mais **computacionalmente caras** em termos de memória e velocidade de execução (Petráš, 2012).

A implementação em tempo real de FOPIDs é usualmente aproximada a representações equivalentes de **filtro linear de ordem inteira superior** (Dastjerdi et al., 2019). Atualmente, os engenheiros de controle ainda enfrentam um dilema na escolha entre representações fracionárias e de ordem inteira do PID. Para a realização de controladores em tempo real para fins de controle crítico de segurança, o uso de **representações de ordem inteira permanece a escolha dominante**, pois reduz a complexidade computacional e de sintonia do PID.

### 4. Problema de Sintonia PID

O problema de sintonia dos controladores PID atrai interesse de pesquisa incessante (Aström & Hägglund, 2018; Vilanova, & Visioli, 2012; Wang et al., 2018). A melhor solução para sintonizar uma malha PID fechada permanece uma questão em aberto. Uma razão é a **ausência de modelos perfeitos** para descrever sistemas do mundo real, que são inerentemente incertos (Ang et al., 2005; Dastjerdi et al., 2018; Jantzen, & Jakobsen, 2016; Sung et al., 2009).

A seleção sistemática do conjunto ótimo de parâmetros PID foi categorizada como um **Problema NP-hard** em termos de complexidade (Koszaka et al., 2006).

Os métodos de sintonia PID podem ser categorizados em três perspectivas gerais:

1.  **Métodos Baseados em Modelo da Planta** (Plant-model based methods).
2.  **Métodos Livres de Modelo da Planta** (Plant-model free methods).
3.  **Métodos Híbridos** (Hybrid methods).

A sintonia pode ser realizada **offline** ou **online**.

### 5. Métodos Baseados em Modelo da Planta

Uma grande porcentagem dos métodos de projeto de controle PID depende do **conhecimento de aproximações de modelos matemáticos**. Os parâmetros identificados desses modelos são explicitamente usados como constantes de projeto para definir os parâmetros PID (Levine, 2011; Li & Wang, 2016; Skogestad, 2006; Sung et al., 2009; Visioli, 2006).

**Outros métodos modernos** incluem controle preditivo por modelo (MPC) (Klaučo, & Kvasnica, 2019), H-infinito (Diaz-Rodriguez et al., 2019), teoria de feedback quantitativo (QFT) (Comasòlivas et al., 2012; Mercader et al., 2017) e controle Gaussiano Quadrático Linear (LQG).

Esses modelos são **representações imperfeitas** dos sistemas físicos, que são inerentemente não lineares e incertos (Guo, 2020). As desvantagens incluem:

1.  Modelos imperfeitos em comparação com a dinâmica real da planta.
2.  Ressintonia significativa pode ser frequentemente necessária.
3.  Processo de identificação demorado.
4.  Uso intensivo de técnicas de otimização numérica.

### 6. Métodos Livres de Modelo da Planta

Estes são abordagens de projeto de controle **puramente orientadas por dados** que evitam a identificação explícita de parâmetros de uma estrutura de modelo. A sintonia baseia-se em dados de entrada-saída de malha fechada e na **minimização de alguma função objetivo**.

Uma técnica popular é o **Teste de Feedback por Relé (RFT)** (Boiko, 2013), que usa a Auto-sintonia por Relé (Aström & Hägglund, 2018) para automatizar a identificação da resposta em frequência.

Outros métodos notáveis incluem sintonia de feedback iterativo (IFT) (Ho et al., 2003), controle de aprendizado iterativo (ILC) (Moore, & Xu, 2000) e método de busca de extremo (ES) (Killingsworth & Krstic, 2006). O ILC, por exemplo, requer que os sistemas físicos satisfaçam uma **condição de inicialização idêntica**, o que é restritivo (Guan et al., 2014; Preitl et al., 2007).

As desvantagens gerais incluem:

1.  **Condições de projeto restritivas** para sistemas práticos.
2.  Otimizações de minimização de erro mais **computacionalmente caras** e às vezes não confiáveis.
3.  Experimentos orientados por dados demorados.
4.  O controle nominal é tão bom quanto os dados, e o controle real pode ser **subótimo**.

### 7. Métodos Híbridos

Combinam o uso de alguma forma de **conhecimento do modelo da planta** (não necessariamente uma estrutura paramétrica) com **abordagens orientadas por dados**.

Métodos de **alocação de autovalores dominantes** (ou alocação de polo) são notáveis nesta categoria, onde o desempenho está diretamente relacionado à distribuição de autovalores de malha fechada (Datta et al., 2013; Diaz-Rodriguez et al., 2019; Han, & Bhattacharyya, 2018; Keel & Bhattacharyya, 2016; Srivastava, & Pandit, 2016; Wang, Han, Liu, & He, 2020; Zítek et al., 2013).

Uma tendência recente propõe **algoritmos de otimização meta-heurísticos (evolucionários)** (Almabrok et al., 2018; Ekinci, & Hekımoğlu, 2019; Hekimoğlu, 2019; Izci, & Ekinci, 2021; Mandava, & Vundavilli, 2019).

Outros métodos notáveis exploram **lógica fuzzy, redes neurais e aprendizado por reforço** (Jafari, & Dhaouadi, 2011; Kofinas, & Dounis, 2019; Malekabadi et al., 2018; Marino, & Neri, 2019; Mendel, 2017; Pirasteh-Moghadam et al., 2020; Savran, & Kahraman, 2014; Shipman, & Coetzee, 2019; Srivastava et al., 2018; Taeib, & Chaari, 2015; Wang, Cheng, & Sun, 2007).

As desvantagens gerais dos métodos híbridos incluem:

1.  Uso dominante de diferentes tipos de heurísticas ou otimizações.
2.  Heredam problemas de suas bases, podendo levar a soluções subótimas e instabilidade.
3.  Pode apresentar desempenho transitório ruim, se em tempo real.
4.  Otimizações de parâmetros em tempo real caras.

### 8. Software de Sintonia e Otimização Numérica

A fraqueza da sintonia ruim ainda é prevalente na automação industrial (Allan, 2018). A maioria dos *softwares* de auto-sintonia baseia-se em ajuste de modelo de planta e no uso de **técnicas de otimização numérica**. Estimações imprecisas podem levar à degradação do desempenho de malha fechada, como aumento da variabilidade do processo e aumento do consumo de energia (Allan, 2018).

A complexidade da sintonia é evidente no espaço de busca e no número de ganhos PID para sintonizar, especialmente em sistemas MIMO (pode ser necessário sintonizar 18 a 24 parâmetros para um sistema de 6 motores).

Há uma necessidade de estruturas alternativas de sintonia para controle simplificado na categoria orientada por dados de malha fechada, **sem o custo adicional da identificação de modelo de planta demorada e da otimização numérica multiobjetivo**.

### 9. Futuro: Descrição de Sistemas Dinâmicos para Controle pela Informação do Tempo de Assentamento

Existe uma necessidade de renovado interesse na busca por **algoritmos de sintonia adaptativos automáticos**.

O artigo propõe a **Teoria de Controle de Seguimento do Modelo de Malha PID Fechada (CPLM)** (*Closed-PID Loop Model Following Control - CPLMFC*).

1.  **O CPLM:** A lei PID possui um modelo de referência de malha fechada interno e implícito (o CPLM).
2.  **Tempo de Assentamento de Malha Fechada:** O tempo de assentamento de malha fechada, em conexão com a largura de banda de baixa frequência, pode ser usado como uma **descrição suficiente da dinâmica do sistema para controle**. A identificação do tempo de assentamento se torna um **teste robusto para a capacidade máxima** (limites) de um sistema de feedback (Guo, 2020).

A principal implicação da CPLMFC é que a lei PID pode se sintonizar adaptativamente em tempo real usando o CPLM em conexão com um tempo de assentamento identificado. A vantagem é que **não requer conhecimento dos parâmetros de uma estrutura de modelo da planta** nem a **minimização explícita de uma função objetivo** para otimização. O desenvolvimento de **algoritmos robustos e automáticos para a identificação *online*** do tempo de assentamento torna-se um problema necessário a ser resolvido.

**O Tempo de Assentamento** é o intervalo de tempo de atraso finito de entrada-saída que captura a transição e é uma **propriedade característica de todos os sistemas dinâmicos controláveis e estáveis**. Ele incorpora os índices de desempenho observáveis, como a rapidez com que a saída se estabiliza e o *overshoot* máximo (Atherton, 2015). O tempo de assentamento é um superconjunto do tempo morto (*dead-time* ou *transport-lag*).

### 10. Observações Finais

O artigo forneceu uma revisão concisa da literatura sobre a sintonia de controladores PID, classificando os métodos disponíveis em baseados em modelo de planta, livres de modelo de planta e híbridos.

O artigo propôs a **identificação do tempo de assentamento de malha fechada** como um descritor de sistemas dinâmicos suficiente para substituir a identificação paramétrica de modelo de planta tradicional.

Há uma necessidade de a comunidade de controle começar a ver o PID como um **algoritmo de otimização natural**. Tentativas futuras bem-sucedidas de resolver o dilema da sintonia PID podem levar a um significativo investimento de economia de dinheiro e revolução tecnológica no campo da engenharia de controle.