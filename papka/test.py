texte = "Cьоаані вранці була гаааа гаааа погода, а ввечері ні"
text = texte.lower()
result_words = []
for word in text.split():
    if len(word) % 2 != 0:
        result_words.append(word)
print(result_words)
max_vowel_count = 0

list = []
for word in result_words:
    vowel_count = sum(letter in 'аеиоуюя' for letter in word)
    if vowel_count > max_vowel_count:
        max_vowel_count = vowel_count
        list.append(word)

print(list)
for word in list:
    text = text.replace(word, '')
print(text)