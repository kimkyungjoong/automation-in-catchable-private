from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

# 엑셀 파일 경로와 시트 설정
excel_file = "/Users/kimkyungjoong/Downloads/매장수분석.xlsx"
sheet_name = "매장 5개 미만 법정동"

# 엑셀 데이터 읽기
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# 원하는 행 부분 선택
# start_row = 1000  # 시작 행
# end_row = 1100  # 종료 행
# partial_data = data.iloc[start_row:end_row]

# 웹드라이버 설정 (사파리 설정으로 사이즈는1200, 1000)
driver = webdriver.Safari()
driver.set_window_size(1200, 1000)

# 웹사이트 바로 이동 검색 영역으로
driver.get("https://beta-app.catchtable.co.kr/ct/search/total")
time.sleep(3)

try:
    # 팝업 노출 없애버리는 로직
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button._1080nhti._1ltqxco26"))
    )
    confirm_button.click()
    print("확인 버튼 클릭 완료!")
    time.sleep(1)
except TimeoutException:
    print("버튼을 찾지 못했습니다. 시간을 초과했습니다.")

# 검색창에 엑셀 데이터 입력해서 필요부분 확인
try:
    for index, row in partial_data.iterrows():    # 역순 -> data.iloc[::-1].iterrows(): /정상 -> data.iterrows():  /중간 지정부분 -> partial_data.iterrows(): 
        search_keyword = row.iloc[1]  # 엑셀 두 번째 열(name) 데이터 가져오기
        
        # 검색대기
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.k7k5xi6._1ltqxco1h"))
        )
        
        # 검색창 초기화 및 검색어 입력
        search_box.clear()
        search_box.send_keys(str(search_keyword))
        print(f"검색어 입력: {search_keyword}")
        
        # 검색
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # 결과 대기

        #뒤로 가서 환경 리셋
        driver.back()
        time.sleep(0.5)

except Exception as e:
    print(f"제발 오류 금지 제발 금지!: {e}")
# 다 했으면 웹사이트 off
finally:
    driver.quit()