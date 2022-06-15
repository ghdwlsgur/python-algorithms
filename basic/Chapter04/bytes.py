"""
- bytes는 유니코드가 아닌 문자열을 사용하는 것과 유사함.
- bytes는 원시 이진 데이터로 사용되어지거나 1바이트 문자로 고정을 위해 사용되어집니다.
- bytes HTTP 응답과 같은 파일과 네트워크 리소스는 바이트 스트림으로 전송되기 때문에 이해하는 것이 중요합니다.
"""

b = b"abcde"
print(b)
print(type(b))

s = b'abc def ghi'
print(s.split())

s2 = "Vi er så glad for å høre og lære om Python!"
b2 = s2.encode('utf-8')  # byte형
print(b2)
print(b2.decode('utf-8'))  # 문자열
