import json
PATH_JSON = "storage/registered_users.json"
def register_user(dados: dict):
    user_registration_data = dados

    with open(PATH_JSON,"r",encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)
    
    conteudo.append(user_registration_data)

    with open(PATH_JSON,"w",encoding="utf-8") as arquivo:
        json.dump(conteudo,arquivo,indent=4)   

    return "Usuario cadastrado."

def log_in_user(username: str ,password: str):
    with open(PATH_JSON,"r",encoding="utf-8") as arquivo:
        arquivo = json.load(arquivo)

        contador = 0

        while contador < len(arquivo):
            register = arquivo[contador]
            for key in register.keys():
                if key == "autentication":
                    if register[key]["username"] == username and register[key]["password"] == password:
                        return True
                    
            contador += 1       
        return False
    pass