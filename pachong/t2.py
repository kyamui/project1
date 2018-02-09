import urllib.request, socket, re, sys, os

# 定义文件保存路径
targetPath = "C:\\Users\\admin\\PycharmProjects\\project1\\pachong\\111"


def saveFile(path):
    # 检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

        # 设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos + 1:])
    return t


# 用if __name__ == '__main__'来判断是否是在直接运行该.py文件


# 网址
url = "https://www.tumblr.com/explore/photos"
# url = "https://www.douban.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
}

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

f = open("out.txt","w+")
# print(set(re.findall(r'(https:[^s]*?(jpg|png|gif))',str(data))),file=f)
# f.close()
print(set(re.findall(r'(https:[^s]*?(jpg|png|gif))',str(data))))

for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(data))):

    print(link)
    try:
        print('成功')
        urllib.request.urlretrieve(link, saveFile(link))
    except:
        print('失败')