import requests

## 1. version of request
## version check code from Damien Francois 
## https://stackoverflow.com/users/1763614/damienfrancois
## on https://stackoverflow.com/questions/20180543/how-to-check-version-of-python-modules
print(requests.__version__)

## 2. curl
## // use code from https://www.kite.com/python/answers/how-to-use-curl-in-python to complete python GET
url = "http://google.com"
res = requests.get(url)
print(res.text)


r = requests.get("https://raw.githubusercontent.com/beltonhe/cmput404lab1/master/read.py")
f = open("read.py", 'w')
f.write(r.text)
f.close()
