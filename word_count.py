#
# Escriba la función load_input que recive como parámetro un folder y retorna
# una lista de tuplas donde el primer elemento de cada tupla es el nombre del
# archivo y el segundo es una línea del archivo. La función convierte a tuplas
# todas las lineas de cada uno de los archivos. La función es genérica y debe
# leer todos los archivos de folder entregado como parámetro.
#
# Por ejemplo:
#   [
#     ('text0'.txt', 'Analytics is the discovery, inter ...'),
#     ('text0'.txt', 'in data. Especially valuable in ar...').
#     ...
#     ('text2.txt'. 'hypotheses.')
#   ]
#


import os

def load_input(input_directory):

# Lista para almacenar las tuplas
    result = []

    # Iterar sobre todos los archivos en el directorio
    for filename in os.listdir(input_directory):
        # Combinar el directorio y el nombre del archivo para obtener la ruta completa
        filepath = os.path.join(input_directory, filename)
        # Verificar si el elemento en el directorio es un archivo
        if os.path.isfile(filepath):
            # Abrir el archivo en modo lectura
            with open(filepath, 'r') as file:
                # Iterar sobre cada línea del archivo
                for line in file:
                    # Agregar una tupla con el nombre del archivo y la línea al resultado
                    result.append((filename, line.strip()))
    return result


#
# Escriba una función llamada maper que recibe una lista de tuplas de la
# función anterior y retorna una lista de tuplas (clave, valor). En este caso,
# la clave es cada palabra y el valor es 1, puesto que se está realizando un
# conteo.
#
#   [
#     ('Analytics', 1),
#     ('is', 1),
#     ...
#   ]
#

def mapper(sequence):
    nuevo = []
    for filename, line in sequence:
        # Dividir la línea en palabras
        words = line.split()
        # Iterar sobre cada palabra
        for word in words:
            # Limpiar la palabra eliminando signos de puntuación al inicio o al final
            cleaned_word = word.strip(".,!?;:'\"")
            cleaned_word = cleaned_word.lower()
            # Agregar la palabra limpiada a la lista de resultados con un valor de 1
            nuevo.append((cleaned_word, 1))
    return nuevo

#
# Escriba la función shuffle_and_sort que recibe la lista de tuplas entregada
# por el mapper, y retorna una lista con el mismo contenido ordenado por la
# clave.
#
#   [
#     ('Analytics', 1),
#     ('Analytics', 1),
#     ...
#   ]
#
def shuffle_and_sort(sequence):
    # Ordenar la lista de tuplas por la clave
    sorted_list = sorted(sequence, key=lambda x: x[0])
    return sorted_list

#
# Escriba la función reducer, la cual recibe el resultado de shuffle_and_sort y
# reduce los valores asociados a cada clave sumandolos. Como resultado, por
# ejemplo, la reducción indica cuantas veces aparece la palabra analytics en el
# texto.
#
def reducer(sequence):
    # Inicializar un diccionario para almacenar la suma de valores para cada clave
    reduced_dict = {}

    # Iterar sobre la lista ordenada
    for key, value in sequence:
        # Si la clave ya está en el diccionario, sumar el valor actual al valor existente
        if key in reduced_dict:
            reduced_dict[key] += value
        # Si la clave no está en el diccionario, agregarla con el valor actual
        else:
            reduced_dict[key] = value
    
    return reduced_dict

#
# Escriba la función create_ouptput_directory que recibe un nombre de directorio
# y lo crea. Si el directorio existe, la función falla.
#
def create_ouptput_directory(output_directory):
    """
    Crea un directorio con el nombre especificado.

    Args:
        directory_name (str): El nombre del directorio a crear.

    Raises:
        OSError: Si el directorio ya existe.
    """
    # Comprobamos si el directorio ya existe
    if os.path.exists(output_directory):
        raise OSError(f"El directorio '{output_directory}' ya existe.")
    
    # Si el directorio no existe, lo creamos
    os.makedirs(output_directory)

# Escriba la función save_output, la cual almacena en un archivo de texto llamado
# part-00000 el resultado del reducer. El archivo debe ser guardado en el
# directorio entregado como parámetro, y que se creo en el paso anterior.
# Adicionalmente, el archivo debe contener una tupla por línea, donde el primer
# elemento es la clave y el segundo el valor. Los elementos de la tupla están
# separados por un tabulador.
#

def save_output(output_directory, reducer_output):
    """
    Almacena el resultado del reducer en un archivo de texto en el directorio especificado.

    Args:
        output_directory (str): El directorio donde se guardará el archivo.
        reducer_output (dict): El resultado del reducer en forma de diccionario.
    """
    # Verificamos si el directorio de salida existe
    if not os.path.exists(output_directory):
        raise FileNotFoundError(f"El directorio '{output_directory}' no existe.")
    
    # Definimos el nombre del archivo de salida
    output_file = os.path.join(output_directory, "part-00000")
    
    # Escribimos el resultado en el archivo
    with open(output_file, 'w') as f:
        for key, value in reducer_output.items():
            f.write(f"{key}\t{value}\n")


#
# La siguiente función crea un archivo llamado _SUCCESS en el directorio
# entregado como parámetro.
#

def create_marker(output_directory):
    """
    Crea un archivo llamado _SUCCESS en el directorio especificado.

    Args:
        directory (str): El directorio donde se creará el archivo _SUCCESS.
    """
    success_file_path = os.path.join(output_directory, "_SUCCESS")
    
    # Creamos el archivo _SUCCESS
    with open(success_file_path, 'w'):
        pass  # No necesitamos escribir contenido en el archivo


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
    

def job(input_directory, output_directory):
    lineas=load_input(input_directory)
    palabras=mapper(lineas)
    palabras_ordenadas=shuffle_and_sort(palabras)
    conteo=reducer(palabras_ordenadas)
    create_ouptput_directory(output_directory)
    save_output(output_directory, conteo)
    create_marker(output_directory)


if __name__ == "__main__":
    job(
        "input",
        "output",
    )
