#Abrir arquivo TXT

#arq = open('arq.txt', 'r') # r = read

#print(arq.read()) 

#print(arq.tell())

#print(arq.seek(0,0))

#arq = open('arq2.txt', 'w') # w = write

#arq.write('Escrevendo quaisquer coisa, e continuando escrevendo.')

#arq.close()

#arq2 = open('arq2.txt', 'r')

#print(arq2.read())

arq3 = open('arq2.txt', 'a')

arq3.write('outra frase')

arq3.close()

arq4 = open('arq2.txt', 'r')

print(arq4.read())