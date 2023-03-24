import random


def jogar():
    print("Bem-vindo ao jogo de adivinhação")

    pontos = 1000
    pontos_perdidos = 0

    nivel = input("Qual o nível desejado? | F | M | D |\n")
    nivel = nivel.upper()
    num_nivel = 0
    match nivel:
        case 'F':
            num_secreto = random.randrange(1, 11)
            num_nivel = 10
        case 'M':
            num_secreto = random.randrange(1, 51)
            num_nivel = 50
        case 'D':
            num_secreto = random.randrange(1, 101)
            num_nivel = 100

    ganhou = False

    for rodada in range(0, 5):
        print(f'Rodada {rodada + 1} de 5')

        chute = input(f"Digite seu chute (1-{num_nivel}):\n")
        chute = int(chute)
        while chute <= 0 or chute > 100:
            chute = input(f"Valor inválido: Digite um número entre 1 e {num_nivel}.\n")
            chute = int(chute)
        print("Você digitou: ", chute)

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if acertou:
            print("Você acertou!")
            ganhou = True
            break
        elif maior:
            print("Você errou. Chute maior que o número secreto.\n")
            pontos_perdidos += abs(num_secreto - chute)
        elif menor:
            print("Você errou. Chute menor que o número secreto.\n")
            pontos_perdidos += abs(num_secreto - chute)

    print("Fim do jogo.")
    print(f"Pontuação final: {pontos - pontos_perdidos}")

    if not ganhou:
        print(f"O número secreto era: {num_secreto}")

if __name__ == "__main__":
    jogar()
