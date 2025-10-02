# 🚗 App Multas de Trânsito

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

**Sistema de cálculo e gerenciamento de multas de trânsito por excesso de velocidade desenvolvido em Python!**

</div>

---

## 📌 Sobre o Projeto

O **App Multas de Trânsito** é uma aplicação em Python desenvolvida para calcular multas de trânsito baseadas em excesso de velocidade. O sistema classifica a gravidade da infração, calcula valores de multas, verifica reincidência, aplica descontos para pagamento antecipado e identifica necessidade de curso de reciclagem no Detran.

## 🎯 Objetivo

Este projeto foi desenvolvido com os seguintes objetivos:

- 🚦 **Classificação de Infrações**: Identificar automaticamente a gravidade da infração (leve, grave ou gravíssima)
- 💰 **Cálculo Preciso**: Calcular valores de multas conforme legislação de trânsito
- 🔄 **Verificação de Reincidência**: Aplicar penalidades dobradas para reincidentes
- 📚 **Curso de Reciclagem**: Identificar quando é necessário fazer curso no Detran
- 💳 **Simulação de Pagamento**: Calcular descontos para pagamento antecipado

## ✨ Funcionalidades

### 📋 Cadastro de Infração
- Registro da placa do veículo
- Nome do condutor
- Velocidade máxima permitida na via
- Velocidade registrada pelo radar
- Histórico de multas anteriores
- Opção de pagamento imediato

### 🚨 Classificação de Infrações

O sistema classifica as infrações em três categorias conforme o percentual de excesso:

| Gravidade | Excesso | Valor da Multa | Pontos na CNH | Penalidades Adicionais |
|-----------|---------|----------------|---------------|------------------------|
| **Leve** | Até 20% | R$ 130,16 | 0 pontos | Nenhuma |
| **Grave** | 20% a 50% | R$ 195,23 | 5 pontos | - |
| **Gravíssima** | Acima de 50% | R$ 880,41 | 7 pontos | Suspensão imediata da CNH |

### 💡 Funcionalidades Especiais

- **Reincidência**: Valor da multa dobrado para infrações graves e gravíssimas em caso de reincidência
- **Desconto**: 20% de desconto para pagamento imediato da multa
- **Curso de Reciclagem**: Obrigatoriedade de curso no Detran para infrações gravíssimas
- **Cálculo Automático**: Percentual de excesso calculado automaticamente

## 🏗️ Estrutura do Código

```python
app_multas.py
├── Cadastro inicial          # Coleta de dados do motorista e infração
├── infracao()                # Classifica a gravidade da infração
├── verificacao()             # Verifica reincidência e dobra multa
├── reciclagem()              # Identifica necessidade de curso
├── preco()                   # Retorna valor da multa conforme gravidade
└── simulacao_pagamento()     # Calcula valor final com/sem desconto
```

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Conceitos Aplicados**:
  - Funções e modularização
  - Cálculos matemáticos e percentuais
  - Estruturas condicionais (if/elif/else)
  - Formatação de strings com f-strings
  - Input/Output de dados
  - Lógica booleana

## 📖 Exemplo de Uso

### Exemplo 1: Infração Leve

```
Qual é a placa do seu carro: ABC-1234
Qual é o seu nome?: João Silva
Qual era a velocidade máxima permitida na via? 60
Qual foi a velocidade registrada? 70
Você já foi multado alguma vez?(Sim/Não): Não
Deseja pagar a multa agora?(Sim/Não): Sim

==== Informações do cadastro: ======
Infração leve - multa de R$ 130,16 e nenhum ponto na CNH.
ATENÇÃO: sem adicionais
ATENÇÃO: Sem necessidade de curso de reciclagem
Você recebeu um desconto de 20%. Valor final da multa: R$ 104.13
```

### Exemplo 2: Infração Grave com Reincidência

```
Qual é a placa do seu carro: XYZ-5678
Qual é o seu nome?: Maria Santos
Qual era a velocidade máxima permitida na via? 80
Qual foi a velocidade registrada? 110
Você já foi multado alguma vez?(Sim/Não): Sim
Deseja pagar a multa agora?(Sim/Não): Não

==== Informações do cadastro: ======
Infração grave - multa de R$ 195,23 e adição de 5 pontos na CNH.
ATENÇÃO: O valor da multa será dobrado por reincidência
ATENÇÃO: Sem necessidade de curso de reciclagem
Sem descontos. Valor total da multa: R$ 195.23
```

### Exemplo 3: Infração Gravíssima

```
Qual é a placa do seu carro: DEF-9012
Qual é o seu nome?: Carlos Oliveira
Qual era a velocidade máxima permitida na via? 60
Qual foi a velocidade registrada? 120
Você já foi multado alguma vez?(Sim/Não): Não
Deseja pagar a multa agora?(Sim/Não): Sim

==== Informações do cadastro: ======
Infração gravíssima - multa de R$ 880,41, adição de 7 pontos na CNH e suspensão imediata do direito de dirigir.
ATENÇÃO: sem adicionais
ATENÇÃO: Você precisa fazer um curso de reciclagem no Detran
Você recebeu um desconto de 20%. Valor final da multa: R$ 704.33
```

## 📊 Tabela de Valores

### Multas Base (2024)

- **Infração Leve**: R$ 130,16
- **Infração Grave**: R$ 195,23
- **Infração Gravíssima**: R$ 880,41

### Descontos e Acréscimos

- **Pagamento Imediato**: 20% de desconto
- **Reincidência**: Multa dobrada (infrações graves e gravíssimas)

### Pontos na CNH

- **Infração Leve**: 0 pontos
- **Infração Grave**: 5 pontos
- **Infração Gravíssima**: 7 pontos + suspensão da CNH

## 🧮 Fórmula de Cálculo

O percentual de excesso de velocidade é calculado pela fórmula:

```
Percentual de Excesso = ((Velocidade Registrada - Velocidade Máxima) / Velocidade Máxima) × 100
```

**Exemplos:**
- Limite 60 km/h, registrado 70 km/h: `((70-60)/60) × 100 = 16,67%` → Infração Leve
- Limite 80 km/h, registrado 110 km/h: `((110-80)/80) × 100 = 37,5%` → Infração Grave
- Limite 60 km/h, registrado 120 km/h: `((120-60)/60) × 100 = 100%` → Infração Gravíssima

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar o código existente
- Atualizar valores conforme legislação vigente

## 👨‍💻 Autor

**Guilherme Miyamoto Bragatto** - RA: 10736124

- 📧 Email: guimbragatto@gmail.com
- 💼 LinkedIn: [Meu perfil](https://www.linkedin.com/in/guilherme-miyamoto-bragatto-2102b4355)
- 🐙 GitHub: [Meu usuário](https://github.com/bragatto-tec)

---

<div align="center">



*Desenvolvido com 🚗 e 🐍*


</div>
