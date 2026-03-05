#--------Coleções em python---------
lista = ["Senai", True, 22, 3.5]
print(lista)
print(type(lista))#Tipo da coleção
print(lista[1])#Acessa o indice numero 1
print(len(lista))#Tamanho da lista
del lista[2]
print(lista)
lista.insert(2, "SENAI")
lista.append("Eduane")
lista.append("Senai")

#--------------Tupla----------------
tupla = ( "Senai", False, 24, 1.73)
print(tupla)
print(type(tupla))
print(tupla[3])


#---------Dicionário----------
dicionario = {"nome": "Senai", "logica": True, "numero":2, "n":2.75}
print(dicionario)
print(type(dicionario))
print(dicionario["nome"])
dicionario.update({"novo": "SENAI"})
del dicionario["nome"]

for chave in dicionario.keys:
    print(chave, "->", dicionario[chave])


#----------Conjunto-----------
conjunto = {"Senai", True, 10, 2.1}
print(conjunto)
print(type(conjunto))
print(conjunto[1])
conjunto.remove(1)
conjunto.update("Clodoaldo")
conjunto.discard(2)
