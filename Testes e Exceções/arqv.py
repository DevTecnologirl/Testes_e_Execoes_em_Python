f = open('arquivo.txt','r')

except IOError:
print("Não foi possivel localizar o arquivo")

else: 
print("Texto escrito com sucesso!")
f.close()