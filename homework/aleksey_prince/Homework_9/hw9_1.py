import datetime

human_date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(human_date, '%b %d, %Y - %H:%M:%S')
print(python_date.month)

human_date_1 = python_date.strftime('%d.%m.%Y, %H:%M')
print(human_date_1)
