import json

from typing import NoReturn

from json_storage import JSONStorage


class BookDescriptor:
    """Дескриптор данных"""

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Book(JSONStorage):
    """
    Класс для представления книги
    Attributes:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания
    Methods:
        generate_id: Генерирует id книги сохраняя в хранилище
    """
    title = BookDescriptor()
    author = BookDescriptor()
    year = BookDescriptor()

    def __init__(self, title: str, author: str, year: int) -> None:
        """
         Инициализация данных.
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания
        :param __id: Генерация id
        :param __status: Установка статуса для книги (по умолчанию: в наличии)
        """
        self.__id = self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.__status = 'в наличии'

    @property
    def id(self) -> int:
        """
        Объект свойство
        уникальный идентификатор, генерируется автоматически
        :return: id книги
        :rtype: int
        """
        return self.__id

    @property
    def status(self) -> str:
        """
        Объект свойство
        Cтатус  по умолчанию: в наличии
        :return: status книги
        :rtype: str
        """
        return self.__status

    def generate_id(self) -> int | NoReturn:
        """
        Автоматическая генерация id книги путем:
        - Десериализации данных
        - Увеличение id на единицу
        - Сериализации данных
        дает гарантии что после перезагрузки id не будет обнулен
        file_path = адрес файла
        :return: id | NoReturn
        """

        try:
            with open(self.file_path, mode='r+') as library:
                books = json.load(library)

                books['library']['last_id'] += 1
                new_last_id = books['library']['last_id']
                library.seek(0)

                json.dump(books, library, ensure_ascii=False, indent=4)
                return new_last_id
        except json.JSONDecodeError as e:
            raise f'Decoding error JSON: {e}'
        except Exception as e:
            raise Exception(f'Another mistake: {e}')

    def __repr__(self) -> str:
        """Строковое представление объекта"""
        return f'{self.__class__.__name__}: {self.id=}, {self.title=}, {self.author=}, {self.year=}, {self.status=}'

    def __setattr__(self, key, value) -> None | NoReturn:
        """
        Метод для установки значения атрибута объекта
        :param key: Имя атрибута
        :param value: Значение для установки
        :return: None | NoReturn
        """
        if key in ('title', 'author') and not isinstance(value, str):
            raise TypeError('Invalid type of assigned data.')
        if key == 'year' and type(value) is not int:
            raise TypeError('Invalid type of assigned data.')
        if key == 'year' and isinstance(value, int) and value < 1:
            raise ValueError('The year cannot be a negative value.')

        super().__setattr__(key, value)
