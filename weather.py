# 모듈
from urllib import request
from bs4 import BeautifulSoup

# 날씨 읽기
target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# 웹 분석
soup = BeautifulSoup(target, "html.parser")


# 약간 좀 어색(?)하니까 간단한 텍스트로 친근한(?)느낌을 주는 텍스트를 출력

print("오늘의 날씨는 다음과 같습니다;;ㅜㅜ") 


# location 태그 찾기
for location in soup.select("location"):
    print()
    print()
    print("도시: ", location.select_one("city").string) # city 태그를 찾아 출력
    print("날씨: ", location.select_one("wf").string) # wf 태그를 찾아 출력
    print("최저기온: ", location.select_one("tmn").string) # tmn 태그를 찾아 출력
    print("최고기온: ", location.select_one("tmx").string) # tmx 태그를 찾아 출력
    print()
    print()