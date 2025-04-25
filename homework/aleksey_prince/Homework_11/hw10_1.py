class Book:
    material_page = "бумага"
    presence_text = True

    def __init__(self, name_book, author, count_page, isbn, reserve=False):
        self.name_book = name_book
        self.author = author
        self.count_page = count_page
        self.isbn = isbn
        self.reserve = reserve

    def __str__(self):
        reserved_info = ', зарезервирована' if self.reserve else ""
        return f"Название: {self.name_book}, Автор: {self.author}, страниц: {self.count_page}, материал: {self.material_page}{reserved_info}"


book_1 = Book('Искусство автономного тестирования с примерами на С#', 'Рой Ошероуве', 500, '100')
book_2 = Book('Fundamentals of Software Testing', 'Homes Bernard', 304, '200')
book_3 = Book('Гибкое тестирование. Практическое руководство для тестировщиков ПО и гибких команд',
              'Лайза Криспин, Джанет Грегори', 545, '300')
book_4 = Book('ATDD. Разработка программного обеспечения через приемочные тесты',
              'Маркус Гэртнер', 432, '400')
book_5 = Book('Beautiful Testing: Leading Professionals Reveal How They Improve Software',
              'Tim Riley, Adam Goucher', 666, '500', True)

for book in [book_1, book_2, book_3, book_4, book_5]:
    print(book)


class SchoolBooks(Book):
    def __init__(self, name_book, author, count_page, isbn, item, class_room, task, reserve=False):
        super().__init__(name_book, author, count_page, isbn, reserve)
        self.item = item
        self.class_room = class_room
        self.task = task

    def __str__(self):
        base_info = ', зарезервирована' if self.reserve else ""
        return f'Название: {self.name_book}, Автор: {self.author}, страниц: {self.count_page}, предмет: {self.item}, класс: {self.class_room}{base_info}'


book_6 = SchoolBooks('Алгебра 8 класс', 'Макарычев', 300, '2342422', 'Математика', 9, task=True)
book_7 = SchoolBooks('История России', 'Ракипов', 1000, '4324225', 'История', 9, task=True, reserve=True)

for books in [book_6, book_7]:
    print(books)
