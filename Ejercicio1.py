def procesar_lista(lista_numeros):   #FUNCIÓN
    positivos = []
    for numero in lista_numeros:
        if numero >= 0:
            positivos.append(numero)
    NO_duplicados = []
    for numero in positivos:
        if numero not in NO_duplicados:
            NO_duplicados.append(numero)
    NO_duplicados.sort()
    return NO_duplicados
#INPUT........................................................
entrada = input("Introduce números separados por espacios: ")
lista = []
for n in entrada.split():
    lista.append(int(n))
resultado = procesar_lista(lista)
print("Lista resultante:", resultado)