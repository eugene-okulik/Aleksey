# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 2

a = 'результат операции: 42'

b = 'результат операции: 514'

c = 'результат работы программы: 9'

print(int(a[a.index(':') + 2:]) + 10)
print(int(b[b.index(':') + 2:]) + 10)
print(int(c[c.index(':') + 2:]) + 10)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students_1 = ', '.join(students)
subjects_2 = ' '.join(subjects)

print(f'Students {students_1} study these subjects: {subjects_2}')
