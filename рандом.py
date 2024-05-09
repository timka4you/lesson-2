import string

def alphabet_letters():
    for letter in sorted(string.ascii_lowercase):
        yield letter

# Приклад використання:
generator = alphabet_letters()
for _ in range(26):  # У нас є 26 букв у англійському алфавіті
    print(next(generator))