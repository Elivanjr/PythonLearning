num1 = int(input("Valor 1: "))
num2 = int(input("Valor 2: "))
sinal = input("Sinal: ")

match sinal:
    case "+":
        print(f"Soma dos dois números: {num1 + num2}")
    case "-":
        print(f"Diferença dos dois números: {num1 - num2}")
    case "*":
        print(f"Produto dos dois números: {num1 * num2}")
    case "/":
        print(f"Quociente dos dois números: {num1 / num2}")
    case "**":
        print(f"Potencia dos dois números: {num1**num2}")
