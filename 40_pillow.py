import os  
""" všechny obrázky ve složce """

from PIL import Image
#OHNO, mám je uložené i v původní složce
"""
úkol: udělat for cyklus nad x obrázky a pro všechny udělat thumb (malá varianta)
- mužete vzít pole cest
- nebo lépe: zadat složku a zní vytáhnout všechny jpg, png obrázky

volitelně: get_thumb_path by mohlo obsahovat informaci o velikosti
"""

DEFAULT_SIZE = 320
DEFAULT_THUMB_SIZE = (DEFAULT_SIZE, DEFAULT_SIZE)


def resize_image(path, save_to, size=DEFAULT_THUMB_SIZE):
    image = Image.open(path)
    image.thumbnail(size)
    image.save(save_to)


def get_thumb_path(path, size=DEFAULT_THUMB_SIZE):
    index = path.rindex('.')
    extra_name = '-' + str(size[0]) + 'x' + str(size[1])
    return path[:index] + extra_name + path[index:]

def main():
    folder = r"C:\Users\zuio\Desktop\test01\html\foto"
    resize_to = (500, 500)

    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(folder, filename)
            thumb_path = get_thumb_path(path, resize_to)

            resize_image(path, thumb_path, size=resize_to)
            print("Vytvořen thumb:", thumb_path)



#def resize_one():
 #   resize_to = (500, 500)

    # path = r"C:\Users\zuio\Desktop\test01\html\foto\tipi.jpg"
    # thumb_path = get_thumb_path(path, resize_to)

    #resize_image(path, thumb_path, size=resize_to)
    #print('thumb saved into', thumb_path)

if __name__ == '__main__':
    main()
    #resize_one()