# 모듈/ 패키지

# 수학 함수들을 편하게 모아둔 모듈 [import math]
import math
import py10_function as calc
import requests

calc.multi(10, 4)

result = math.pow(2, 10)
print(result)

result = math.log2(4)
print(result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests 아래 보이는 request 다운로드 코드

res = requests.get('https://www.naver.com') # 네이버 사이트를 접속하라
print(res.status_code) # 200

print(res.content)