from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import random


# Safari 드라이버 초기화
driver = webdriver.Safari()

driver.set_window_size(1200, 1000)

# 웹 페이지 열기
driver.get("https://beta-app.catchtable.co.kr")

# 10초간 대기
time.sleep(3)

try:
    # 팝업을 닫는 요소를 찾습니다. (예: close_button 클래스)
    close_button = driver.find_element(By.CLASS_NAME, "disable-user-select")
    close_button.click()
    print("팝업을 닫았습니다.")
    time.sleep(1.5)
except NoSuchElementException:
    print("팝업을 닫는 버튼을 찾을 수 없습니다.")


#뒤로 가기
driver.back()
time.sleep(3)

# tab_links 변수 정의
tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .best-food-list-item")

max_retries = 1
# 링크를 클릭하여 해당 페이지에 접근 (음식종류별 BEST)
for i in range(len(tab_links)):
    for attempt in range(max_retries):
        try:
            # 링크를 다시 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .best-food-list-item")
            link = tab_links[i]
            link_text = link.text  # 링크 클릭 전에 텍스트를 가져옵니다.
            link.click()
            print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")
            # 페이지가 로드될 때까지 대기하거나 다음 동작 수행
            # WebDriverWait(driver, 10).until(EC.url_to_be("원하는 URL"))
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)

            driver.back()
            break  # 성공적으로 링크를 클릭했으면 다음 링크로 이동합니다.
        except Exception as e:
            print("링크를 클릭할 수 없습니다:", e)
            print("어디로 가시나요를 종료하겠습니다.")


# 브라우저 종료
driver.quit()