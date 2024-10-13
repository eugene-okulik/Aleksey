my_dict = {'tuple': None, 'list': None, 'dict': None, 'set': None}

my_dict['tuple'] = ('Python', 'лучший', 'язык', 'программирования', 'последний элемент:)')
my_dict['list'] = [1000000, '$$$', 'США', True, {'text': 'hellow world'}]
my_dict['dict'] = {'language': 'python', 'author': 'Gvido van Rossum', 'created': '20.02.1991',
                   'developer': 'Python Software Foundation и Гвидо ван Россум[4]', 'cite': 'python.org'}
my_dict['set'] = {'15360 × 8640', '11520 × 6480', '10240 × 5760', 9393942, 'VGA'}

print(my_dict['tuple'][-1])

my_dict['list'].append('forever')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'WTF tuple??'
del my_dict['dict']['language']

my_dict['set'].add('800 x 600')
my_dict['set'].remove('VGA')

print(f'----------------\nВывод списка: \n {my_dict}')

print(my_dict['tuple'])
print(my_dict['list'])
print(my_dict['dict'])
print(my_dict['set'])
