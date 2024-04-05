from django.shortcuts import render
import matplotlib.pyplot as plt

# io : 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO: 이진 데이터를 다루기 위한 버퍼를 제공함
# 버퍼: 임시 저장 공간. 
# 파일 시스템과 유사하지만, 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있음.
from io import BytesIO

# 텍스트 <-> 이진 데이터 변환할 수 있는 모듈
import base64

# 참고. 터미널 에러 고치기
# UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
# plt 를 만드는 쪽과 실제 화면에 그리는 곳이 다른 곳에서 동작하여 오류가 날 수 있다는 에러
# 참고: 공식문서(https://matplotlib.org/stable/users/explain/figure/backends.html)
# 백엔드를 Agg 로 설정하여 해결할 수 있다.
plt.switch_backend('Agg')


def index(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 8, 16]

    # 다른 view 함수에서 plt 를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여 초기화를 진행해줘야 함.
    plt.clf()

    plt.plot(x, y)
    plt.title('Test Graph')
    plt.ylabel('y label')
    plt.xlabel('x label')
    plt.grid()

    # 비어있는 버퍼 생성
    buffer = BytesIO()
    # 버퍼에 그래프를 저장
    # 이미지 형식은 png 로
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해 data URI 형식으로 만들어진 문자열을 생성
    context = {
        # 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'index.html', context)


import pandas as pd
csv_path = 'firstapp/data/austin_weather.csv'

# 파일 읽기
def example(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'example.html', context)