# Respostas sobre Machine Learning

## 1. O que é Machine Learning

Machine Learning é um campo que permite que os computadores aprendam a partir dos padrões dos dados que são passados como treinamento.

## 2. Conceito de Conjunto de Treinamento, Conjunto de Validação e Conjunto de Teste

- **Conjunto de treinamento:** É um subconjunto de dados utilizado para realizar o aprendizado do algoritmo.

- **Conjunto de validação:** É um subconjunto de dados utilizado para validar o modelo.

- **Conjunto de teste:** É um subconjunto de dados utilizado para verificar o desempenho do modelo, utilizando informações novas.

## 3. Como lidar com dados ausentes em um conjunto de dados de treinamento

- Realizando a remoção de linhas ou colunas com dados ausentes.
- Usando modelos como KNN ou regressão para estimar valores ausentes.
- Preenchendo com um valor especial como "desconhecido" ou -999, para destacar a ausência.
- Preenchendo com a média, mediana (para dados numéricos) ou moda (para dados categóricos).
- Adicionando uma coluna binária indicando se o dado estava ausente (útil quando a ausência é informativa).
- Utilizando modelos como XGBoost ou Random Forest, que lidam bem com dados ausentes.

## 4. O que é uma Matriz de Confusão e como ela é usada para avaliar o desempenho de um modelo preditivo

Uma matriz de confusão é uma tabela que permite visualizar o desempenho de um modelo de classificação, exibindo:

- Verdadeiros Positivos (VP)
- Falsos Positivos (FP)
- Verdadeiros Negativos (VN)
- Falsos Negativos (FN)

A partir dela, é possível calcular métricas como Acurácia, Precisão, Recall e F1-Score, ajudando a entender melhor como o modelo está se comportando.

## 5. Áreas interessantes para aplicar Machine Learning

Uma das áreas que acho mais interessante é a **construção civil**. Em um projeto recente que tive a oportunidade de conhecer, foi criada uma inteligência artificial para verificar se os profissionais estavam utilizando corretamente os EPIs (Equipamentos de Proteção Individual), de forma a evitar acidentes graves nas obras.
