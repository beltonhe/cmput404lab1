## 1. version of request
## version check code from Damien Francois 
## https://stackoverflow.com/users/1763614/damienfrancois
## on https://stackoverflow.com/questions/20180543/how-to-check-version-of-python-modules
import requests
print(requests.__version__)

## 2. curl
## // use code from https://www.kite.com/python/answers/how-to-use-curl-in-python to complete python GET
import requests
url = "http://google.com"
res = requests.get(url)
print(res.text)