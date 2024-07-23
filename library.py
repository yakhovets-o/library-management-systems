import json

from typing import NoReturn

from json_storage import JSONStorage
from book import Book


class Library(JSONStorage):
    """
    Класс реализует CRUD
    Methods:
        add_book: Добавление книги
        get_books: Получение всех книг
        del_book: Удаление книги по id
        change_status_book: Смена статуса у книги
        search_book: Поиск книги по поисковому ключу
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Создает или возвращает единственный экземпляр класса
        _instance: Единственный экземпляр класса
        :param args:
        :param kwargs:
        :return: Singleton
        """
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def add_book(self, book: Book) -> str | NoReturn:
        """
        Метод реализует добавление книги в хранилище
        :param book: объект Книги
        :return: Если аргумент был передан верный,
        то функция вернет сообщение об успешной добавлении книги, либо поднимет исключение
        """
        add_book = {book.id: {'title': book.title, 'author': book.author, 'year': book.year,
                              'status': book.status}}

        try:
            with open(self.file_path, mode='r+') as library:
                books = json.load(library)

                books['library']['books'].update(add_book)

                library.seek(0)
                json.dump(books, library, ensure_ascii=False, indent=4)
                return 'The book has been added to the repository'
        except json.JSONDecodeError as e:
            raise f'Decoding error JSON: {e}'
        except Exception as e:
            raise Exception(f'Another mistake: {e}')

    def get_books(self) -> str:
        """
        Метод реализует возврат всех книг из хранилища
        :return: Все книги
        """
        with open(self.file_path, 'r') as file:
            books = json.load(file)['library']['books']

        return '\n'.join([f'{k} {" ".join(map(str, v.values()))}' for k, v in books.items()])

    def del_book(self, book_id: int | str) -> str | NoReturn:
        """
        Метод реализует удаление книги по id
        :param book_id: id книги в строковом или числовом представлении
        :return: Если аргумент был передан верный,
        то функция вернет сообщение об успешном удалении книги, либо поднимет исключение
        """
        try:
            with open(self.file_path, mode='r+') as library:
                library.seek(0)
                books = json.load(library)

                del books['library']['books'][str(book_id)]

                library.seek(0)
                library.truncate()
                json.dump(books, library, ensure_ascii=False, indent=4)
                return f'The book with {book_id} has been deleted'
        except json.JSONDecodeError as e:
            raise f'Decoding error JSON: {e}'
        except KeyError as e:
            raise KeyError(e)
        except Exception as e:
            raise Exception(f'Another mistake: {e}')

    def change_status_book(self, book_id: str | int, status: str) -> str | NoReturn:
        """
        Метод реализует смену статута у книги
        :param book_id: id книги в строковом или числовом представлении
        :param status: status книги может быть в наличии или выдана
        :return: строку с успешной сменой статуса либо исключение
        """
        if status not in ('в наличии', 'выдана'):
            raise ValueError('The status can only be: в наличии или выдана')
        try:
            with open(self.file_path, mode='r+') as library:
                library.seek(0)
                books = json.load(library)
                books['library']['books'][str(book_id)]['status'] = status

                library.seek(0)
                library.truncate()
                json.dump(books, library, ensure_ascii=False, indent=4)
                return 'The status has been successfully changed'

        except json.JSONDecodeError as e:
            raise f'Decoding error JSON: {e}'
        except KeyError as e:
            raise KeyError(e)
        except Exception as e:
            raise Exception(f'Another mistake: {e}')

    def search_book(self, search_key: str | int) -> str | NoReturn:
        """
        Метод реализует поиск книги по поисковому ключу
        ключом может быть:
        - Название книги
        - Автор книги
        - Год издания
        :param search_key:
        :return:
        В случае успешного поиска будет возвращена строка с книгой
        либо сообщение о том что поиск завершился неудачей
        либо исключение
        """
        try:
            with open(self.file_path, 'r') as file:
                books = json.load(file)['library']['books']
        except json.JSONDecodeError as e:
            raise f'Decoding error JSON: {e}'
        except KeyError as e:
            raise KeyError(e)
        result = '\n'.join(
            [f'{k} {" ".join(map(str, v.values()))}' for k, v in books.items() if
             search_key in v.values()]) or 'No books were found according to your request'

        return result
