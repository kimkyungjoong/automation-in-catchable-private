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



###################키친마이아르
driver.get("https://beta-app.catchtable.co.kr/ct/shop/kitchenmaillard")
time.sleep(2)

try:
    # '메뉴' 탭을 클릭
    menu_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='메뉴']]"))
    )
    menu_tab.click()
    print("메뉴 탭 클릭 성공!")
    time.sleep(2)
except Exception as e:
    print(f"키친 마이아르 메뉴 탭 연결 실패: {e}")


try:
    # 'FOOD' 항목을 클릭
    food_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='FOOD']]"))
    )
    food_item.click()
    print("키친 마이아르 FOOD 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
except Exception as e:
    print(f"키친 마이아르 food 항목 연결 실패: {e}")

try:
    # 'DRINK' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='DRINK']]"))
    )
    drink_item.click()
    print("키친 마이아르 DRINK 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
except Exception as e:
    print(f"키친 마이아르 drink 항목 연결 실패: {e}")



###################리파인 성수점 
driver.get("https://beta-app.catchtable.co.kr/ct/shop/refine_seongsu?type=VISIT_RESERVATION")
time.sleep(2)

try:
    # '메뉴' 탭을 클릭
    menu_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='메뉴']]"))
    )
    menu_tab.click()
    print("메뉴 탭 클릭 성공!")
    time.sleep(2)
except Exception as e:
    print(f"리파인 성수점 메뉴 연결 실패: {e}")


try:
    # 'Snack' 항목을 클릭
    food_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='Snack']]"))
    )
    food_item.click()
    print("리파인 성수점 Snack 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
except Exception as e:
    print(f"snack 항목 연결 실패: {e}")

try:
    # 'Meal' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='Meal']]"))
    )
    drink_item.click()
    print("리파인 성수점 Meal 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
except Exception as e:
    print(f"meal 항목 연결 실패: {e}")

try:
    # 'Side' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='Side']]"))
    )
    drink_item.click()
    print("리파인 성수점 Side 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
except Exception as e:
    print(f"side 항목 연결 실패: {e}")



###################스케줄 청담
driver.get("https://beta-app.catchtable.co.kr/ct/shop/schedule_cheongdam")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")  # 수직으로 50 픽셀만큼 스크롤 다운
time.sleep(1)

try:
    # '메뉴' 탭을 클릭
    menu_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='메뉴']]"))
    )
    menu_tab.click()
    print("메뉴 탭 클릭 성공!")
    time.sleep(2)
except Exception as e:
    print(f"스케줄 청담 메뉴 탭 연결 실패: {e}")


try:
    # 'Snack' 항목을 클릭
    food_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='ALL DAY 메뉴']]"))
    )
    food_item.click()
    print("스케줄 청담 ALL DAY 메뉴 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
except Exception as e:
    print(f"연결 실패: {e}")

try:
    # 'Meal' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='PIZZA 메뉴']]"))
    )
    drink_item.click()
    print("스케줄 청담 PIZZA 메뉴 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
   
except Exception as e:
    print(f"연결 실패: {e}")

try:
    # 'Side' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='BRUNCH 메뉴']]"))
    )
    drink_item.click()
    print("스케줄 청담 BRUNCH 메뉴 항목 클릭 성공!")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
    
except Exception as e:
    print(f"연결 실패: {e}")

try:
    # 'Side' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='MAIN 메뉴']]"))
    )
    drink_item.click()
    print("스케줄 청담 MAIN 메뉴 항목 클릭 성공!")
    time.sleep(2)
    
except Exception as e:
    print(f"연결 실패: {e}")

try:
    # 'Side' 항목을 클릭
    drink_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-info'][h4[@class='name']/strong[text()='NIGHT 메뉴']]"))
    )
    drink_item.click()
    print("스케줄 청담 NIGHT 메뉴 항목 클릭 성공!")
    time.sleep(2)
    
except Exception as e:
    print(f"연결 실패: {e}")

finally:
    if 'driver' in locals():
        driver.quit()