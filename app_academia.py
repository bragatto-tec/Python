# Guilherme Miyamoto Bragatto - 10736124
import random
def cadastro():
    print("* Faça seu cadastro *")
    nome = input("Nome do exercício: ")
    tempo = int(input("Tempo gasto em minutos: "))
    calorias = int(input("Quantas calorias foram gastas: "))
    dia = input("Dia da semana:(segunda, terça, quarta, quinta, sexta, sabado ou domingo ?) ")
    exercicios = []
    exercicios.append(nome)
    exercicios.append(tempo)
    exercicios.append(calorias)
    exercicios.append(dia)
    return exercicios

def adiciona(exercicios,relatorios):
    relatorios.append(exercicios)
    

def relatorio(exercicios,relatorios):
    tempo = 0
    calorias = 0
    for exercicios in relatorios:
        if exercicios[3] == dia:
            tempo = tempo + exercicios[1]
            calorias = calorias + exercicios[2]
    else:
        return 0.0
def cal_imc():
    peso = float(input("Seu peso(kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)
    print("Seu IMC final é: {imc:.2f}")

    if imc < 18.5:
        classificacao = "Baixo peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    print(f"Classificação: {classificacao}\n")

def meta(exercicios,relatorios):
    metafinal = int(input("Qual será sua meta de calorias queimadas na semana? "))
    print("Sua meta semana é: {metafinal:.2f}")
    soma = 0.0
    for exercícios in relatorios:
        if exercicios[2] == calorias:
            soma = soma + exercicios[2]
        return soma
    else:
        return 0.0
    if metafinal < soma:
        print("Essa semana você não bateu a meta definida.")
    else:
        print("Parábens, você atingiu sua meta semanal de calorias gastas.")

        
frases = [
    "Se desafie mais um pouco, você consegue."
    "Mesmo se estiver em um dia ruim, vá la e faça."
    "Vai nessa monstro, você consegue."
    "Vá novamente, você é o melhor"
    "Hoje é mais um dia para melhor, eu confio em você."
    "OLha você, está conquistando o que desejava."
    "Pode apostar, tem pessoas que se inspiram na sua dedicação, sem desanimar."  
]
def frase():
    frase = random.choice(frases)
    print("Frase de motivação do dia: {frase}\n")

def media_calorias(exercicios, relatorios): 
    total_calorias = 0
    for exercicios in relatorios:
        total_calorias += exercicios[2]  # índice 2 = calorias
    
    media = total_calorias / len(relatorios)
    print(f"Média de calorias queimadas por exercício: {media:.2f}")

def grafico_calorias(exercicios, relatorios):
     print("\n** Gráfico de Calorias Queimadas por Exercício **")
     for exercicio in relatorios:
        nome = exercicios[0]
        calorias = exercicios[2]
        barras = calorias // 100  # cada "#" representa 100 calorias
        grafico = ""
        for i in range(barras):
            grafico = grafico + "# "
        print(nome + " " + grafico + str(calorias))


def menu():
    print("** MENU **")
    print("1. Exercícios realizados com tempo total e calorias gastas")
    print("2. Calcule seu IMC")
    print("3. Defina uma meta semanal")
    print("4. Leia uma frase motivacional")
    print("5. Sua média de calorias queimdas por exercício")
    print("6. Veja em formato de gráfico suas calorias queimadas por exercicio.")
    print("0. Sair")
    return int(input("Informe uma opção: "))

if __name__ == "__main__":
    relatorios = []
    opcao = 1
    while opcao != 0:
        opcao = menu()
        if opcao == 1:
            exercicios = cadastro()
            adiciona(exercicios,relatorios)
        elif opcao == 2:
            print(cal_imc)
        elif opcao == 3:
            meta(exercicios,relatorios)
        elif opcao == 4:
            frase()
        elif opcao == 5:
            media_calorias(exercicios, relatorios)
        elif opcao == 6:
            grafico_calorias(exercicios, relatorios)
        elif opcao < 0 or opcao > 6:
            print("Opção Inválida")    








