import random

print ("Bem-vindo ao jogo de adivinhação")
numero_secreto = random.randrange(1,101)
tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print ("(1) Fácil (2) Médio (3) Difícil")
print("Você tem {} pontos iniciais!".format(pontos))

nivel = int(input("Define o nível: "))

if(nivel ==1):
    tentativas = 10
elif(nivel == 2):
    tentativas = 5
else:
    tentativas = 1



for rodada in range(1, tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")

    print("Você digitou ", chute_str)
    chute   = int (chute_str)

    if(chute < 1 or chute > 100):
        print ("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    if (acertou):
        print ("Você acertou e fez {} pontos!".format(pontos))
        break

    else:
        if (maior):
            print ("Você errou! O seu chute foi maior que o número secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print ("Fim do jogo! O número era {}".format(numero_secreto))
