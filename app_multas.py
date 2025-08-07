#Guilherme Miyamoto Bragtto RA-10736124

#cadastro
placa = input("Qual é a placa do seu carro: ")
nome = input("Qual é o seu nome?: ")
vel_max = int(input("Qual era a velocidade máxima permitida na via ? "))
vel = int(input("Qual foi a velocidade registrada ? "))
multa = str(input("Você ja foi multado alguma vez?(Sim/Não):"))
multa_pag = str(input("Deseja pagar a multa agora?(Sim/Não):"))

# Definição dos valores das multas conforme a gravidade da infração
infracao_leve = 130.16
infracao_grave = 195.23
infracao_gravissima = 880.41
calculo_infra = ((vel - vel_max) / vel_max) * 100

#cauculo da infração e penalidades
def infracao():
    if vel <= vel_max:
        print("Nenhuma infração")
    calculo_infra = ((vel - vel_max) / vel_max) * 100 #cauculo para ver o excesso de velocidade
    if calculo_infra <= 20:
        print("Infração leve - multa de R$ 130,16 e nenhum ponto na CNH.")
    elif 20 < calculo_infra and calculo_infra <= 50:
        print("Infração grave - multa de R$ 195,23 e adição de 5 pontos na CNH.")
    else:  
        print("Infração gravíssima - multa de R$ 880,41, adição de 7 pontos na CNH e suspensão imediata do direito de dirigir.")
        
            
# Função para verificar se a multa será dobrada em caso de reincidência
def verificacao(vel, vel_max, multa):
    calculo_infra = ((vel - vel_max) / vel_max) * 100 #garantir a variavel
    if multa == "Sim" and (calculo_infra >= 20 < calculo_infra <= 50 or calculo_infra >50):
        print("ATENÇÃO : O valor da multa será dobrado por reincidência ")
    else:
        print("ATENÇÃO : sem adicionais")
    
# Ver o se o usuário terá de fazer curso de reciclagem
def reciclagem(vel, vel_max):
    calculo_infra = ((vel - vel_max) / vel_max) * 100 #garantir a variavel
    if calculo_infra > 50:
        print("ATENÇÃO: Você precisa fazer um curso de reciclagem no Detran")
    else:
        print("ATENÇÃO: Sem necessidade de curso de reciclagem")

        
# Função para retornar o valor da multa conforme a gravidade da infração
# Se a infração for leve (até 20% acima do limite), retorna R$ 130,16
# Se for grave (entre 20% e 50% acima), retorna R$ 195,23
# Se for gravíssima (mais de 50% acima), retorna R$ 880,41
    
def preco(calculo_infra):
    if calculo_infra <=20:
        return infracao_leve
    elif 20 < calculo_infra and calculo_infra <= 50:
        return infracao_grave
    else:
        return infracao_gravissima
        
        
#Simulação de Pagamento da Multa
def simulacao_pagamento(calculo_infra, multa_pag):
    valor_multa = preco(calculo_infra)
    if multa_pag == "Sim":
        valor_com_desconto = valor_multa *0.8
        print(f"Você recebeu um desconto de 20%. Valor final da multa: R$ {valor_com_desconto:.2f}")
    else:
        print(f"Sem descontos. Valor total da multa: R$ {valor_multa:.2f}")
    
    
# Impressão das informações do cadastro
print("==== Informações do cadastro: ======")
print("A placa é:", placa)
print("O nome do motorista é:", nome)
print("A velocidade máxima na via era de:", vel_max)
print("A velocidade em que o carro estava era:", vel)
print("O motorista já foi multado?: ", multa)

# Chamando as funções

infracao()
verificacao(vel, vel_max, multa)
reciclagem(vel, vel_max)
simulacao_pagamento(calculo_infra, multa_pag)



