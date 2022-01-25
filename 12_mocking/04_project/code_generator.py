import random
from unittest.mock import Mock, patch
from datetime import date


def get_code():
    rand_int = random.randint(0, 9)
    return f'CX-{rand_int}'


def get_today_name():
    return date.today().strftime('%a')


def get_code_with_day():
    code = get_code()
    day_name = get_today_name().upper()
    return f'{code}-{day_name}'
