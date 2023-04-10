texte = "Cьоаані вранці була гаааа гаааа погода, а ввечері ні"
texte2 = "Київ це столиця України"
texte3 = "Куріння шкодить вашому здоровю"
texte = texte.lower()
texte2 = texte2.lower()
texte3 = texte3.lower()
textlist = [texte,texte2,texte3]
result_words = []
result_words2 = []
result_words3 = []
def neparno(text):
    for word in text.split():
        if text == texte:
            if len(word) % 2 != 0:
                result_words.append(word)
        elif text == texte2:
            if len(word) % 2 != 0:
                result_words2.append(word)
        elif text == texte3:
            if len(word) % 2 != 0:
                result_words3.append(word)

for i in range(len(textlist)):
    neparno(textlist[i])
print(f"З першого рядка: {result_words}\n Другого: {result_words2}\n"
          f"Третього: {result_words3}")
"""
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
"""
