from gui.inputs import request_date_birth,request_email,request_name,request_password,request_username

def autentication_screen():
    
    return input("1 - LOGIM\n2 - CADASTRE-SE\n -> ")

def login_screen():
    
    username = input("Username -> ")
    password = input("Password -> ")

    return {"username": username,"password":password}

def register_screen():
    while True:
        name = request_name()
        data_birth = request_date_birth()
        e_mail = request_email()
        username = request_username()
        password = request_password()
        
        break

    return {"nome":name, "e_mail":e_mail,"data_nasc":data_birth,
            "autentication":{"username":username, "password":password},
              "tarefas":[]}