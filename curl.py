import requests
url = "http://google.com"
res = requests.get(url)
print(res)
with open(__file__) as f:
    print(f.read())