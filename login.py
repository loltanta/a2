def login():
    usario = input("ingrese su nombre: ")
    password = input("ingrese su contraseña: ")

    if ( usario== "admin" and password == "2007"):
        print(f"Ingreso exitoso y bienvenido {usario} ")
        return True
    else:
        print("usario o ocntraseña incorrecto")
        return False

    
if __name__  == "__main__":
    login()
