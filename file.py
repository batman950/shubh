from urllib import request  # get files from internet to get access

url = "https://en.wikipedia.org/wiki/Main_Page"


def download(f_url):
    res = request.urlopen(f_url)
    file = res.read()
    file1 = str(file)
    fx = open("sam.txt", "w")
    fx.write(file1)


download(url)




