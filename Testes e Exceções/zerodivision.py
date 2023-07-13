a = 10
b = 0

try: 
    print(a/b)

except ZeroDivisionError as error: 
    print(error)

else:
    print('sem erros')
finally:
    print('aqui sempre vai printar')
