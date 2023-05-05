arq = open(r"arq.txt", "r")

#print(type(arq))

print(arq.read())

print(arq.seek(0,0))

print(arq.tell())