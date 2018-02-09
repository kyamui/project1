from urllib.request import urlopen
import urllib
import re

def url_is_correct():
    '''
    使用requests.get方法判断url是否正确,并返回url
    :return:
    '''
    try:
        url = input("Please input the target test url:")
        #url = "http://10.70.18.47:8080" 这是我内网环境的测试地址
        urlopen(url)
        return url
    except:
        print('please input the correct url!!!')
        #exit(-1)   #如果url是固定写入的，那么必须添加此句，否则会一直循环
    return url_is_correct()

url = url_is_correct()

def url_protocol(url):
    '''
    获取输入的url地址的协议，是http、https等
    '''
    print('该站使用的协议是：' + re.findall(r'.*(?=://)',url)[0])
    return re.findall(r'.*(?=://)',url)[0]

urlprotocol = url_protocol(url)

