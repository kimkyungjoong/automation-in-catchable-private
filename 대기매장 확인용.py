from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

# [1] 엑셀 파일 경로 및 데이터 로드
excel_file = "/Users/kimkyungjoong/Downloads/대기가맹매장리스트.xlsx"
sheet_name = "result"
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# 1~300행 슬라이싱
partial_data = data.iloc[0:400]

# [2] 드라이버 설정
driver = webdriver.Safari()
driver.set_window_size(1200, 1000)

# [3] CatchTable 검색 URL
search_url = "https://app.catchtable.co.kr/ct/search/total"

# [4] 팝업 닫기 
def close_popup_if_present():
    try:
        confirm_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button._1080nhti._1ltqxco26"))
        )
        confirm_button.click()
        print("팝업 닫기 완료")
    except TimeoutException:
        print("팝업 없음")

# [5] 검색어 입력 (input 또는 div 대응)
def input_search_keyword(keyword):
    try:
        # 첫번째 
        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.k7k5xi6._1ltqxco1h"))
        )
    except TimeoutException:
        # 뒤로가기 후 클래스 바뀌면서 클래스 값 변경 후 재 시도
        fake_box = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div._1imj5prc._1ltqxco1h._1imj5pre"))
        )
        fake_box.click()
        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.k7k5xi6._1ltqxco1h"))
        )

    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    print(f" 검색어 입력: {keyword}")
    time.sleep(2)

# [6] 메인 루프
try:
    for index, row in partial_data.iterrows():
        keyword = str(row.iloc[2]).strip()
        print(f"\n {index+1}번째 실행 검색 매장: {keyword}")

        driver.get(search_url)
        close_popup_if_present()
        input_search_keyword(keyword)

        time.sleep(1.5)  # 검색 결과 렌더링 대기

        try:
            #  결과 없음 메시지 먼저 탐지
            driver.find_element(By.CSS_SELECTOR, "div.hgay2w0")
            print("검색결과 없음 (조건에 맞는 매장이 없어요)")
            continue  # 다음 검색어로 넘어감
        except:
            pass  # 결과 없음 메시지가 없으면 다음 단계로 진행

        try:
            #  검색 결과 존재 시, 첫 번째 결과만 클릭
            results = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ShopListItem_titleBox__1p45wh64')]"))
            )

            if not results:
                print("검색결과 없음 (리스트 비어 있음)")
                continue

            driver.execute_script("arguments[0].click();", results[0])
            print("검색 매장 클릭 성공")

        except TimeoutException:
            print("검색결과 없음 ")
            continue

        time.sleep(1.5)
except Exception as e:
    print(f"\n 치명적 오류 발생: {type(e).__name__} - {e}")

finally:
    driver.quit()
    print("\n 드라이버 종료 완료")
