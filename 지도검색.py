from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException  # TimeoutException import 추가
import time
import random

# Safari 드라이버 초기화
driver = webdriver.Safari()

driver.set_window_size(1200, 1000)

# 웹 페이지 열기
driver.get("https://beta-app.catchtable.co.kr")

# 10초간 대기
time.sleep(5)

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
    print("GNB영역 검색 클릭")
    time.sleep(2)

    #달력 영역 클릭
    complete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "_1mkd3670"))
    )
    complete_button.click()
    time.sleep(2)
    
    next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next page']")

    # 3. 버튼 클릭
    next_button.click()
    print("다음 페이지 버튼 클릭 완료")

    # 클릭 후 잠시 대기 (클릭 완료를 위해)
    time.sleep(2)


    date_elements = [el for el in driver.find_elements(By.XPATH, "//div[@role='button']") if el.is_enabled()]

    # 4. 무작위로 요소 선택
    date_elements
    random_element = random.choice(date_elements)
    time.sleep(1)
    
    # 5. 무작위로 선택된 날짜 클릭
    random_element.click()
    time.sleep(2)

    # 결과 출력
    print(f"선택된 날짜: {random_element.text}")

    # 잠시 대기 (클릭이 완료되도록 시간 확보)
    time.sleep(3)

    
    # 클래스 이름으로 요소 찾기
    apply_button = driver.find_element(By.CLASS_NAME, "_1mohj8u2")  # 첫 번째 클래스명으로 찾기

    # 3. 버튼 클릭
    apply_button.click()
    print("적용하기 버튼 클릭 완료")

    # 클릭 후 잠시 대기 (클릭 완료를 위해)
    time.sleep(2)

    button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-lg') and contains(@class, 'btn-red')]")

    # 3. 버튼 클릭
    button.click()
    print("검색 버튼 클릭 완료")

    # 클릭 후 잠시 대기 (클릭 완료를 위해)
    time.sleep(5)

    # element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "xnbnj36")))

    # # 요소가 화면에 보이도록 스크롤
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    # # ActionChains를 사용한 드래그
    # action = ActionChains(driver)
    # action.click_and_hold(element).move_by_offset(0, 200).release().perform()
    # time.sleep(2)  # 확인을 위해 잠시 대기

    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_53lcbm0._53lcbm1")))

    element = driver.find_element(By.CLASS_NAME, "_53lcbm0._53lcbm1")  # 이동할 요소의 클래스명을 입력

    # 3. ActionChains을 사용하여 요소 이동
    action = ActionChains(driver)
    
    # 예: 0px 만큼 x축 이동하고, 1157px 만큼 y축 이동
    action.click_and_hold(element).move_by_offset(0, 1157).release().perform()
    print("요소 이동 완료")

    # 이동 후 잠시 대기 (동작 확인을 위해)
    time.sleep(2)


#     # 특정 영역의 버튼 클릭
#     specific_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".obkhm80 .obkhm81"))
#     )
#     specific_button.click()
#     print("캘린더 클릭")
#     time.sleep(2)

#      # 특정 시간 선택 (오후 19:30)
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio'][value='1930']"))
#     )
#     # 자바스크립트로 직접 클릭 시도
#     driver.execute_script("arguments[0].click();", radio_button)
#     print("7시30분 클릭 완료")
#     time.sleep(2)

#     # '확인' 버튼 클릭
#     confirm_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".sticky-bottom-btns .btn.btn-lg.btn-red"))
#     )
#     confirm_button.click()
#     print("확인!!")
#     time.sleep(2)


#     # '서울' 링크 요소 찾기
#     element = driver.find_element(By.XPATH, "//a[@id='map-aggregation-marker']")
#     driver.execute_script("arguments[0].click();", element)
#     print("서울 매장 클릭")
#     time.sleep(2)


#     #강남구 클릭
#     element = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.XPATH, "//a[@class='_1fs8ek32' and span[text()='강남구']]"))
#     )
#     # 스크롤하여 요소가 보이게 하기
#     driver.execute_script("arguments[0].scrollIntoView(true);", element)
#     time.sleep(1)  # 스크롤이 완료되기를 기다립니다.

#     # 요소 클릭
#     driver.execute_script("arguments[0].click();", element)
#     print("강남구 클릭 성공")
#     time.sleep(5)

#     #새로고침
#     driver.refresh()
#     time.sleep(3)

#     # img 태그 요소 찾기
#     element = driver.find_element(By.XPATH, "//div[@style='position: relative;']/img[@class='m1pocwl _1ltqxco1v' and @src='/public/img/icons/pin-active.webp']")
#     actions = ActionChains(driver)
#     actions.move_to_element(element).click().perform()
#     time.sleep(2)
#     print("강남구 매장 클릭")

#     # 웨이팅 버튼 요소 찾기
#     waiting_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_1dl7a7ab')]"))
#     )
#     # JavaScriptExecutor를 사용하여 클릭 시뮬레이션
#     driver.execute_script("arguments[0].click();", waiting_button)
#     print("웨이팅 버튼 클릭 완료")
#     time.sleep(2)

#      # 픽업 예약 버튼 요소 찾기
#     element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[contains(., '픽업 예약')]"))
#     )
#     element.click()
#     print("픽업 예약 버튼 클릭")
#     time.sleep(3)

#     # "예약" 버튼을 찾기
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//button[@type='button' and contains(@class, '_1dl7a7a3') and contains(@class, '_1ltqxco1k') and contains(@class, '_1dl7a7a5') and contains(@class, '_1dl7a7a7') and contains(@class, '_1dl7a7ab')]"))
#     )

#     # ActionChains를 사용하여 클릭
#     actions = ActionChains(driver)
#     actions.move_to_element(element).click().perform()
#     print("예약 버튼 클릭")
#     time.sleep(3)

#     # "매장 더보기" 버튼
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'xnbnj34') and contains(@class, '_1ltqxco20')]"))
#     )
#     element.click()
#     print("매장 더보기 버튼 클릭")
#     time.sleep(3)

#     #목록 클릭 
#     wait = WebDriverWait(driver, 10)
#     button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._1u9cbg30._1ltqxco20._1u9cbg31")))
#     button.click()
#     print("목록을 클릭했습니다.")
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
#     time.sleep(0.5)


except Exception as e:
    print(f"에러난다 안돼!!!: {e}")

