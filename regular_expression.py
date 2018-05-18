import re

pattern = re.compile(r'\w+@[a-z]+[.[a-z]+]*')  # r=raw string
string = "9464163122 adss@gmail.com saad921@gmail.com 9466163522 948416312 casddadasd@asd sadsad@das.sad.asd.s"
data = pattern.findall(string)
print(data)
pattern1 = re.compile(r'\w+[.]png|\w+[.]gif|\w+[.]img')
string2 = "sad.png Csdas.sdada sda.img adas.da.ad.as.img 435.png asas.ipn dawsd.img  asdfas.gnp"
data1 = pattern1.findall(string2)
print(data1)
pattern2 = re.compile(r'http://[\w-]+[.[a-z]+]*')
string3 = "hello members http://kumarshubham950.com http://sadsa3424322423.com http://fasdada-908_ahsa.com   http://asdaasas.co.in  fasfaf@sdvf.min "
data2 = pattern2.findall(string3)
print(data2)


# get the url from a list of file
