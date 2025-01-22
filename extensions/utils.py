import random


def generate_random_number(len=9):
    if len < 1:
        raise ValueError('طول عدد باید بزرگتر از صفر باشد')
    return random.randint(10**(len-1), 10**len - 1)
