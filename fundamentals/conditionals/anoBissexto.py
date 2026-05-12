year = int(input("Digite um ano qualquer ou o atual: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"O ano de {year} é bissexto.")
elif year % 200 == 0:
    print(f"O ano {year} é bissexto.")
else:
    print(f"O ano {year} NÃO É BISSEXTO.")
