from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
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

driver.execute_script("window.scrollBy(0, 1550);") 
time.sleep(2)

#고객님이 좋아할 매장
try:
    # 매장 목록 로딩 대기
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")))

    # 각 매장 클릭 (인덱스 1부터 70개까지)
    for i in range(1, 70):  #v-scroll-inner .restaurant-list-item가 웬만한 모든 매장에 걸려있어서 숫자로 구별. (웨이팅 핫플레이스 best, 고객님 좋아할 매장, 놓치면 안되는 혜택 가득, 캐치테이블 on, 미쉐린가이드 2024)
        try:
            # 다시 매장 목록 요소 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")

            # 원하는 매장 요소 가져오기
            link = tab_links[i]
            link_text = link.find_element(By.CLASS_NAME, "name").text
            print(f"{link_text} 매장을 방문합니다...")

            # 매장 클릭
            driver.execute_script("arguments[0].scrollIntoView();", link)  # 요소가 보일 때까지 스크롤
            driver.execute_script("window.scrollBy(0, 500);")  # 스크롤 조정
            link.click()

            # 매장 페이지 로딩 대기
            time.sleep(0.5)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)

            # 이전 페이지로 이동 (뒤로 가기)
            driver.execute_script("window.history.go(-1);")
            print(f"{link_text} 매장 방문 후 이전 페이지로 돌아갑니다...")

            # 다음 매장 방문 전 대기
            time.sleep(0.5)

        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
            print("탐색을 종료합니다.")
            break

    # 두 번째 섹션의 전체보기 링크 클릭
    second_section_show_all_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".container:nth-of-type() .btn-more")))
    second_section_show_all_link.click()
    print("두 번째 섹션의 전체보기 링크를 클릭했습니다.")

except Exception as e:
    print("오류 발생:", e)

finally:
    # 브라우저 닫기
    driver.quit()