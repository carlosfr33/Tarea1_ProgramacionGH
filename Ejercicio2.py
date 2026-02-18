import string

def contar_palabras(lista_palabras, ruta_texto):
    cuenta = {}
    for palabra in lista_palabras:
        cuenta[palabra] = 0

    archivo = open(ruta_texto, "r")
    texto = archivo.read()
    archivo.close()

    texto = texto.lower()

    for signo in string.punctuation:
        texto = texto.replace(signo, " ")
    palabras = texto.split()

    
    for palabra in palabras:
        if palabra in cuenta:
            cuenta[palabra] = cuenta[palabra] + 1
    return cuenta

texto_usuario = input("Escribe palabras a buscar (separadas por espacio): ")
lista_palabras = texto_usuario.lower().split()

ruta_texto = input("Inserta la ruta del archivo de texto: ")

resultado = contar_palabras(lista_palabras, ruta_texto)

print("FILTRADO:")
for palabra in resultado:
    print(palabra, "=", resultado[palabra])
