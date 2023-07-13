x = float(input("Digite o numero x: "))
y = float(input("Digite o numero y: "))

try:
    print("{:.2f}".format(x/y))
except ZeroDivisionError:
    print("ERRO! Divisão por 0 NÃO permitida!")