# 모듈 : 미리 작성된 라이브러리 등을 프로젝트에서 import를 통해 이용
# 표준 모듈(파이썬 기본 제공) <-> 외부 모듈(사람들이 작성)

import math
import review_module02

# 만약 특정한 모듈 파일만 이용하고 싶다면 (모듈 파일이 너무 크거나..)
# from review_module02 import add : lib 모듈 내의 add 함수만 사용하겠다

# 모듈 이름이 너무 길 때는
# import review_module02 as r -> r.add(n,m) : alias

# 제곱
print(math.pow(2, 4)) 
# 제곱근
print(math.sqrt(16))
# 최대 공약수
print(math.gcd(72, 24))

# 사용자 정의 모듈
print(review_module02.add(2,4))