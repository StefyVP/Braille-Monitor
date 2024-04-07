import os
from rembg import remove
from PIL import Image
import string


braille_alphabet = []
braille_alphabet_images = []
pinterest_link = []
i = 0

for char in string.ascii_lowercase:
    braille_alphabet.append("braille " + char)
    input_path = braille_alphabet[i] + ".jpg"
    output_path = braille_alphabet[i] + "_rembg.png"
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    if(os.path.exists(input_path)):
        os.remove(input_path)
    else:
        print("The file does not exist")
    i = i+1



