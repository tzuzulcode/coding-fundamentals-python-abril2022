class CredentialsException(Exception):
    pass

users = [{
    "username":"tzuzul",
    "password":"12345"
}]

username = input("Ingresa tu username: ")
password = input("Ingresa tu contraseña: ")

try:
    for user in users:
        if user["username"]!=username or user["password"]!=password:
            raise CredentialsException("Invalid credentials")

    print("Bienvenido", username)
except Exception as error:
    print("Exception: ", error.__class__.__name__)
    print("Algo salio mal: ", error)


lista = [1,2,3,4,5]

# result = sum(filter(lista))
