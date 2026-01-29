print("=" * 50)
print("Практическая 5")
print("=" * 50)

# Вариант 1: Количество слов, начинающихся с буквы "е"
print("\n1. Количество слов, начинающихся с буквы 'е':")
text = input("Введите текст на русском языке: ")
words = text.split()
count_e = sum(1 for word in words if word and word[0].lower() == 'е')
print(f"Количество слов, начинающихся с 'е': {count_e}")

# Вариант 2: Замена двоеточий на % и подсчет замен
print("\n2. Замена двоеточий (:) на знак процента (%):")
text = input("Введите строку: ")
original_text = text
text = text.replace(':', '%')
replacements = original_text.count(':')
print(f"Результат: {text}")
print(f"Количество замен: {replacements}")

# Вариант 3: Удаление точек и подсчет удаленных символов
print("\n3. Удаление точек и подсчет удаленных символов:")
text = input("Введите строку: ")
original_text = text
text = text.replace('.', '')
removed_count = original_text.count('.')
print(f"Результат: {text}")
print(f"Количество удаленных точек: {removed_count}")

# Вариант 4: Замена буквы(а) на букву(о) и подсчет
print("\n4. Замена буквы 'а' на 'о':")
text = input("Введите строку: ")
original_text = text
# Замена строчных 'а' на 'о'
text = text.replace('а', 'о')
# Замена заглавных 'А' на 'О'
text = text.replace('А', 'О')
replacements = original_text.count('а') + original_text.count('А')
total_chars = len(original_text)
print(f"Результат: {text}")
print(f"Количество замен: {replacements}")
print(f"Количество символов в строке: {total_chars}")

# Вариант 5: Замена всех заглавных букв строчными
print("\n5. Замена всех заглавных букв строчными:")
text = input("Введите строку: ")
result = text.lower()
print(f"Результат: {result}")

# Вариант 6: Удаление всех букв "а" и подсчет
print("\n6. Удаление всех букв 'а' и подсчет:")
text = input("Введите строку: ")
original_text = text
# Удаляем строчные и заглавные 'а'
text = text.replace('а', '').replace('А', '')
removed_count = original_text.count('а') + original_text.count('А')
print(f"Результат: {text}")
print(f"Количество удаленных символов 'а': {removed_count}")

# Вариант 7: Замена букв "п" на * среди первых n/2 символов
print("\n7. Замена букв 'п' на * среди первых n/2 символов:")
text = input("Введите строку: ")
n = len(text)
half_n = n // 2
result = list(text)
for i in range(half_n):
    if result[i].lower() == 'п':
        result[i] = '*'
result = ''.join(result)
print(f"Длина строки: {n}")
print(f"Результат: {result}")

# Вариант 8: Подсчет слов в строке, заканчивающейся точкой
print("\n8. Подсчет слов в строке, заканчивающейся точкой:")
text = input("Введите строку, заканчивающуюся точкой: ")
if text and text[-1] == '.':
    text = text[:-1]  # Убираем точку для корректного подсчета слов
    words = text.split()
    print(f"Количество слов в строке: {len(words)}")
else:
    print("Строка не заканчивается точкой!")

# Вариант 9: Сколько раз встречается заданное слово
print("\n9. Сколько раз встречается заданное слово:")
text = input("Введите текст: ")
search_word = input("Введите слово для поиска: ")
# Разбиваем на слова и ищем точные совпадения (без учета регистра)
words = text.lower().split()
search_word = search_word.lower()
count = words.count(search_word)
print(f"Слово '{search_word}' встречается {count} раз(а)")

# Вариант 10: Каждое слово с заглавной буквы (английский)
print("\n10. Каждое слово с заглавной буквы (английский):")
text = input("Введите предложение на английском: ")
result = text.title()  # title() делает первую букву каждого слова заглавной
print(f"Результат: {result}")

# Вариант 11: Самая длинная последовательность "н" и замена ! на .
print("\n11. Самая длинная последовательность 'н' и замена ! на .:")
text = input("Введите строку: ")
# Поиск самой длинной последовательности "н"
max_n_sequence = 0
current_sequence = 0
for char in text:
    if char.lower() == 'н':
        current_sequence += 1
        max_n_sequence = max(max_n_sequence, current_sequence)
    else:
        current_sequence = 0
# Замена восклицательных знаков на точки
result = text.replace('!', '.')
print(f"Самая длинная последовательность букв 'н': {max_n_sequence}")
print(f"Результат после замены ! на .: {result}")

# Вариант 12: Слова, оканчивающиеся на букву "я"
print("\n12. Слова, оканчивающиеся на букву 'я':")
text = input("Введите строку: ")
words = text.split()
result_words = [word for word in words if word and word[-1].lower() == 'я']
print(f"Слова, оканчивающиеся на 'я': {result_words}")

# Вариант 13: Символы внутри скобок
print("\n13. Символы внутри скобок:")
text = input("Введите строку с одной парой скобок: ")
start = text.find('(')
end = text.find(')')
if start != -1 and end != -1 and start < end:
    inside = text[start + 1:end]
    print(f"Символы внутри скобок: {inside}")
else:
    print("Скобки не найдены или расположены некорректно")

# Вариант 14: Слова на "а" и на "я"
print("\n14. Слова, начинающиеся на 'а' и оканчивающиеся на 'я':")
text = input("Введите строку: ")
words = text.split()
result_words = []
for word in words:
    if word:
        first_char = word[0].lower()
        last_char = word[-1].lower()
        if first_char == 'а' and last_char == 'я':
            result_words.append(word)
print(f"Слова, начинающиеся на 'а' и оканчивающиеся на 'я': {result_words}")

# Вариант 15: Количество букв "т" в строке
print("\n15. Количество букв 'т' в строке:")
text = input("Введите текст: ")
count_t = text.lower().count('т')
print(f"Количество букв 'т' в тексте: {count_t}")
