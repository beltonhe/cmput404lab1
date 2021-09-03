import requests
import inspect
r1 = requests.get("https://raw.githubusercontent.com/beltonhe/cmput404lab1/master/Version.py")
r2 = requests.get("https://raw.githubusercontent.com/beltonhe/cmput404lab1/master/curl.py")
print(r1.text)
print(r2.text)