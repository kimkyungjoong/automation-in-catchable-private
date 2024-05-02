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
time.sleep(2)

#베스트 리뷰

# 리뷰 게시물 요소 찾기
tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .best-review-item")))

# 현재 페이지에 있는 모든 리뷰를 열고 닫기
for i in range(len(tab_links)):
    try:
        # 다시 요소 찾기 (페이지 변화로 인해 요소가 업데이트될 수 있음)
        tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner  .best-review-item")
        
        link = tab_links[i]
        link_text = link.text
        link.click()

        # 페이지가 로드될 때까지 대기
        time.sleep(2)

        # 현재 열려있는 리뷰를 닫기
        driver.execute_script("window.scrollBy(0, 100);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.back()

    except Exception as e:
        print(f"링크를 클릭할 수 없습니다: {e}")
        print("메인을 다 훑고 탐색을 종료하겠습니다.")

# 브라우저 닫기
driver.quit()