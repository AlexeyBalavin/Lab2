
from PIL import Image
import lab21


with open("symbols.ini") as f: # _________________  Символы
    sym = f.readlines()        # _________________  Символы

name_image = 'p.jpeg'
img = Image.open(name_image)

if int(input("0 - Не включать инверсию цветов \n1 - Включить инверсию цветов \nВведите чило -  ")) == 1:
    img = lab21.inversion(img,img.size[0],img.size[1])

if int(input("0 - Не включать инверсию сторон (лево-право) \n1 - Включить инверсию сторон (лево-право) \nВведите чило -  ")) == 1:
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

if int(input("0 - Не включать инверсию сторон (низ-верх) \n1 - Включить инверсию сторон (низ-верх) \nВведите чило -  ")) == 1:
    img = img.transpose(Image.FLIP_TOP_BOTTOM)

#img = img.rotate(90) # __________ Поворот
img_new = lab21.get_image_resize(img, 50,img)  # привести к размеру 50 пикселей

symbols = sym[int(input("0 - Числа \n1 - Буквы \n2 - Знаки \nВведите число - "))]  # ________________________  Символы

count = len(symbols)
full = 256 + 256 + 256  # максимальное значение
segment = full // count  # длина сегмента

res = open("p.txt","w+") # Создание текстового документа

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

if int(input("0 - Не сохронять результат \n1 - Сохранить результат \nВведите чило -  ")) == 1: 
    res.write(result) 
    res.close()      # Запись в текстовый документ

print(result)



print("Размер рисунка (в символах) -", len(result)) #_______ Размер


