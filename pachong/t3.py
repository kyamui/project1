import urllib.request
import urllib
data = urllib.request.urlopen('http://www.x11xx.com')
try:

    print(data.read())
except urllib.error.URLError as e:
    print(e.reason)