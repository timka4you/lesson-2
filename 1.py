def login(username, password):
    # Перевірка правильності ім'я користувача та пароля за допомогою оператора assert
    assert username == "admin" and password == "admin123", "Невірне ім'я користувача або пароль"
    print("Вхід виконано успішно")

# Запит на введення ім'я користувача та пароля
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

# Виклик функції login з введеними даними
login(username, password)



