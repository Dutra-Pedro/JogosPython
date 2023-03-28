import random


def jogar():
    print("Bem-vindo ao jogo forca")

palavra_secreta = "banana"
enforcou = False
acertou = False

while (not enforcou and not acertou):
    index = 0
    chute = input("Digite uma letra:\n")
    chute = chute.lower().strip()
    for letra in palavra_secreta:
        if (chute == letra):
            print(letra)
        else:
            print("_ \t")
        index += 1


if __name__=="__main__":
    jogar()
