import adivinhacao
import forca

print("Bem-vindo, Escolha o seu jogo")
opc = int(input("(1) - Adivinhação\n(2) - Forca\n"))

match opc:
    case 1:
        print("Abrindo adivinhação...")
        adivinhacao.jogar()
    case 2:
        print("Abrindo forca...")
        forca.jogar()
