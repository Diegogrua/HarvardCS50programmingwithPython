import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) == 3:
    extensions = [".jpg", ".jpeg", ".png"]
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])
    if extension1[1] == extension2[1] and extension1[1] in extensions:
        try:
            user_image = Image.open(sys.argv[1]) # aca se abre el archivo
        except FileNotFoundError:
            sys.exit("File dones't exist")

        shirt = Image.open("shirt.png")
        size = shirt.size
        # (width, height)
        user_image = ImageOps.fit(user_image, size) # el tamaño
        user_image.paste(shirt, shirt) # se copia
        user_image.save(sys.argv[2]) # aca se guarda con el segundo comando
    elif extension1[1] != extension2[1]:
        sys.exit("input and ouput have different extensions")
    else:
        sys.exit("wrong extension")
elif len(sys.argv) > 3:
    sys.exit("too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("too few command-line arguments")
