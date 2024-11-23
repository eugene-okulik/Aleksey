import random

salary = int(input('Какая у тебя ЗП: '))

bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(1000, 10000)
    total_salary = salary + random_bonus
else:
    total_salary = salary
print(f'Бонус {bonus}')
print(f'{total_salary}')
