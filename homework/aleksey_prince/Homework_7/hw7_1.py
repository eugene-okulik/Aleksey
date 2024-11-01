pin_code = 9999

what_pin_code = int(input('Отгадай цифры пинкода: '))
while what_pin_code != pin_code:
    print('Попробуй снова')
    what_pin_code = int(input('Отгадай цифры пинкода: '))
print('“Поздравляю! Вы угадали!”')
