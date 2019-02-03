import requests
from bs4 import BeautifulSoup
from sys import argv
from urllib.request import urlretrieve  # Python 3

counter = 0

url = 'https://www.google.com/search?&tbm=isch&q='
query = argv[1]

# Gets the content of the page by using a get request
page_data = requests.get(url+query).content
bs4_data = BeautifulSoup(page_data, 'html.parser')

img_data = bs4_data.find_all('img')

for img in img_data:
    counter += 1
    urlretrieve(img['src'], "./output_images/" + str(counter) + '.jpg')
