import requests
import string
import urllib.request
from bs4 import BeautifulSoup as bs
from PIL import Image
import re

braille_alphabet = []
braille_alphabet_images = []
pinterest_link = []

for char in string.ascii_lowercase:
    braille_alphabet.append("braille " + char)



for letter in braille_alphabet:
    print('\n', letter)
    img_parameters = {
        "query": letter,
        "tbm": "isch"
    }

    html = requests.get("https://www.google.com/search", params=img_parameters, timeout=5)

    #print("html_url: " + letter + html.text)


    soup = bs(html.content, "html.parser")
    #images = soup.select('div img')

    '''for link in soup.select('div img'):
        print("Link", link)
        pinterest_link.append(link)'''

    for link in soup.find_all('a',
                              attrs={'href': re.compile("https://www.pinterest.com")}):
        print(link)
        pinterest_link.append(link)



    images = soup.select('div img')
    print("Images", images)
    print("length: ", len(images))


    image_url = images[1]['src']
    print("image_url: ", image_url)

    braille_alphabet_images.append(image_url)


    letter_photoname = letter + ".jpg"
    urllib.request.urlretrieve(image_url, letter_photoname)
    data = requests.get(image_url).content
    #print(data)

    img = Image.open(letter_photoname)

