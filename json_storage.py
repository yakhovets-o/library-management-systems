import os
import json


class JSONStorage:
    """Класс для создания хранилища
    Attributes:
        file_path (str):
    Methods:
        __create_json_storage : Создает хранилище для хранения книг"""

    file_path = 'library.json'

    @classmethod
    def create_json_storage(cls) -> None:
        """
        Создает хранилище
        :return: None
        """
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, mode='w') as library:
                books = {'library': {'last_id': 0, 'books': {}}}
                json.dump(books, library, ensure_ascii=False, indent=4)
