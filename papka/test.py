import re

# Попросити користувача ввести текст в декілька рядків
text = input("Введіть текст в декілька рядків:\n")

# Розділити текст на окремі рядки
lines = text.split('\n')

# Визначити, які рядки є непарними
odd_lines = [i for i in range(len(lines)) if i % 2 != 0]

# Для кожного непарного рядка видалити слово, яке містить найбільшу кількість голосних {а, е, i, ї, о, и, y, я, є, ю}
for i in odd_lines:
    words = re.findall(r'\b\w+\b', lines[i])
    max_vowels = 0
    max_vowels_word = ''
    for word in words:
        vowel_count = len(re.findall(r'[аеiїоиyяєю]', word.lower()))
        if vowel_count > max_vowels:
            max_vowels = vowel_count
            max_vowels_word = word
    if max_vowels_word:
        lines[i] = lines[i].replace(max_vowels_word, '')

# Вивести оновлений текст
print("\n".join(lines))