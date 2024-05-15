import requests
from bs4 import BeautifulSoup


def get_book_titles(url):
    # Відправляємо GET-запит на вказаний URL
    response = requests.get(url)

    # Перевіряємо, чи отримали ми успішний відгук
    if response.status_code == 200:
        # Створюємо об'єкт BeautifulSoup для парсингу HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Знаходимо всі елементи <h3>, які містять назви книг
        book_titles = soup.find_all('h3')

        # Витягуємо текст назв книг та зберігаємо їх у список
        titles = [title.text.strip() for title in book_titles]

        return titles
    else:
        print("Не вдалося отримати доступ до сторінки")
        return None


# URL адреса сторінки зі списком книг
url = "http://books.toscrape.com"

# Витягуємо назви книг за допомогою функції get_book_titles
book_titles = get_book_titles(url)

# Виводимо назви книг, якщо вони були успішно отримані
if book_titles:
    for title in book_titles:
        print(title)

