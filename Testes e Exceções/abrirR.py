f = open('arquivo.txt','r')
f.write("tente escrever isso")

except:
print("Não foi possivel localizar o arquivo")

else:
print("Texto escrito com sucesso!")
f.close()