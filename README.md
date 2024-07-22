# 📖 Library-management-systems (LMS)

## 🍂 Описание.

* Консольное приложение для управления библиотекой книг. 
* Приложение  позволяет делать с книгами следующие действия:
    - *Добавлять*
    - *Удалять*
    - *Искать*
    - *Отображать* 
* Приложение имеет следующие  основные модули:
    - `book` 
    - `library`
    - `main`
    - `json_storage`

***

## 🦋 Модули 

###  [***`book`***](https://github.com/yakhovets-o/library-management-systems/blob/main/book.py)

*`Class Book`* -  Реализует создание книги 

Имеет следующие атрибуты:
* `title` (str): Название книги
* `author` (str): Автор книги
* `year` (int): Год издания
* `id` (int): Идентификатор книги(генерируется автоматически)
* `status` (str): Cтатус книги, по умолчанию статус(в наличии)

Методы:
* `generate_id` : Генерирует id книги сохраняя в хранилище

Пример корректного создания экземпляра:

```python
book = Book('Преступление и наказание', 'Ф. М. Достоевский.', 1866)
```

***
###  [***`library`***](https://github.com/yakhovets-o/library-management-systems/blob/main/library.py)

*`Class Library`* -  Реализует ***CRUD***

Методы:
* `add_book`: Добавляет книгу в хранилище 
    * param `book`: Объект `Book`
    * return: Если аргумент был передан верный, то функция вернет сообщение об успешном добавлении книги, либо поднимет исключение

* `get_books`: Позволяет получить все книги
    * param: Не требует
    * return: Возвращает строки книг, каждая новая книга с новой строки 

* `del_book`: Удаление книги по ее `id`
    * param `book_id`: `id` книги в строковом или числовом представлении
    * return:  Если аргумент был передан верный, то функция вернет сообщение об успешном удалении книги, либо поднимет исключение

* `change_status_book`: Смена статута у книги
    * param `book_id`: `id` книги в строковом или числовом представлении
    * param `status`: `status` книги может быть(в наличии или выдана)
    * return: строку с успешной сменой статуса либо исключение

* `search_book`: Поиск книги по поисковому ключу
    * param `search_key`: Один из `title`, `author`, `year`
    * return: В случае успешного поиска будет возвращена строка с книгой,
    либо сообщение о том что поиск завершился неудачей, либо исключение

Пример корректного создания экземпляра:
```python
library = Library()
```

***

### [***`json_storage`***](https://github.com/yakhovets-o/library-management-systems/blob/main/json_storage.py)

*`Class JSONStorage`* -  Реализует создание хранилища

Атрибуты:
* `file_path` (str): Путь к хранилищу

Методы:
* `create_json_storage`: Создает хранилище для хранения книг

Пример инициализации класса:
```python 
JSONStorage.create_json_storage() 
```

***

### [***`main`***](https://github.com/yakhovets-o/library-management-systems/blob/main/main.py)

#### точка входа в приложение

***Пример***:
```python
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
```

* `JSONStorage.create_json_storage()` - Должнен быть проиниализирован в первую очередь, он создает хранилище 
* `library = Library()`-  Должнен быть проиниализирован для корректной работы с хранилищем 
 * После операций выше возможны ***CRUD*** операции с книгами 

***

### [***`library.json`***](https://github.com/yakhovets-o/library-management-systems/blob/main/library.json)

#### Хранилище

#### Структура

![Structure](https://github.com/yakhovets-o/library-management-systems/blob/main/structure.png)

***
## 🖥️ Установка
#### Для Windows
* Скопируйте репозиторий к себе на компьютер [***library-management-systems***]([https://github.com/yakhovets-o/library-management-systems](https://github.com/yakhovets-o/library-management-systems))
* Установите виртуальное окружение  ```python -m venv venv```
* Активируйте виртуальное окружение ```venv/Scripts/activate```
