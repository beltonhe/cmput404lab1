import requests
r = requests.get("https://raw.githubusercontent.com/beltonhe/cmput404lab1/master/AllInOne.py")
print(r.text)
