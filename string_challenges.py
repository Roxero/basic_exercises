# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print('#1 Последняя буква в слове:')
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print('#2 Количество букв "a" в слове:')
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
print('#3 Количество гласный в слове:')
print(sum([int(bool(letter)) for letter in word.lower() if letter in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']]))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print('#4 Количество слов в предложении:')
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
print('#5 Выводим первую букву каждого слова:')
[print(word[0]) for word in sentence.split()]

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
print('#6 Усредненная длина слова в предложении:')
print(sum([len(word) for word in sentence.split()]) / len(sentence.split()))