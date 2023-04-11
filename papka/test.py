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
result_wordses = [result_words,result_words2,result_words3]
list = []
list2 = []
list3 = []
lse = [list,list2,list3]
def suma(result):
    max_vowel_count = 0
    for word in result:
        if result == result_words:
            vowel_count = sum(letter in 'аеиоуюя' for letter in word)
            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count
                list.append(word)
        elif result == result_words2:
            vowel_count = sum(letter in 'аеиоуюя' for letter in word)
            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count
                list2.append(word)
        elif result == result_words3:
            vowel_count = sum(letter in 'аеиоуюя' for letter in word)
            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count
                list3.append(word)

for i in range(len(result_wordses)):
    suma(result_wordses[i])
print(f"Слова з найбільшою кількістю голосних з \nпершого речення: {list}\n"
      f"Другого: {list2}\n"
      f"Третього: {list3}")

def dellate(ls):
    global texte, texte2,texte3
    for word in ls:
        if ls == list:
            texte = texte.replace(word, '')
        elif ls == list2:
            texte2 = texte2.replace(word, '')
        elif ls == list3:
            texte3 = texte3.replace(word, '')


for i in range(len(lse)):
    dellate(lse[i])
print(f"{texte}\n{texte2}\n{texte3}")
