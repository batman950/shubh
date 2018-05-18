from urllib import request
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list=[]
    source_code= request.urlopen(url)
    soup = BeautifulSoup(source_code,"html.parser")
    for post_text in soup.findAll('a'):
        content =  post_text.string
        #words = content.lower().split()
        for each_word in content:
            print(each_word)
            word_list.append(each_word)
            print(word_list)
start("https://en.wikipedia.org/wiki/Main_Page")
