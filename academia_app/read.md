# 💪 App Academia - Controle de Exercícios

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

**Sistema de gerenciamento e acompanhamento de exercícios físicos desenvolvido em Python!**

</div>

---

## 📌 Sobre o Projeto

O **App Academia** é uma aplicação em Python desenvolvida para ajudar praticantes de atividades físicas a registrar, monitorar e analisar seus exercícios. O sistema permite cadastrar treinos, calcular IMC, definir metas semanais, visualizar estatísticas e receber frases motivacionais para manter a consistência nos treinos.

## 🎯 Objetivo

Este projeto foi desenvolvido com os seguintes objetivos:

- 📊 **Controle de Exercícios**: Registrar exercícios com tempo e calorias gastas
- 🎯 **Definição de Metas**: Estabelecer objetivos semanais de calorias queimadas
- 📈 **Análise de Desempenho**: Visualizar estatísticas e gráficos de progresso
- 💪 **Motivação**: Receber frases inspiradoras para manter o foco
- ⚖️ **Saúde**: Calcular e acompanhar o Índice de Massa Corporal (IMC)

## ✨ Funcionalidades

### 📝 Cadastro de Exercícios
- Registro do nome do exercício
- Tempo gasto em minutos
- Calorias queimadas
- Dia da semana da atividade

### ⚖️ Calculadora de IMC
- Cálculo automático do Índice de Massa Corporal
- Classificação (Baixo peso, Peso normal, Sobrepeso, Obesidade)
- Feedback sobre a condição física atual

### 🎯 Sistema de Metas
- Definição de meta semanal de calorias
- Acompanhamento do progresso
- Verificação automática de cumprimento da meta

### 💬 Frases Motivacionais
- Biblioteca com 7 frases inspiradoras
- Seleção aleatória para motivação diária
- Incentivo para manter a consistência

### 📊 Estatísticas e Análises
- **Média de Calorias**: Calcula a média de calorias queimadas por exercício
- **Gráfico de Calorias**: Visualização em formato de barras ASCII das calorias por exercício
- **Relatório Semanal**: Acompanhamento de tempo total e calorias por dia da semana

## 🏗️ Estrutura do Código

```python
app_academia.py
├── cadastro()              # Cadastra novos exercícios
├── adiciona()              # Adiciona exercício ao relatório
├── relatorio()             # Gera relatório por dia da semana
├── cal_imc()               # Calcula IMC e classifica
├── meta()                  # Define e verifica metas semanais
├── frase()                 # Exibe frase motivacional aleatória
├── media_calorias()        # Calcula média de calorias
├── grafico_calorias()      # Exibe gráfico ASCII de calorias
└── menu()                  # Interface do menu principal
```

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Biblioteca**: `random` (para frases motivacionais aleatórias)
- **Conceitos Aplicados**:
  - Funções e modularização
  - Listas e manipulação de dados
  - Estruturas de controle (if/else, while, for)
  - Input/Output de dados
  - Formatação de strings

## 💡 Menu de Opções

Ao executar o programa, você terá acesso ao seguinte menu:

```
** MENU **
1. Exercícios realizados com tempo total e calorias gastas
2. Calcule seu IMC
3. Defina uma meta semanal
4. Leia uma frase motivacional
5. Sua média de calorias queimadas por exercício
6. Veja em formato de gráfico suas calorias queimadas por exercício
0. Sair
```

## 📖 Exemplo de Uso

### 1. Cadastrar um Exercício

```
Opção: 1
* Faça seu cadastro *
Nome do exercício: Corrida
Tempo gasto em minutos: 30
Quantas calorias foram gastas: 300
Dia da semana: segunda
```

### 2. Calcular IMC

```
Opção: 2
Seu peso(kg): 75
Altura (m): 1.75
Seu IMC final é: 24.49
Classificação: Peso normal
```

### 3. Definir Meta Semanal

```
Opção: 3
Qual será sua meta de calorias queimadas na semana? 2000
Sua meta semana é: 2000.00
Parabéns, você atingiu sua meta semanal de calorias gastas.
```

### 4. Visualizar Gráfico

```
Opção: 6
** Gráfico de Calorias Queimadas por Exercício **
Corrida # # # 300
Musculação # # # # # 500
Natação # # # # 400
```

## 📊 Estrutura de Dados

Cada exercício é armazenado como uma lista com a seguinte estrutura:

```python
exercicio = [nome, tempo, calorias, dia]
# Exemplo: ["Corrida", 30, 300, "segunda"]
```

Todos os exercícios são mantidos na lista `relatorios`.

## 🎨 Frases Motivacionais

O app possui 7 frases inspiradoras para manter você motivado:

- "Se desafie mais um pouco, você consegue."
- "Mesmo se estiver em um dia ruim, vá lá e faça."
- "Vai nessa monstro, você consegue."
- "Vá novamente, você é o melhor"
- "Hoje é mais um dia para melhor, eu confio em você."
- "Olha você, está conquistando o que desejava."
- "Pode apostar, tem pessoas que se inspiram na sua dedicação, sem desanimar."

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar o código existente
- Adicionar mais frases motivacionais


## 👨‍💻 Autor

**Guilherme Miyamoto Bragatto** - 10736124

- 📧 Email: guimbragatto@gmail.com
- 💼 LinkedIn: [Meu perfil](https://www.linkedin.com/in/guilherme-miyamoto-bragatto-2102b4355)
- 🐙 GitHub: [Meu usuário](https://github.com/bragatto-tec)

---

<div align="center">
*Desenvolvido com 💪 e 🐍 *

</div>
