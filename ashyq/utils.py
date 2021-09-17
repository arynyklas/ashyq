from string import ascii_uppercase, ascii_lowercase, digits
from random import choice


_chars = ascii_uppercase + ascii_lowercase + digits


def random_string(length: int) -> str:
    return ''.join(choice(_chars) for _ in range(length))
