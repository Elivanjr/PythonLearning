nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

if nota > 7.0:
    print(f"O aluno {nome} foi aprovado com {nota} pontos.")
elif nota >= 5.0 and nota <= 6.9:
    print(
        f"O aluno {nome} não foi aprovado, mas pode fazer recuperação com sua nota, {nota}."
    )
else:
    print(f"O aluno {nome} foi reprovado com {nota} pontos.")
