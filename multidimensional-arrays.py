import numpy as np
# EN: Importing NumPy library
# RU: Импортируем библиотеку NumPy

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
# EN: 3D array (3x3x3) of letters
# RU: 3D массив (3x3x3) с буквами

print(array.ndim)
# EN: Number of dimensions → 3
# RU: Количество измерений → 3

print(array.shape)
# EN: Shape of the array → (3, 3, 3)
# RU: Форма массива → (3, 3, 3)

print(array[1, 1, 1])
# EN: Accessing one element: block 1, row 1, element 1 → 'N'
# RU: Доступ к элементу: блок 1, ряд 1, элемент 1 → 'N'

# How to read indices to pick letters:
# EN: array[x, y, z] → x = block, y = row, z = element
# RU: array[x, y, z] → x = блок, y = ряд, z = элемент
#
# Visual example:
# Block 0 (x=0)         Block 1 (x=1)         Block 2 (x=2)
# [['A','B','C'],        [['J','K','L'],        [['S','T','U'],
#  ['D','E','F'],         ['M','N','O'],         ['V','W','X'],
#  ['G','H','I']]         ['P','Q','R']]         ['Y','Z',' ']]
#
# Examples:
# array[0,0,1] → 'B' (Block 0 → Row 0 → Element 1)
# array[2,2,0] → 'Y' (Block 2 → Row 2 → Element 0)
# array[0,1,1] → 'E' (Block 0 → Row 1 → Element 1)

word = array[0, 0, 1] + array[2, 2, 0] + array[0, 1, 1]
# EN: Concatenate letters to form 'BYE'
# RU: Склеиваем буквы → получаем 'BYE'

print(word)
# EN: Print the formed word → 'BYE'
# RU: Выводим сформированное слово → 'BYE'