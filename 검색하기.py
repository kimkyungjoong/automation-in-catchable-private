from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException  # TimeoutException import 추가
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
time.sleep(3)


try:
    # 검색 링크 클릭
    # 'href' 속성을 사용하여 요소를 찾음
    search_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/ct/search']"))
    )
    search_link.click()
    time.sleep(2)

    complete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shepherd-button"))
    )
    complete_button.click()
    time.sleep(1)

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "design_system_gjbv2i0"))
    )
    button.click()
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")



#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(1)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)


try:
    # '스시오마카세' 버튼 클릭
    # 버튼의 텍스트를 기준으로 선택하여 클릭
    sushi_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='스시오마카세']]"))
    )
    sushi_button.click()
    

except Exception as e:
    print(f"d인기메뉴 오류: {e}")


try:
    # '일식' 버튼 클릭
    # XPath를 사용하여 '일식' 텍스트가 있는 버튼을 선택
    japanese_food_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='일식']]"))
    )
    japanese_food_button.click()
    time.sleep(1)

except Exception as e:
    print(f"국가별 오류: {e}")


try:
    # '20만원대' 버튼 클릭
    # CSS 선택자를 사용하여 해당 클래스를 가진 버튼을 찾고 클릭
    price_range_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.design_system_1mb4yfk0.design_system_jg3o1w1d.design_system_1mb4yfk2"))
    )
    price_range_button.click()
    time.sleep(1)

except Exception as e:
    print(f"가격 오류: {e}")



try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)



try:
    # '검색' 버튼 클릭
    # 클래스 이름 'btn', 'btn-lg', 'btn-red'를 사용하여 버튼 클릭
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-red"))
    )
    search_button.click()
    time.sleep(2)
    # 스크롤 다운
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)

except Exception as e:
    print(f"검색 오류: {e}")





#################### 추천 해시태그
try:
    # 상황별 주제별 BEST 찾기
    tab_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".swiper-slide a"))
    )

    max_retries = 1

    # 링크를 클릭하여 해당 페이지에 접근
    for i in range(len(tab_links)):
        for attempt in range(max_retries):
            try:
                # 링크 다시 찾기
                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".swiper-slide a"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 추천 해시태그 페이지에 접근했습니다.")

                # 페이지 로드를 기다림
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

                # 스크롤 다운
                time.sleep(2)
                driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
                time.sleep(1)
                driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
                time.sleep(1)
                driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
                time.sleep(1)

                # 뒤로 가기
                driver.back()
                time.sleep(2)
                break  # 성공적으로 링크를 클릭했으면 다음 링크로 이동

            except Exception as e:
                print("링크를 찾고 있습니다.:", e)

except Exception as e:
    print(f"오류 발생: {e}")





# 드라이버 종료 (실행이 끝난 후 브라우저를 닫음)
driver.quit()
