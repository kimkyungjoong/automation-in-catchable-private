from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException  # TimeoutException import 추가
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

###################청담그늘
driver.get("https://beta-app.catchtable.co.kr/ct/shop/gnl")
time.sleep(2)

try:
    # '메뉴' 탭을 클릭
    menu_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='사진']]"))
    )
    menu_tab.click()
    print("사진 탭 클릭 성공!")
    time.sleep(8)
except Exception as e:
    print(f"청담 그늘 탭 연결 실패: {e}")


###################타크
driver.get("https://beta-app.catchtable.co.kr/ct/shop/tac")
time.sleep(2)

try:
    # '메뉴' 탭을 클릭
    menu_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='사진']]"))
    )
    menu_tab.click()
    print("사진 탭 클릭 성공!")
    time.sleep(8)
except Exception as e:
    print(f"청담 그늘 탭 연결 실패: {e}")


finally:
    if 'driver' in locals():
        print("완벽한 성공 후 마무리")
        driver.quit()