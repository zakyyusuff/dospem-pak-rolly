import requests

data = requests.get('https://google.com/')
print(data.text)
result = data
contents = result
print(contents)
