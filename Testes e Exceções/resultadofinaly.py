numero = int(input("DIGITE UM NUMERO: "))
try:
    resultado = 30 / numero
except ZeroDivisionError:
    print("NAO FOI POSSIVEL CALCULAR!")
    resultado = 0
finally:
    print(resultado)