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

###########################################다이닝 매거진
try:
    # 팝업을 닫는 요소를 찾습니다. (예: close_button 클래스)
    close_button = driver.find_element(By.CLASS_NAME, "disable-user-select")
    close_button.click()
    print("팝업을 클릭하였습니다.")
    time.sleep(1.5)
except NoSuchElementException:
    print("팝업을 닫는 버튼을 찾을 수 없습니다.")


#뒤로 가기
driver.back()
time.sleep(2)


driver.execute_script("window.scrollBy(0, 4850);")
time.sleep(2)


try:
    # 탭 링크 요소 찾기
    tab_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".swiper-slide"))
    )

    max_retries = 1

    # 링크를 클릭하여 해당 페이지에 접근
    for i in range(len(tab_links)):
        for attempt in range(max_retries):
            try:
                # 링크 다시 찾기
                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".magazine-list-item"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} '다이닝 메거진' 페이지에 접근했습니다.")

                # 페이지 로드를 기다림
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

                 # 스크롤 다운
                time.sleep(1)
                driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
                time.sleep(0.5)
                driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
                time.sleep(0.5)
                driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
                time.sleep(0.5)

                # 뒤로 가기
                driver.back()
                time.sleep(1)
                break  # 성공적으로 링크를 클릭했으면 다음 링크로 이동

            except Exception as e:
                print("링크를 찾고 있습니다.:", e)

except Exception as e:
    print(f"오류 발생: {e}")

# 브라우저 종료
driver.quit()
