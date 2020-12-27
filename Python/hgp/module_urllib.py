from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

# 바이너리 데이터 출력
print(output)