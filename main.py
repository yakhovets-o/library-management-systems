from book import Book
from library import Library
from json_storage import JSONStorage

if __name__ == '__main__':
    # Инициализация хранилища
    JSONStorage.create_json_storage()
    # создание экземпляра класса Library
    library = Library()

    book1 = Book('Преступление и наказание', 'Ф. М. Достоевский.', 1866)
    book2 = Book('Евгений Онегин', 'А. С. Пушкин', 1833)
    book3 = Book('1984', 'Джордж Оруэлл', 1949)
    book4 = Book('Портрет Дориана Грея', 'Оскар Уайльд', 1890)
    for i in [book1, book2, book3, book4]:
        library.add_book(i)
