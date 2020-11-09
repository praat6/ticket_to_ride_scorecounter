from random import randint


def generate():
    first_number = randint(10, 99)
    second_number = randint(10, 99)
    return '{}-{}'.format(first_number, second_number)
