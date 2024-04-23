## 기술 트렌드 분석 웹 애플리케이션
- 이 Django 프로젝트는 BeautifulSoup 및 Selenium을 사용하여 Google 검색 결과를 스크래핑하고, 사용자가 지정한 키워드에 대한 기술 트렌드를 분석하고 시각화합니다.

### 기능
- 키워드 관리: 사용자는 웹 페이지에서 새로운 키워드를 추가할 수 있습니다. 이를 통해 사용자는 관심 있는 주제나 트렌드에 대한 키워드를 지정할 수 있습니다.
또한, 기존의 키워드를 삭제할 수 있습니다. 이는 사용자가 더 이상 분석하고 싶지 않은 키워드를 제거할 때 유용합니다.

- 크롤링: crawling 함수는 지정된 키워드에 대해 Google에서 검색 결과를 스크래핑하여 데이터베이스에 저장합니다.
사용자가 원하는 기간 동안의 검색 결과를 가져올 수 있습니다. 이는 get_data 함수에서 period 매개변수를 통해 설정됩니다.

- 기술 트렌드 시각화: crawling_histogram 및 crawling_advanced 함수는 저장된 데이터를 기반으로 기술 트렌드를 시각화합니다. 히스토그램을 통해 각 키워드에 대한 검색 결과의 상대적인 크기를 쉽게 파악할 수 있습니다.
crawling_histogram은 모든 데이터를 기반으로 한 히스토그램을 생성합니다. 반면에, crawling_advanced는 더 긴 기간(예: 연간)에 대한 데이터를 분석하여 시각화합니다.

### 사용법
- 웹 페이지에서 키워드를 추가합니다.
- 크롤링 버튼을 클릭하여 키워드에 대한 Google 검색 결과를 스크래핑합니다.
- 시각화 버튼을 클릭하여 기술 트렌드를 히스토그램으로 확인합니다.

### 기술 스택
- Python
- Django
- BeautifulSoup
- Selenium
- Matplotlib
- SQLite

### 어려웠던 부분
- model 작업 중 Foriegn키 적용 여부
- 크롤링 작업의 전반적인 부분, 특히 중복처리
- sqlite3 파일에서 pandas로 데이터 처리
- get_or_create()
- 어려웠음

### 해결 방법
- 크롤링 작업의 중복처리는 get_or_create로 해결
- get_or_create에서 중복이면 안되는 인자가 중복으로 등록되는 문제 발생
- get_or_create의  defaults에 중복이 될 수 있는 인자를 넣으니 해결
 
 ```py
 conn = sqlite3.connect('db.sqlite3')
    df = pd.read_sql("SELECT * FROM trends_trend WHERE search_period = 'all'", conn)
 ```
 - sql 판다스로 변환해서 읽어오는 코드