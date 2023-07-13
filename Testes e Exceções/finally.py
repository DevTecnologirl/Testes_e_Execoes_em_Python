def pergunta_Numero():
    numero = 1;
while True:
    try:
        val = int(input("Por favor digite um numero inteiro: "))
    except:
        print("Parece que voce nao digitou um inteiro!")
        continue
    else:
        print("Muito bem!")
        break
    finally:
        print("Tentativa numero: ",numero)
        numero=numero+1

    #print(val)
    #return
pergunta_Numero()