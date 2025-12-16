# image_resizer.py

from PIL import Image # python -m pip install pillow


class ImageResizer:
    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)
    
    def resize_to(self, size: int):
        thumb = self.image.copy()
        thumb.thumbnail((size, size))
        path = self.get_path(size)
        thumb.save(path)
    
    def get_path(self, size: int):
        index = self.path.rindex('.')
        extra_name = '-' + str(size)
        return self.path[:index] + extra_name + self.path[index:]


image_paths = [
    r"C:\Users\zuio\Desktop\test01\html\foto\tipi.jpg",
    r"C:\Users\zuio\Desktop\test01\html\foto\pergola_condor_strecha.jpg",
]

for image_path in image_paths:
    my_image_resizer = ImageResizer(image_path)
    print(my_image_resizer.image)

    my_image_resizer.resize_to(500)
    my_image_resizer.resize_to(800)


class ImageResizer2:
    def resize(self, path, *sizes):
        image = Image.open(path)

        for size in sizes:
            thumb = image.copy()
            thumb.thumbnail((size, size))
            thumb.save(self.get_path(path, size))

    def get_path(self, path, size):
        index = path.rindex('.')
        return path[:index] + '-' + str(size) + path[index:]

resizer = ImageResizer2()
resizer.resize(
    r"C:\Users\zuio\Desktop\test01\html\foto\tipi.jpg",
    200, 400, 600
)



class CharCounter:
    """ třída umožní vypočítat počet znaků v txt souboru """
    def __init__(self, path):
        self.path = path

    def count_chars(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return len(file.read())

    def print_info(self):
        print(f"{self.count_chars()} - {self.path}")

# takto to chci používat
counter = CharCounter('path.txt')
counter.print_info() # 7373 - path.txt



"""
2 způsoby

1. každý obrázek má vlastní ImageResizer

2. ImageResizer dokáže měnit velikost pro různé obrázky

3. WordCounter



"""
