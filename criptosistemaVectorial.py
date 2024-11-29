import numpy as np

char_to_num = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
    'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
}

# Invertir la tabla de conversión para convertir números a caracteres
num_to_char = {v: k for k, v in char_to_num.items()}


def encriptar_mensaje_vectorial(mensaje, T, b, modulo=29):
    
    # Tabla inversa para convertir números a caracteres
    num_to_char = {v: k for k, v in char_to_num.items()}
    
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


def desencriptar_mensaje_vectorial(mensaje_encriptado, T, b, modulo=29):
    # Invertir la matriz T
    T_inv = np.linalg.inv(T)  # Matriz inversa de T
    T_inv = np.round(T_inv).astype(int)  # Asegurarse de que los valores sean enteros
    
    # Completar el mensaje encriptado con espacios para que tenga longitud múltiplo de 3
    while len(mensaje_encriptado) % 3 != 0:
        mensaje_encriptado += ' '
    
    # Dividir el mensaje en bloques de tamaño 3
    bloques = [mensaje_encriptado[i:i+3] for i in range(0, len(mensaje_encriptado), 3)]
    
    # Convertir bloques a vectores columna
    bloques_vectores = [np.array([[char_to_num[char]] for char in bloque]) for bloque in bloques]
    
    # Desencriptar cada bloque
    mensaje_desencriptado = ''
    for vector in bloques_vectores:
        # Restar el vector b y aplicar la transformación inversa
        resultado = (np.dot(T_inv, vector - b) % modulo)
        
        # Convertir los resultados desencriptados a texto
        for valor in resultado.flatten():
            valor_mod = int(valor) % 29  # Asegura que esté en el rango 0-28
            mensaje_desencriptado += num_to_char[valor_mod]
    
    return mensaje_desencriptado



T = np.array([[2, 1, 0], [0, 1, 1], [1, 0, 1]])  # Matriz T con determinante 1
b = np.array([[1], [2], [3]])  # Vector constante

# Texto original
texto_original = "LA VIDA ES BELLA CUANDO UNO APRENDE A DISFRUTAR DE LAS PEQUEÑAS COSAS Y SE ENFOCA EN LO QUE REALMENTE IMPORTA"

# Encriptar el mensaje
mensaje_encriptado = encriptar_mensaje_vectorial(texto_original, T, b)
print("\n Mensaje Original:", texto_original)
print("\n Mensaje Encriptado:", mensaje_encriptado)


# Llamada a la función
letra, posiciones = letra_mas_repetida_y_posiciones(texto_original)

print("\n Letra más repetida:", letra)
print("Posiciones:", posiciones)

# Llamada a la función
letra, posiciones = letra_mas_repetida_y_posiciones(mensaje_encriptado)

print("\n Letra más repetida:", letra)
print("Posiciones:", posiciones)


# Desencriptar el mensaje
mensaje_desencriptado = desencriptar_mensaje_vectorial(mensaje_encriptado, T, b)

print("Mensaje Encriptado:", mensaje_encriptado)
print("Mensaje Desencriptado:", mensaje_desencriptado)