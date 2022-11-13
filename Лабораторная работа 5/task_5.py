import string
from random import sample

n = 8
def get_random_password() -> str:
    alfa = f'{string.digits}{string.ascii_lowercase}{string.ascii_uppercase}'
    passwords = sample(alfa, k=8, counts=None)
    return ''.join(passwords)


print(get_random_password())
