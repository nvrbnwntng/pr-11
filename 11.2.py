from PIL import Image
import os

images = 'забыл.jpg'

if images.lower().endswith(('.jpg', '.jpeg', '.png')):
    image = Image.open(images)
    print(f"Width: {image.size}")
    print(f"Format: {image.format}")
    print(f"Color: {image.mode}")
    image.show()
else:
    print(f"Ошибка: файл '{images}' не является изображением JPG или PNG")
