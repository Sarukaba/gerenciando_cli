import re

EMAIL_STANDARD = re.compile(
    r"""
    ^
    [A-Za-z0-9._%+-]+
    @
    (?:[A-Za-z0-9-]+\.)+
    [A-Za-z]{2,}  
    $
    """,re.VERBOSE )

NAME_STANDARD = re.compile(r'^[^0-9._$@#%!&*()=-]+$')

DATA_STANDARD = r"^\d{2}\d{2}\d{4}$"

USERNAME_STANDARD = r"^[a-zA-Z0-9_]{3,15}$"

def email_valid(email: str) -> bool:
    return EMAIL_STANDARD.fullmatch(email) is not None 

def name_valid(nome: str) -> bool:
    return NAME_STANDARD.fullmatch(nome) is not None

def data_birth_valida(data: str) -> str:
    if not re.match(DATA_STANDARD,data):
        return False
    
    try:
        data_birth_formatted = f"{data[0:2]}/{data[2:4]}/{data[4:]}"
        return data_birth_formatted
    
    except ValueError:
        return False

#Validar: formato, tamanho, caracteres permitidos, unicidade e palavras proibidas.    
def username_valid_format(username) -> bool:
    if not re.match(USERNAME_STANDARD, username):
        return False

def username_available(username):
    pass

def username_prohibited(username):
    pass

def username_valid(username):
    pass