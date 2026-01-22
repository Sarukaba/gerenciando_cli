from utils.validacao.registro import name_valid,email_valid,data_birth_valida

def request_name() -> str:
    while True:
        nome = input("Digite seu nome -> ").title()
        
        if name_valid(nome):
            return nome
        
        print("nome invalido, Use apenas letras e espaços.")
        continue

def request_date_birth() -> str:
    while True:
        data_birth = input("Digite sua data de nascimento(OBS:apenas numeros) -> ")
        data_birth = data_birth_valida(data_birth)
        
        if data_birth:
            return data_birth
        
        print('Insira apenas numeros referente a data')
        continue

def request_email() -> str:
    while True:
        email = input("Insira o seu e-mail: ").lower()
        
        if email_valid(email):
            return email

        print("Email invalido")
        continue

def request_username() -> str:
    username = input("digite seu username: ")

def request_password() -> str:
    pass