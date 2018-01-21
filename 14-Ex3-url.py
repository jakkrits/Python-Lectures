from urllib.request import urlopen
response = urlopen('http://ppsmartbot.com')
data = response.read()
print(data)