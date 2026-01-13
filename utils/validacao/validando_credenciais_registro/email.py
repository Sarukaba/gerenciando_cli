import re

EMAIL_REGEX = re.compile(
    r"""
    ^
    [A-Za-z0-9._%+-]+
    @
    (?:[A-Za-z0-9-]+\.)+
    [A-Za-z]{2,}  
    $
    """,re.VERBOSE )

def validando_email(email: str) -> bool:
    return EMAIL_REGEX.fullmatch(email) is not None 
