import numpy as np

char_to_num = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
    'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
}

# Invertir la tabla de conversión
num_to_char = {v: k for k, v in char_to_num.items()}

def modular_inverse(a, modulo):
    """Calcula la inversa modular de un número"""
    for x in range(1, modulo):
        if (a * x) % modulo == 1:
            return x
    return None


def modular_inverse_matrix(T, modulo):
    """Calcula la inversa modular de una matriz"""
    det = int(round(np.linalg.det(T)))  # Determinante de T
    det_mod_inv = modular_inverse(det % modulo, modulo)  # Inversa modular del determinante

    # Matriz adjunta
    adjunta = np.round(det * np.linalg.inv(T)).astype(int) % modulo

    # Inversa modular de T
    T_inv = (det_mod_inv * adjunta) % modulo
    return T_inv

def encriptar_mensaje_vectorial(mensaje, T, b, modulo=29):
    # Completar el mensaje con espacios para que tenga longitud múltiplo de 3
    while len(mensaje) % 3 != 0:
        mensaje += ' '
    
    # Dividir el mensaje en bloques de tamaño 3
    bloques = [mensaje[i:i+3] for i in range(0, len(mensaje), 3)]
    
    # Convertir bloques a vectores columna
    bloques_vectores = [np.array([[char_to_num[char]] for char in bloque]) for bloque in bloques]
    
    # Aplicar la transformación lineal y el vector b a cada bloque
    encriptados = []
    for vector in bloques_vectores:
        resultado = (np.dot(T, vector) + b) % modulo
        encriptados.append(resultado)
    
    # Convertir los resultados encriptados a texto
    mensaje_encriptado = ''
    for vector in encriptados:
        for valor in vector.flatten():
            mensaje_encriptado += num_to_char[int(valor)]
    
    return mensaje_encriptado

def desencriptar_mensaje_vectorial(mensaje_encriptado, T, b, modulo=29):
    # Calcular la inversa modular de T
    T_inv = modular_inverse_matrix(T, modulo)
    
    # Dividir el mensaje en bloques de tamaño 3
    bloques = [mensaje_encriptado[i:i+3] for i in range(0, len(mensaje_encriptado), 3)]
    
    # Convertir bloques a vectores columna
    bloques_vectores = [np.array([[char_to_num[char]] for char in bloque]) for bloque in bloques]
    
    # Desencriptar cada bloque
    mensaje_desencriptado = ''
    for vector in bloques_vectores:
        # Restar el vector b y aplicar la transformación inversa
        resultado = np.dot(T_inv, (vector - b) % modulo) % modulo
        
        # Convertir los resultados desencriptados a texto
        for valor in resultado.flatten():
            mensaje_desencriptado += num_to_char[int(valor)]
    
    return mensaje_desencriptado

def letra_mas_repetida_y_posiciones(mensaje):
    # Crear un diccionario para contar las ocurrencias de cada letra
    conteo = {}
    for i, letra in enumerate(mensaje):
        if letra != ' ':
            if letra in conteo:
                conteo[letra].append(i)
            else:
                conteo[letra] = [i]
    
    # Encontrar la letra con más apariciones
    letra_mas_repetida = ""
    max_apariciones = 0

    for letra, posiciones in conteo.items():
        if len(posiciones) > max_apariciones:
            letra_mas_repetida = letra
            max_apariciones = len(posiciones)

    posiciones = conteo[letra_mas_repetida]
    return letra_mas_repetida, posiciones

# Parámetros
T = np.array([[2, 1, 0], [0, 1, 1], [1, 0, 1]])  # Matriz T
b = np.array([[1], [2], [3]])  # Vector constante

# Texto original
texto_original = "LA VIDA ES BELLA CUANDO UNO APRENDE A DISFRUTAR DE LAS PEQUEÑAS COSAS Y SE ENFOCA EN LO QUE REALMENTE IMPORTA"

# Encriptar el mensaje
mensaje_encriptado = encriptar_mensaje_vectorial(texto_original, T, b)
print("\nMensaje Original:", texto_original)
print("\nMensaje Encriptado:", mensaje_encriptado)

# Encontrar la letra más repetida y sus posiciones en el mensaje original
letra, posiciones = letra_mas_repetida_y_posiciones(texto_original)
print("\nLetra más repetida en el mensaje original:", letra)
print("Posiciones:", posiciones)

# Encontrar la letra más repetida y sus posiciones en el mensaje encriptado
letra, posiciones = letra_mas_repetida_y_posiciones(mensaje_encriptado)
print("\nLetra más repetida en el mensaje encriptado:", letra)
print("Posiciones:", posiciones)

# Desencriptar el mensaje
mensaje_desencriptado = desencriptar_mensaje_vectorial(mensaje_encriptado, T, b)
print("\nMensaje Desencriptado:", mensaje_desencriptado)
