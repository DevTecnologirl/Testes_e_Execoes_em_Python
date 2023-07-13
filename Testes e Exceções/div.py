try: 
    n1 = float(input("Insira um número: "))
    n2 = float(input("Insira outro número: "))

    resultado = n1 / n2 

    print("Resultado: {:.2f}".format(resultado))
except ValueError:
    print("Isso não é um numero!")
except ZeroDivisionError:
    print("Divisao por 0 inderteminada")
except:
    print("Algo deu errado")