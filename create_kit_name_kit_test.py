import sender_stand_request
import data







# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol():
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = data.kit_body()

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert_no_firstname(kit_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert sender_stand_request.response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


# Prueba 1. kit1 creado con éxito. El parámetro name contiene 1 caracter
def test_create_kit1_1_letter_in_name_get_success_response(new_kit_body1='a'):
    var = sender_stand_request.positive_assert == data.kit_body1


# Prueba 2. kit creado con éxito. El parámetro firstName contiene 511 caracteres
def test_create_user_511_letter_in_first_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba 3. Error. El parámetro firstName contiene 1 carácter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")


# Prueba 4. Error. El parámetro firstName contiene 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")


# Prueba 5. Usuario o usuaria creada con éxito. El parámetro firstName contiene caracteres latinos
def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")


# Prueba 6. Error. El parámetro firstName contiene un string de caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")


# Prueba 7. Error. El parámetro firstName contiene un string de dígitos
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


# Prueba 8. Error. Falta el parámetro firstName en la solicitud
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)


# Prueba 9. Error. El parámetro contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    kit_body = post_kit_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)


# Prueba 10. Error. El tipo del parámetro firstName: número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    kit_body = post_kit_body(123)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400
