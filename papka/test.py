texte = "Cьоаані вранці була гаааа погода, а ввечері ні"
text = texte.lower()
text = text.split()
selected_words = [word for word in text if len(word) %2 == 1]
max_vowels = max(selected_words, key=lambda word: sum(letter in 'аеиоуюя' for letter in word))
selected_words_max_vowels = [word for word in selected_words if sum(letter in 'аеиоуюя' for letter in word) == sum(letter in 'аеиоуюя' for letter in max_vowels)]
text.remove(selected_words_max_vowels[0])
print(text)