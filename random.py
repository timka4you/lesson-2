import random
import string

def random_alphabet_generator():
    while True:
        yield random.choice(string.ascii_lowercase)

# Приклад використання:
generator = random_alphabet_generator()
for _ in range(10):  # Генеруємо 10 випадкових букв
    print(next(generator))
