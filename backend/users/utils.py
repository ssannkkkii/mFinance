import random

def generate_card_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])

def generate_cvv():
    return ''.join([str(random.randint(0, 9)) for _ in range(3)])