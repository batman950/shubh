def start(url):
    word_list=[]
    file = open(file='url')
    for post_text in soup.findAll('a',{'class':'index_singleListingTitles'}):
        content = post_text.string
        words =content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start(url='C:\\Users\\User\PycharmProjects\shubh\sam.txt')