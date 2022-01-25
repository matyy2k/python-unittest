import random
from unittest.mock import Mock, patch


def get_code():
    rand_int = random.randint(0, 9)
    return f'CX-{rand_int}'
