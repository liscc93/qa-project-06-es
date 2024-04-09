import sender_stand_request
import data

def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body
def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]
# Función para las pruebas negativas
def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# 1ero El número permitido de caracteres (1) / Código de respuesta: 201
def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_1_letter
    positive_assert(kit_body, auth_token)

# 2do El número permitido de caracteres (511) / Código de respuesta: 201
def test_create_kit_511_letters_in_name_get_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_511_letters
    positive_assert(kit_body, auth_token)

# 3ro El número es menor que la cantidad permitida (0) / Código de respuesta: 400
def test_create_kit_no_letters_in_name_get_non_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_no_letters
    negative_assert_code_400(kit_body, auth_token)

# 4to El número es mayor que la cantidad permitida (512) / Código de respuesta: 400
def test_create_kit_512_letters_in_name_get_non_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_512_letters
    negative_assert_code_400(kit_body, auth_token)

# 5to Se permiten caracteres especiales (№%@',) / Código de respuesta: 201
def test_create_kit_special_character_in_name_get_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_special_character
    positive_assert(kit_body, auth_token)

# 6to Se permiten espacios (A Aaa) / Código de respuesta: 201
def test_create_kit_with_spaces_in_name_get_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_with_spaces
    positive_assert(kit_body, auth_token)

# 7to Se permiten números ("123") / Código de respuesta: 201
def test_create_kit_nums_in_name_get_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_nums
    positive_assert(kit_body, auth_token)

# 8vo El parametro no se pasa en la solicitud () / Código de respuesta: 400
def test_create_kit_no_parameters_in_name_get_non_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_no_parameters
    negative_assert_code_400(kit_body, auth_token)

# 9no El tipo de parametro es diferente (123) / Código de respuesta: 400
def test_create_kit_type_num_in_name_get_non_success_response():
    auth_token = get_new_user_token("Lis")
    kit_body = data.kit_type_num
    negative_assert_code_400(kit_body, auth_token)