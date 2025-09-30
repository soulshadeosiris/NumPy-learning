import numpy as np
from collections import Counter

words_list = []

while True:
    word = input("Введите блюдо (или 'stop' для завершения): ")

    if word.lower() == 'stop':
        break
    words_list.append(word)

array_1d = np.array(words_list)

counter_words = Counter(array_1d)
most_common = counter_words.most_common(1)

print(f"Ваша любимая еда: {most_common[0][0]}")
