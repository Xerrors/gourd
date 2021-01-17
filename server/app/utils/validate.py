import hashlib

from app.config import SERVER_TOKEN, ADMIN_NAME


def validate_srver_token(username, password):
    return username == ADMIN_NAME and hashlib.md5(password) == hashlib.md5(SERVER_TOKEN)