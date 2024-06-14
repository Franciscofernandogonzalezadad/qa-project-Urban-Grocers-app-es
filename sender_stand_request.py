import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         # Concatenación de URL base y ruta.
                         json=products_ids,  # Datos a enviar en la solicitud.
                         headers=data.headers)  # Encabezados de solicitud.


# Función para cambiar el valor del parámetro Name en el cuerpo de la solicitud
def post_kit_body1():
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body1.copy()
    # Se cambia el valor del parámetro firstName
    current_body = 'kit_body1'
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body


# Función de prueba positiva
def positive_assert(kit_body1):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = post_kit_body1()

    # El resultado de la solicitud para crear un nuevo kit  se guarda en la variable response


response = post_new_kit(data.kit_body1)
# Comprueba si el código de estado es 201
assert response.status_code == 201
# Comprueba que el campo authToken está en la respuesta y contiene un valor
assert response.json()["authToken"] != ""


# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def post_kit_body2():
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body2.copy()
    # Se cambia el valor del parámetro firstName
    current_body = 'kit_body2'
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body


# Función de prueba positiva
def positive_assert():
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = post_kit_body2()

    # El resultado de la solicitud para crear un nuevo kit  se guarda en la variable response


response = post_new_kit(data.kit_body2)
# Comprueba si el código de estado es 201
assert response.status_code == 201
# Comprueba que el campo authToken está en la respuesta y contiene un valor
assert response.json()["authToken"] != ""
