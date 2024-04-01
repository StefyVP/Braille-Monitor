from PIL import Image
from os import listdir
from pathlib import Path
import serial

full_dot = Image.open('dot.jpg')
empty_dot = Image.open('empty_dot.jpg')
letter = Image.open('Braille_letters/braille_A.jpg')

enter_letter = input("Enter letter:")
print(enter_letter)

photo = "Braille_letters/" + "braille_" + str(enter_letter) + ".jpg"
letter_photo = Image.open(photo)

#folder_dir = 'Braille_letters'

#images = Path(folder_dir).glob('br*')
#for image in images:
#    print(image)

#max_colors = 256

def is_black_image(dot):
    dot_width, dot_height = dot.size
    dotcenterwidth = dot_width // 2
    dotcenterheight = dot_height // 2

    print("dot size", dot.size)

    dot_pixelcolor = dot.getpixel((dotcenterwidth, dotcenterheight))
    print("dot color", dot_pixelcolor)
    if dot_pixelcolor[0] == 0 and dot_pixelcolor[1] == 0 and dot_pixelcolor[2] == 0:
        print("This dot is fully black colored")
    else:
        print("This dot is not colored")

#is_black_image(empty_dot)

def run_servos(letter):
    width, height = letter.size
    print("width ", width, "height", height)
    dot_width = width//3
    dot_height = height//4
    print("dot_width ", dot_width, "dot_height", dot_height)

    #while dot_width != width:
    #    while dot_height != height:
    #        print("dot_width ", dot_width, "dot_height", dot_height)
    #        dot_pixelcolor = letter.getpixel((dot_width, dot_height))
    #        print("dot color", dot_pixelcolor)
    #        if dot_pixelcolor[0] == 0 and dot_pixelcolor[1] == 0 and dot_pixelcolor[2] == 0:
    #            print("This dot is fully black colored")
    #        else:
    #            print("This dot is not colored")
    #        dot_height = dot_height + dot_height
    #    dot_width = dot_width + dot_width
    #    dot_height = height // 4


    for i in range (dot_width, width-1, dot_width):
        dot_height = height // 4
        for j in range(dot_height, height-1, dot_height):
            print("VLIZA")
            print("dot_width ", i, "dot_height", j)
            dot_pixelcolor = letter.getpixel((i,j))
            #print("dot color", dot_pixelcolor)
            if dot_pixelcolor[0] == 0 and dot_pixelcolor[1] == 0 and dot_pixelcolor[2] == 0:
                print("This dot is black")
            else:
                print("This dot is white")

print("Run servos")
run_servos(letter_photo)

#print("letter_photo")
#is_black_image(letter_photo)