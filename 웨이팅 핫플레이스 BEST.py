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

#웨이팅 핫플레이스 best 
tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")
max_retries = 1

for i in range(len(tab_links)):
    for attempt in range(max_retries):
        try:
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item ")
            link = tab_links[i]
            link_text = link.text
            link.click()

            # 링크를 클릭하고 페이지가 로드될 때까지 대기
            #WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)

            driver.back()

            print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

            break
        except Exception as e:
            print("링크를 클릭할 수 없습니다:", e)
            print("메인을 다 훑고 탐색을 종료하겠습니다.")

tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .showall")
max_retries = 1

for i in range(len(tab_links)):
    for attempt in range(max_retries):
        try:
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .showall ")
            link = tab_links[i]
            link_text = link.text
            link.click()

            # 링크를 클릭하고 페이지가 로드될 때까지 대기
            #WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)
            print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

            break
        except Exception as e:
            print("링크를 클릭할 수 없습니다:", e)
            print("메인을 다 훑고 탐색을 종료하겠습니다.")
            driver.back()
            time.sleep(3)