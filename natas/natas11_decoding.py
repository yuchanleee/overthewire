import base64
from urllib.parse import unquote

# 1. 기존 평문과 암호문에서 XOR 키 추출
str_decoded = '{"showpassword":"no","bgcolor":"#ffffff"}'
decoded = str_decoded.encode()

cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"
encoded = unquote(cookie)
mid = base64.b64decode(encoded)

xor_key = [chr(decoded[i] ^ mid[i]) for i in range(len(decoded))]
key_full = ''.join(xor_key)
print("추출한 XOR 키:", key_full)  # 예: eDWo

# 2. 새 평문 만들기
key = 'eDWo'
want = '{"showpassword":"yes","bgcolor":"#ffffff"}'.encode()
key = key.encode()

# 3. XOR 후 base64 인코딩
after_xor = bytes([want[i] ^ key[i % len(key)] for i in range(len(want))])
ans = base64.b64encode(after_xor).decode()

print("조작된 쿠키:", ans)
