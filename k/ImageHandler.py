from PIL import Image, ImageOps
import datetime

now = datetime.datetime.now()

class ImageHandler():
    #загрузка изображения
    def load(filename):
        with Image.open(filename) as img:
            img.load()
        print(f"Изображение {filename} открыто")
        return img
    
    #сохранение изображения
    def save(img, filename, format):
        img.save(f"img\\new_{filename.split('.')[0]}.{format}")

    #сохранение изображения c датой    
    def save_with_data(img, filename, format):
        date = (now.strftime("%d-%m-%Y"))
        img.save(f'img\\new_{filename.split(".")[0]}-{date}.{format}')
    
    #изменение размера
    def change_size(img, new_size):
        try:
            img = img.resize(new_size)
            print("Размер изображения изменён")
            img.show()
        except:
            print("Некорректный ввод данных")
        return img

    #изменение формата
    def change_format(format):
        if(format==1):
            return '.jpg'
        elif(format==2):
            return '.gif'
        elif(format==3):
            return '.png'
        elif(format==4):
            return '.jpeg'
        else:
            print("Некорректный ввод данных")
            return format
    
    #масштабирование до 50%
    def change_scale(img):
        img = ImageOps.scale(img,0.5)
        return img


    