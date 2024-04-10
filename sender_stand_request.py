import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body)  # inserta el cuerpo de solicitud
def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    response = post_new_user(user_body)
    return response.json()["authToken"]
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body
def post_new_client_kit(kit_body, auth_token):
    auth_token = get_new_user_token()
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
def get_existing_users():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH)