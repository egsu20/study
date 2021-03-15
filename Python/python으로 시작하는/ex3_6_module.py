# 1. from 모듈이름 import 포함할 함수나 변수
# 모듈이름.변수와 같은 형식 필요 x
# 2. import 모듈 as 식별자(별명)

from math import sqrt

n = sqrt(3.0)

if n*n == 3.0:
    print("sqrt(3.0)*sqrt(3.0)은 3.0과 같다")
else:
    print("sqrt(3.0)*sqrt(3.0)은 3.0과 같지 않다")
