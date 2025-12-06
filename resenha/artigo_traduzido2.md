Com base nos excertos fornecidos, a seguir está a tradução completa do artigo de revisão, "Review on model predictive control: an engineering perspective" (Revisão sobre controle preditivo por modelo: uma perspectiva de engenharia).

***

## REVISÃO CRÍTICA
## Revisão sobre controle preditivo por modelo: uma perspectiva de engenharia

Max Schwenzer, Muzaffer Ay, Thomas Bergs, Dirk Abel

Recebido: 5 de Março de 2021 / Aceito: 8 de Julho de 2021
© The Author(s) 2021

### Resumo

O **Controle Preditivo Baseado em Modelo (MPC)** descreve um conjunto de métodos avançados de controle, que utilizam um **modelo de processo** para prever o comportamento futuro do sistema controlado. Ao resolver um problema de otimização (potencialmente restrito), o MPC **determina a lei de controle implicitamente**. Isso transfere o esforço de projeto do controlador para a **modelagem do processo** a ser controlado. Uma vez que tais modelos estão disponíveis em muitos campos da engenharia, a barreira inicial para a aplicação do controle é diminuída com o MPC. Sua formulação implícita mantém a compreensão física dos parâmetros do sistema, facilitando a sintonia do controlador. O Controle Preditivo Baseado em Modelo (MPC) pode controlar até mesmo sistemas que não podem ser controlados por controladores de feedback convencionais.

Com a maior parte da teoria estabelecida, é hora de um resumo conciso e uma pesquisa orientada por aplicações. Este artigo de revisão deve servir para isso. Embora no início do MPC vários artigos de revisão amplamente notados tenham sido publicados, uma visão geral abrangente sobre os desenvolvimentos mais recentes e as aplicações está ausente hoje. Este artigo revisa o estado da arte atual, incluindo teoria, evolução histórica e considerações práticas para criar uma compreensão intuitiva. Damos atenção especial às **aplicações** para demonstrar o que já é possível hoje. Além disso, fornecemos uma discussão detalhada sobre detalhes de implementação em geral e estratégias para lidar com a **carga computacional** — que ainda é um fator importante no projeto do MPC. Além dos métodos-chave no desenvolvimento do MPC, esta revisão aponta para as **tendências futuras**, enfatizando por que elas são os próximos passos lógicos no MPC.

**Palavras-chave:** Controle preditivo por modelo, MPC, Estabilidade, Robustez, Otimização, Aplicação, Computação.

***

### 1 Introdução

Para a automação de sistemas técnicos, **controladores de feedback** (também chamados de controladores de malha fechada) comparam uma referência ($\boldsymbol{r}$) com uma variável medida ($\boldsymbol{y}$), determinando um valor adequado para a variável manipulada ($\boldsymbol{u}$) com base no desvio resultante ($e = \boldsymbol{r} - \boldsymbol{y}$). Com base no princípio de funcionamento, eles podem ser divididos nas categorias: controladores clássicos, controladores preditivos e controladores repetitivos.

**Controladores clássicos**, como controladores PID, *bang-bang* ou controladores de estado, consideram apenas o comportamento passado e atual do sistema (ou seja, são "reativos" a um desvio). **Controladores preditivos** usam um modelo de sistema para prever o comportamento futuro, **antecipando desvios** da referência. **Controladores repetitivos**, por outro lado, consideram o comportamento do sistema do ciclo anterior e calculam uma trajetória ótima para o próximo ciclo.

O controlador PID é o controlador mais conhecido, com uma importância e disseminação notáveis em aplicações industriais. Embora existam várias regras de configuração, é frequentemente difícil encontrar uma parametrização, especialmente para sistemas não lineares ou variáveis no tempo. "A eficácia de qualquer projeto de feedback é fundamentalmente" limitada pela dinâmica do sistema e pela precisão do modelo.

Casos especiais, como limitações técnicas de atuadores, requerem soluções individuais que são frequentemente baseadas em heurísticas, difíceis de entender e manter.

O MPC é baseado em uma **otimização repetida em tempo real** de um modelo matemático do sistema. Com base neste modelo de sistema, o MPC prevê o comportamento futuro do sistema, considerando-o na otimização que determina a **trajetória ótima** da variável manipulada $\boldsymbol{u}$.

O comportamento antecipatório e o fato de que pode considerar **restrições duras** tornam o método tão valioso para controlar sistemas reais. Modelos estão disponíveis em quase todas as disciplinas, o que permite ao MPC utilizar esse conhecimento de longa data e economizar a formulação tediosa de uma lei de controle explícita, que geralmente é reservada para especialistas em controle. Em vez disso, o MPC determina a lei de controle automaticamente por meio de uma otimização baseada em modelo. Essa formulação implícita, a flexibilidade e o uso explícito de modelos são as principais vantagens do MPC.

Esta revisão é impulsionada pela ideia de que o MPC não permanecerá para sempre um tópico para engenheiros de controle.

### 2 Teoria

O MPC é um conjunto de métodos avançados de controle, que explicitamente usam um modelo para **prever o comportamento futuro** do sistema. Levando essa previsão em consideração, o MPC determina uma saída ótima $\boldsymbol{u}$ resolvendo um problema de otimização restrita. É um dos poucos métodos de controle que considera diretamente as **restrições**.

Muitas vezes, a função de custo é formulada de tal forma que a saída do sistema $\boldsymbol{y}$ rastreia uma dada referência $\boldsymbol{r}$ por um horizonte $N_2$. Apenas o **primeiro valor** da trajetória de saída otimizada é aplicado ao sistema. Esta predição e otimização são repetidas em cada instante de tempo. É por isso que o MPC também é referido como controle de "**horizonte recuante**" (*receding horizon*). Em essência, a ideia é que uma otimização preditiva de curto prazo alcança a otimalidade a longo prazo.

O horizonte de predição $N_2$ deve ser longo o suficiente para representar o efeito de uma mudança na variável manipulada $\boldsymbol{u}$ sobre a variável de controle $\boldsymbol{y}$. Atrasos podem ser considerados pelo horizonte de predição inferior $N_1$ ou incorporando-os ao modelo do sistema.

O MPC minimiza uma função de custo $J$ definida pelo usuário (Eq. 3), por exemplo, o erro de rastreamento entre o vetor de referência $\boldsymbol{r}$ e a saída do modelo $\boldsymbol{y}$ (Eq. 4). A formulação usa uma norma arbitrária $\lVert \cdot \rVert$.

A formulação abreviada de restrição é: $\boldsymbol{x}_{lb} \leq \boldsymbol{x}(\cdot) \leq \boldsymbol{x}_{ub}$, indicando que a sequência $\boldsymbol{x}(\cdot)$ está no conjunto viável $X_f$.

### 3 História

No final dos anos 1970, e lançaram as bases da teoria do MPC de forma independente.

 introduziu o **Controle Heurístico Preditivo por Modelo (MPHC)** em 1978, que já incluía todas as características do MPC: um modelo de processo explícito (descrito por funções de resposta ao impulso - IRFs), um horizonte recuante, restrições de entrada e saída, e uma determinação iterativa dos controles. O MPHC foi desenvolvido para a **indústria de processo** (sistemas MIMO, atrasos distintos e longos tempos de processamento).

Quase ao mesmo tempo, (da Shell Oil Company) desenvolveu o **Controle por Matriz Dinâmica (DMC)**. Eles usaram um modelo linear por partes para prever o comportamento futuro. O DMC calcula variáveis de controle **ótimas**, mas sua formulação matricial o restringe a modelos de processo lineares.

Ambos os trabalhos lançaram as bases para uma ampla e rápida disseminação do MPC na **indústria de processo petroquímica**. No início, os tempos de amostragem eram de **várias horas**. A flexibilidade na escolha da formulação do modelo foi uma das principais razões para o rápido sucesso do MPC.

Os primeiros estudos negligenciaram incertezas e instabilidades do modelo. A partir do final dos anos 1980, o foco de pesquisa mudou para a **robustez e estabilidade** do MPC. Com horizontes finitos, o problema de estimação linear podia ser formulado como um problema de programação quadrática. Devido à pressão computacional, introduziu o **"MPC explícito"**, que transfere o cálculo para otimização *a priori* massiva (Seção 8.1).

Com o aumento do poder computacional, a pesquisa mudou de grandes problemas e longos tempos de cálculo para problemas com menos variáveis de controle e requisitos de tempo computacional muito mais rápidos.

### 4 Viabilidade, estabilidade e robustez

É preciso distinguir vários aspectos do MPC:

*   **Viabilidade** do problema de otimização de malha aberta.
*   **Estabilidade** do controlador de malha fechada.
*   **Robustez** em relação às incertezas.

A robustez lida com a incerteza do modelo, sendo o modelo o elemento chave do MPC, mas nunca é perfeito.

#### 4.1 Viabilidade

**Restrições de entrada duras** ($\boldsymbol{u}$) representam limitações físicas (atuadores) que não devem ser violadas. Em contraste, **restrições de saída duras** ($\boldsymbol{y}$) são frequentemente mais desejadas do que exigidas. As restrições de saída podem tornar o problema de otimização inviável.

Para garantir a viabilidade, as restrições de saída são relaxadas (suavizadas) introduzindo **variáveis de folga ($\boldsymbol{\xi}$)** no problema de otimização. A extensão da violação é penalizada na função objetivo (Eq. 5). Todos os pacotes de *software* MPC comercial suavizam restrições de saída duras por meio de variáveis de folga.

O **Reference Governor** é uma abordagem para lidar com trajetórias desejadas inviáveis $\boldsymbol{w}$, filtrando-as para gerar uma trajetória de referência viável $\boldsymbol{r}$, ajustando a trajetória com relação ao comportamento de resposta da planta para evitar violações de restrição de entrada.

#### 4.2 Estabilidade

**Estabilidade BIBO** é a propriedade de um sistema onde uma entrada limitada resulta em uma saída limitada. Se o comportamento transitório convergir para um equilíbrio, o sistema de malha fechada é **assintoticamente estável**.

A estabilidade assintótica global é garantida para todos os sistemas LTI (Linear Invariante no Tempo) discretos com restrições de entrada duras e restrições de saída suaves se o problema de otimização for resolvido em **horizontes infinitos** ($N_2 = N_u = \infty$).

Para horizontes de predição finitos (limitados por restrições computacionais), a estabilidade é garantida se o **custo ótimo** da função objetivo do MPC for **monotonicamente decrescente** ao longo do tempo.

Uma função de **Lyapunov** ($V(\boldsymbol{x})$) é uma função escalar que é sempre positiva e não aumenta com o tempo (Eq. 6 e Eq. 7). O estado da arte para estabilidade é definir a função de custo para se comportar como uma função de Lyapunov. Isso pode ser feito introduzindo um **custo terminal** $J(k+N_2)$ ou uma **restrição de região terminal**.

A abordagem mais comum que evita a análise de Lyapunov é introduzir **restrições de contração**, garantindo que a norma (geralmente euclidiana) do vetor de estado esteja diminuindo ao longo do tempo (Eq. 8).

#### 4.3 Robustez

O MPC **não é inerentemente mais ou menos robusto** do que o controle de feedback clássico (ex: PID).

**Robustez** significa que a estabilidade é mantida e as especificações de desempenho são atendidas para uma faixa especificada de **variações do modelo (incerteza)**.

A robustez lida com a incerteza do modelo, que pode ser formulada por: intervalos de incerteza, feedback estruturado, ou usando um **conjunto de modelos** (otimizando o pior caso). Para otimizar o pior caso, utiliza-se a norma $L_\infty$. Os cálculos de robustez vêm ao **custo de desempenho** (otimalidade e computação).

A minimização do erro máximo no horizonte de predição (norma $L_\infty$) resulta em ações de controle menos extremas e orientação do processo mais suave. No entanto, o uso da norma $L_\infty$ leva a ações de controle **conservadoras**, impedindo o controlador de usar todo o potencial da planta.

Um compromisso prático para manter a otimalidade é adicionar o requisito de que a **predição no pior caso se contraia**.

#### 4.4 Resumo sobre Viabilidade, Estabilidade e Robustez

Existe uma teoria de estabilidade extensa para MPCs lineares. No entanto, problemas de otimização com restrições de entrada duras são frequentemente não lineares. A estabilidade de MPC não linear, restrito e de horizonte finito é alcançada formulando a função de custo como uma função de Lyapunov e introduzindo uma restrição de conjunto terminal. A robustez é um *trade-off* com o desempenho.

### 5 Desenvolvimentos Recentes na Teoria do MPC

O MPC foi integrado ao **Controle de Aprendizado Iterativo (ILC)** para processamento em batelada, reagindo a distúrbios dentro de um ciclo e minimizando o erro de rastreamento em múltiplos ciclos. A combinação de MPC e ILC impõe restrições ao ILC.

A **modelagem orientada por dados**, como *machine learning*, pode ser usada para o modelo de sistema no MPC, ou para aproximar o espaço de solução do MPC explícito. Em sistemas multiagentes, a **inteligência de enxame** foi utilizada para aprender a trajetória para um MPC distribuído.

### 6 Aplicações

O MPC se tornou interessante para muitas tarefas devido ao controle ótimo em presença de restrições e ao design intuitivo.

#### 6.1 Indústria de Processo

A indústria de processo utilizou o MPC quase que exclusivamente por um longo tempo. É a abordagem padrão para implementar **controle multivariável restrito** (MIMO complexos, atrasos longos).

Exemplos iniciais incluíram colunas de destilação, geradores de vapor e plantas de cloreto de polivinila (PVC). O tempo de amostragem ($T_s$) era inicialmente de **várias horas**, mas hoje em dia diminuiu para minutos e segundos.

A indústria de processo evoluiu para o uso de modelos empíricos não lineares, frequentemente linearizados (como em colunas de destilação). Redes Neurais (NN) são usadas para modelar o comportamento não linear. O MPC é usado em reatores de polietileno e misturadores agitados, demonstrando tempos de assentamento mais rápidos em comparação com o controle PI.

Em 2003, já contabilizava mais de **4.600 aplicações industriais**. A indústria de processo ainda é a principal usuária, evoluindo para processos mecânicos mais rápidos, como máquinas de papel ou **moinhos de pedra**. O MPC (DMC) foi usado em um moinho de pedra, reduzindo o consumo de energia em 66%.

#### 6.2 Eletrônica de Potência

A partir de meados dos anos 2000, surgiu uma tendência oposta. Estes são sistemas **SISO extremamente rápidos**, usando modelos puramente analíticos, com frequências de amostragem **abaixo da faixa de ms**.

Para tempos de amostragem curtos, utiliza-se o **MPC explícito** (Explicit MPC), que resolve a otimização *offline* e armazena as leis de controle em uma tabela de consulta.

O MPC é considerado ideal para o controle de motores elétricos, devido à existência de modelos analíticos lineares precisos. No controle de **conversores de potência**, que possuem um número finito de estados discretos, o MPC exige otimização de inteiros mistos (frequentemente usando força bruta).

O MPC foi aplicado para o controle direto de torque (DTC) de *drives* elétricos, visando minimizar a frequência de comutação do inversor (redução média de 16,5% em teste experimental). O MPC pode lidar nativamente com o **tempo de atraso (*dead time*)** do conversor, incorporando-o ao modelo do sistema. O MPC para conversores de potência e retificadores é um tópico de pesquisa ativo devido à sua ubiquidade e à demanda por alta eficiência.

#### 6.3 Clima e Energia de Edifícios

O MPC tem sido aplicado desde 2010. Utiliza sistemas MIMO não lineares com longos horizontes de predição, tipicamente com tempos de amostragem de minutos a 1h. O objetivo principal é **reduzir o consumo de energia** mantendo o conforto.

O sucesso deve-se à capacidade de incorporar **incertezas estatísticas** e previsões meteorológicas. O MPC para sistemas de Aquecimento, Ventilação e Ar Condicionado (HVAC) é a estratégia mais utilizada em sistemas de gerenciamento de energia de edifícios.

A modelagem requer um esforço enorme (até 70% do esforço de controle). Modelos *black box* (como Redes Neurais) são usados para modelagem. O **MPC Econômico** é usado para otimizar os custos financeiros da energia, deslocando o consumo para horas fora de pico. A descarbonização global impulsionará ainda mais as aplicações de MPC neste campo.

#### 6.4 Manufatura

Manufatura é um campo comparativamente novo para o MPC. O MPC explora **novas tarefas de controle de alto nível** (controle de processo).

Exemplos incluem **controle de força em fresagem**, controle da profundidade de penetração em soldagem e controle de pressão no molde em moldagem por injeção. Aplicações de automação com estados discretos apresentam problemas de **otimização de inteiros mistos**.

### 7 Projeto e Sintonia do Controlador

A barreira inicial para usar o MPC é relativamente pequena, desde que se tenha um modelo adequado. O esforço é transferido do projeto do controlador para a **modelagem**.

Fatores que afetam o design incluem: o modelo, a função de custo, as restrições e a escolha do solucionador (*solver*). Modelos lineares ou MPC linear são favorecidos. A **linearização sucessiva** pode ser usada para aplicar o controle linear a sistemas não lineares.

O esquema de **Real-Time Iteration (RTI)** usa a solução anterior (*warm starting*) como um bom ponto de partida para a próxima otimização, limitando o número de iterações, o que funciona bem se a frequência de amostragem for suficientemente alta.

As **variáveis de folga ($\boldsymbol{\xi}$)** suavizam as restrições, penalizando sua violação na função de custo (Eq. 11), e devem ser sintonizadas manualmente. A função de custo pode incluir a **mudança na variável manipulada ($\Delta \boldsymbol{u}$)** para um comportamento de controle suave.

Os horizontes são cruciais. O horizonte de predição ($N_2$) deve ser longo o suficiente para capturar o efeito de uma mudança em $\boldsymbol{u}$. O horizonte de manipulação ($N_u$) pode ser estimado pela diferença entre $N_2$ e o tempo de atraso $T_d$ dividido pelo tempo de amostragem $T_s$ (Eq. 12). A prática recomendada é definir o horizonte de predição inferior ($N_1$) como 1.

### 8 Computação

O esforço computacional imposto pela otimização *online* é um problema. Embora o poder computacional tenha aumentado exponencialmente (Lei de Moore), os intervalos de controle diminuíram, e o cálculo continua sendo um desafio.

#### 8.1 MPC Explícito

O **MPC Explícito (Explicit MPC)** resolve o problema de otimização *offline* para uma variedade de casos e armazena os resultados em uma tabela de consulta (*look-up table*). Isso move o esforço de computação para um cálculo *offline* não crítico em relação ao tempo, permitindo que o controle de malha fechada seja realizado em taxas mais altas.

O grande inconveniente é o aumento do esforço computacional geral (calculando todos os estados *a priori*) e a demanda por memória. Este método é limitado pela **"maldição da dimensionalidade"**.

Redes Neurais (NNs) podem ser usadas para **aproximar o espaço de solução** do MPC explícito, superando a maldição da dimensionalidade e acelerando a computação *online*.

#### 8.2 Move Blocking

A estratégia **Move Blocking** (Bloqueio de Movimento) reduz o grau de liberdade da otimização, mantendo a saída de controle constante em etapas definidas ao longo do horizonte de controle. Isso diminui a carga computacional.

A desvantagem é que a continuidade da otimização para um horizonte recuante não pode mais ser garantida, o que pode comprometer a estabilidade e a satisfação das restrições.

### 9 Conclusão

A popularidade do MPC deve-se ao fato de que, dado um modelo adequado, o controlador pode ser implementado facilmente com uma compreensão física dos parâmetros e fácil manipulação de restrições. A incorporação de restrições físicas na otimização transfere o esforço do projeto do controlador para a modelagem do sistema.

O obstáculo para o impacto duradouro do MPC na indústria é a **complexidade da modelagem e da sintonia algorítmica**. O uso de **modelagem orientada por dados** (como *machine learning*) pode ser a segunda era do MPC, diminuindo as barreiras.

O megatrend global de **descarbonização** impulsionará ainda mais as aplicações de MPC em eletrônica (componentes elétricos eficientes) e em sistemas de controle climático (HVAC). O MPC permite controlar **objetivos de alto nível** em vez de pontos de ajuste de máquinas-ferramenta.