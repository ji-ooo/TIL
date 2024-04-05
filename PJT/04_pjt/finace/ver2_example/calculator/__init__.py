# __init__.py
# - 패키지를 나타내는 데 사용되는 특별한 파일
# 1. 파이썬 인터프리터에게 해당 디렉토리를 패키지로 취급하도록 알려줌
# 2. 패키지가 로드될 때 실행되는 초기화 코드
# 3. 패키지 수준의 변수나 함수를 정의 

start_number = 10

def start_add(x):
    return start_number + x;

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y