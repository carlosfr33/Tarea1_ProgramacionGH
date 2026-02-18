def operaciones_listas(lista1, lista2):

    conjunto1 = set(lista1) #listas a conjunto
    conjunto2 = set(lista2)

    resultado = {}     #DICCIONARIO

    resultado["INTERSECCIÓN"] = conjunto1.intersection(conjunto2)

    resultado["UNIÓN"] = conjunto1.union(conjunto2)

    resultado["DIF_SIMÉTRICA"] = conjunto1 ^ (conjunto2)     # TAMBIÉN VÁLIDO CON SÍMBOLOS 

    return resultado




entrada_A = input("Introduce números para  lista A separados por espacios: ")
entrada_B = input("Introduce números para  lista B separados por espacios: ")

lista1 = []
for num in entrada_A.split():
    lista1.append(int(num))

lista2 = []
for num in entrada_B.split():
    lista2.append(int(num))

resultado = operaciones_listas(lista1, lista2)

print("Resultados:")

for clave in resultado:
    print(clave, resultado[clave])