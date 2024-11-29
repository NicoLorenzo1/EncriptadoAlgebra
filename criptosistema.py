char_to_num = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
    'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
}
def encriptar_mensaje(mensaje, a, b, modulo=29):
    
    # Tabla inversa para convertir números a caracteres
    num_to_char = {v: k for k, v in char_to_num.items()}
    
    # Convertimos el mensaje a números
    numeros = [char_to_num[char] for char in mensaje]
    
    # Aplicamos la fórmula de encriptado
    encriptados = [(a * x + b) % modulo for x in numeros]
    
    # Convertimos los números encriptados a caracteres
    mensaje_encriptado = ''.join([num_to_char[num] for num in encriptados])
    #print("Mensaje Numero encriptado:", encriptados)
    
    return mensaje_encriptado

def letra_mas_repetida(mensaje):
    diccionario = {}
    letra_mas_repetida = ""
    
    # Contar las apariciones de cada letra
    for letra in mensaje:
        if letra != " ":
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    
    for letra in diccionario:
        if letra_mas_repetida == "" or diccionario[letra] > diccionario[letra_mas_repetida]:
            letra_mas_repetida = letra

    posiciones = [i for i, l in enumerate(mensaje) if l == letra_mas_repetida]
    
    return letra_mas_repetida, posiciones


def desencriptar_mensaje(mensaje_encriptado, a, b, modulo=29):
    # Calcular el inverso multiplicativo de 'a'
    def calcular_inverso_multiplicativo(a, modulo):
        for x in range(modulo):
            if (a * x) % modulo == 1:
                return x
        raise ValueError("No tiene inverso multiplicativo")
    
    a_inverso = calcular_inverso_multiplicativo(a, modulo)
    
    num_to_char = {v: k for k, v in char_to_num.items()}
    
    # Convertir el mensaje encriptado a números
    numeros = [char_to_num[char] for char in mensaje_encriptado]
    
    # Aplicar la fórmula de desencriptado
    desencriptados = [(a_inverso * (y - b)) % modulo for y in numeros]
    
    # Convertir números desencriptados a caracteres
    mensaje_original = ''.join([num_to_char[num] for num in desencriptados])
    
    return mensaje_original

#Ejemplo de como encriptar segun el profe.
mensaje_original = "LA CULPA ES DE CATARINA"
a = 5  
b = 7
mensaje_encriptado = encriptar_mensaje(mensaje_original, a, b)
print("Mensaje Original:", mensaje_original)
print("Mensaje Encriptado:", mensaje_encriptado)

#Texto 100 caracteres
mensaje_original = "LA VIDA ES BELLA CUANDO UNO APRENDE A DISFRUTAR DE LAS PEQUEÑAS COSAS Y SE ENFOCA EN LO QUE REALMENTE IMPORTA"
a = 5  
b = 7
mensaje_encriptado = encriptar_mensaje(mensaje_original, a, b)
print("\n \nMensaje Original:", mensaje_original)
print("Mensaje Encriptado:", mensaje_encriptado)

# 4
print("\nMensaje Original:")
#letra mas repetida
letra, posiciones = letra_mas_repetida(mensaje_original)

print(f"Letra más repetida: {letra}")
print(f"Posiciones: {posiciones}")

# 5
print("\nMensaje Encreiptado:")
#letra mas repetida
letra, posiciones = letra_mas_repetida(mensaje_encriptado)

print(f"Letra más repetida: {letra}")
print(f"Posiciones: {posiciones}")

# 8
mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, a, b)
print(f"\nMensaje desencriptado: {mensaje_desencriptado}")
