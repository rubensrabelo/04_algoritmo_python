arq = open(r"C:\Users\ruben\OneDrive\Documentos\pratica\04_algoritmo_python\arq.txt", "r")

#print(type(arq))

print(arq.read())

print(arq.seek(0,0))

print(arq.tell())