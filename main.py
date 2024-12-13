from k import ImageHandler

filename=input("Введите название изображения с форматом: ")
print(filename)
img = ImageHandler.ImageHandler.load(f"img\\{filename}")
format = filename.split('.')[1]

filename=filename.split('.')[0]

new_img = ImageHandler.ImageHandler.change_size(img, 300)


#filename=ImageHandler.ImageHandler.change_format(filename, 2)
ImageHandler.ImageHandler.save_with_data(img, filename, format)


img.show()

