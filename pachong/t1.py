# import urllib.request
# # response = urllib.request.urlopen("https://www.tumblr.com/explore/photos")
# response = urllib.request.urlopen("http://www.baidu.com")
#
# # f = open("out.txt","w+")
# #
# # print(response,file=f)
# # f.close()
#
# print(response)

import re, urllib
from urllib.request import urlopen

url_getallfolders = 'https://www.tumblr.com/explore/photos'
x = urlopen(url_getallfolders)
data = x.read()
# data = data.decode('utf-8')
# print(data)
f = open("out.txt","w+")
print(data,file=f)
f.close()

