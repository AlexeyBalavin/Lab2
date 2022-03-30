
from PIL import Image
import lab21


with open("symbols.ini") as f: # _________________  Символы
    sym = f.readlines()        # _________________  Символы

name_image = 'p.jpeg'
img = Image.open(name_image)

lab21.invcolor(int(input("0 - Не включать инверсию цветов \n1 - Включить инверсию цветов \nВведите чило -  ")))

lab21.invgorizont(int(input("0 - Не включать инверсию сторон (лево-право) \n1 - Включить инверсию сторон (лево-право) \nВведите чило -  ")))

lab21.invvert(int(input("0 - Не включать инверсию сторон (низ-верх) \n1 - Включить инверсию сторон (низ-верх) \nВведите чило -  ")))


img_new = lab21.get_image_resize(img, 50,img)  # привести к размеру 50 пикселей

symbols = sym[int(input("0 - Числа \n1 - Буквы \n2 - Знаки \nВведите число - "))]  # ________________________  Символы

segment = 1024 // len(symbols)  # масимальное значение // на кол-во символов = длина сегмента



result = ''
width, height = img_new.size
for y in range(height):
    for x in range(width):
        r, g, b = img_new.getpixel((x, y))
        color = r + g + b
        pos = 0
        if color >= segment * 1:
            pos = 1
        if color >= segment * 2:
            pos = 2
        if color >= segment * 3:
            pos = 3
        result += symbols[pos] * 3
    result += '\n'

lab21.savetxt(int(input("0 - Не сохронять результат \n1 - Сохранить результат \nВведите чило -  ")),result)

print(result)



print("Размер рисунка (в символах) -", len(result)) #_______ Размер


