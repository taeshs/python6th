import urllib.request

url = 'https://www.google.com'

request = urllib.request.Request(url)
respone = urllib.request.urlopen(request)

html = respone.read()

print(html)