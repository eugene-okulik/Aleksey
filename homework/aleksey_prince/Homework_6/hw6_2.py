"""
Задание №2 - "FuzzBuzz"
Напишите программу, которая перебирает последовательность от 1 до 100.
Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.
"""

for i in range(1, 100):
    if i % 3 == 0:
        print("Fuzz")

    if i % 5 == 0:
        print("Buzz")

    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")

    else:
        print(i)