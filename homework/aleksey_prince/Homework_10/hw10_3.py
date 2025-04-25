# Декоратор для управления операциями
def operation_decorator(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            operation = '*'  # Это условие не будет выполнено, но для логики добавим

        return func(first, second, operation)

    return wrapper


# Функция для выполнения арифметических операций
@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second if second != 0 else 'Ошибка: деление на ноль'
    elif operation == '*':
        return first * second


# Запрос чисел у пользователя
first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

# Вызов функции calc
result = calc(first_number, second_number)
print(f"Результат: {result}")

# Прайс-лист
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# Преобразование прайс-листа в словарь
price_dict = {line.split()[0]: int(line.split()[1][:-1]) for line in PRICE_LIST.strip().split('\n')}
print(price_dict)
