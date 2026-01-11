def autentication_screen():
    
    return input("1 - LOGIM\n2 - CADASTRE-SE\n -> ")

def login_screen():
    
    username = input("Username -> ")
    password = input("Password -> ")

    return {"username": username,"password":password}

def register_screen():
    try:
        
        nome = input("Digite seu nome -> ")
        data_nasc = input("Digite sua data de nascimento -> ")
        e_mail = input("Digite seu e-mail -> ")
        username = input("Digite seu Username -> ")
        password = input("Digite seu Password -> ")
        lista_tarefas = []

        return {"nome":nome, "e_mail":e_mail,"data_nasc":data_nasc,
                "username":username, "password":password, "tarefas":lista_tarefas}
    
    except:
    
        return False