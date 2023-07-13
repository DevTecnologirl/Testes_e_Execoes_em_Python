try: 
    with open("arquivo.txt",'r') as file_objetc:
        texto = file_objetc.read()
        print(texto)

except FileNotFoundError as error:
    print(error)

except:
    print('Não foi possível acessar!')