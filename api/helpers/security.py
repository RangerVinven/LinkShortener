from secrets import token_hex

def generateSessionToken():
    return token_hex(16)