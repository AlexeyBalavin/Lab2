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


def get_image_resize(_img, height_new,img):
    """ изменить размеры рисунка """
    _width, _height = _img.size  # исходные размеры рисунка
    width_new = _width // (_height // height_new)
    img_res = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_res