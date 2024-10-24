"""
Задание №1
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте “Etiam tincidunt neque erat,
quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после этого
выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.
Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова, но уже преобразованного.
"""
import string

verse = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero."
verse_splits = verse.split()
ing = 'ing'
c = []

for verse in verse_splits:
    stripped_word = verse.rstrip(string.punctuation)
    punctuation = verse[len(stripped_word):]
    c.append(stripped_word + ing + punctuation)
result_string = ' '.join(c)
print(result_string)
