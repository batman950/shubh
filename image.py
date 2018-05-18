import random
import urllib.request

def download(url):
    
    name = random.randrange(1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url, full_name)

download("https://auto.ndtvimg.com/bike-images/gallery/honda/cbr-150r/exterior/bike-img.png")