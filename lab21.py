from PIL import Image

def inversion(img,height,width):
    for y in range(int(height)):
        for x in range(int(width)):
            r, g, b = img.getpixel((x,y))
            r = 255 - r
            g = 255 - g
            b = 255 - b
            img.putpixel((x, y), (r,g,b))
    return img # Инверсия цветов

def invcolor(num1):
    if num1 == 1:
        img = lab21.inversion(img,img.size[0],img.size[1])
        return(img)

def invgorizont(num2):    
    if num2 == 1:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        return(img)

def invvert(num3):
    if num3 == 1:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        return(img)


def get_image_resize(_img, height_new,img):
    """ изменить размеры рисунка """
    _width, _height = _img.size  # исходные размеры рисунка
    width_new = _width // (_height // height_new)
    img_res = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_res

def savetxt(num4,result):
    if num4 == 1: 
        res = open("p.txt","w+") # Создание текстового документа
        res.write(result) 
        res.close()      # Запись в текстовый документ