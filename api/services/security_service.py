from secrets import token_hex
import hashlib

def generateSessionToken():
    return token_hex(16)

def hashPassword(password: str):
    return hashlib.sha256(password).hexdigest()