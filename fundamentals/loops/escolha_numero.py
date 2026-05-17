import random
import os

print("- - -ADIVINHE O NÚMERO - - -")

while True:
    pcNumber = random.randrange(1, 11)
    print("Já escolhi meu número, adivinhe se for capaz.")

    myNumber = int(input("Digite um número: "))

    if myNumber != pcNumber:
        print("Tente novamnte humano lento.")
    else:
        print("FUI DERROTADO... Nãooooooooooooooo...")
        break

    os.system("sleep 3")
    os.system("clear")
