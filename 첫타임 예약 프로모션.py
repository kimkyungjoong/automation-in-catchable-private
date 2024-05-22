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
    # 팝업이 있을 경우, 닫기
    alert = driver.switch_to.alert
    alert.dismiss()
    print("팝업을 닫았습니다.")
except:
    print("팝업이 없습니다.")




repeat_count = 10

for _ in range(repeat_count):

##############산청 숯불 가든 을지로##############산청 숯불 가든 을지로##############산청 숯불 가든 을지로##############산청 숯불 가든 을지로##############산청 숯불 가든 을지로
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/sancheong_ej")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(3)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(3)

        #6/19로 날짜변경
        date_to_select = "수요일, 6월 19, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()


        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '6'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(3)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(3)




    except Exception as e:
        print(f"산청 숯불 가든 을지로  오류: {e}")






##############금돼지 식당###########금돼지 식당###########금돼지 식당###########금돼지 식당###########금돼지 식당###########금돼지 식당 

    driver.get("https://beta-app.catchtable.co.kr/ct/shop/Goldpig")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(3)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(3)

        #6/15로 날짜변경
        date_to_select = "토요일, 6월 15, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()

        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '5'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(3)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(3)




    except Exception as e:
        print(f"금돼지 식당 오류: {e}")







#############안주마을########3#########안주마을########3#########안주마을########3#########안주마을########3#########안주마을########3
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/amjoomaeul")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(3)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(3)

        #6/10로 날짜변경
        date_to_select = "월요일, 6월 10, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()

        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(3)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(3)




    except Exception as e:
        print(f"안주마을 오류: {e}")







########################쯔루하시 후게츠 명동점#################쯔루하시 후게츠 명동점#################쯔루하시 후게츠 명동점#################쯔루하시 후게츠 명동점
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/fugetsu")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(3)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(3)

        #6/19로 날짜변경
        date_to_select = "일요일, 6월 30, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()
        time.sleep(1)

        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(3)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(3)




    except Exception as e:
        print(f"쯔루하시 오류: {e}")





###################고도식#############고도식#############고도식#############고도식#############고도식#############고도식
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/godosik_songpa")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(3)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(3)

        #6/19로 날짜변경
        date_to_select = "토요일, 6월 29, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()
        time.sleep(1)

        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(3)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(3)


    except Exception as e:
        print(f"고도식 오류: {e}")




########################## 우정 양곱창#################### 우정 양곱창#################### 우정 양곱창#################### 우정 양곱창#################### 우정 양곱창
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/woojung")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(1)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(1)

        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(1)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(1)


    except Exception as e:
        print(f"우정 양곱창 오류: {e}")



#####################꿉당신사###############꿉당신사###############꿉당신사###############꿉당신사###############꿉당신사###############꿉당신사
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/ggupdang_sinsa")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(1)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(1)

        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(1)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(1)


    except Exception as e:
        print(f"꿉당 신사 오류: {e}")



#####################숙성도 판교점##############숙성도 판교점##############숙성도 판교점##############숙성도 판교점##############숙성도 판교점##############숙성도 판교점
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/suksungdo_pg?type=VISIT_RESERVATION")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(1)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(1)

         #6/19로 날짜변경
        date_to_select = "월요일, 6월 17, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()
        time.sleep(1)


        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(1)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(3)


    except Exception as e:
        print(f"숙성도 판교점 오류: {e}")



#################쌤쌤쌤##############쌤쌤쌤##############쌤쌤쌤##############쌤쌤쌤##############쌤쌤쌤
    driver.get("https://beta-app.catchtable.co.kr/ct/shop/samsamsam_kr")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 800);")

    try:
        # 
        # 예약 클릭
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ce8v0l1"))
        ).click()
        time.sleep(1)

        # 예약 일시 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mb-8"))
        ).click()
        time.sleep(1)

         #6/27로 날짜변경
        date_to_select = "목요일, 6월 27, 2024"
        date_element_xpath = f"//div[@aria-label='{date_to_select}']"

        # 요소가 클릭 가능할 때까지 대기 후 클릭
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
        date_element.click()
        time.sleep(1)


        # 두 번째 버튼 클릭 (클래스 이름: mb-8)
        target_value = '4'  # 이 값을 변경하여 다른 요소를 선택할 수 있습니다.
        xpath_expression = f"//div[contains(@class, 'swiper-slide')]//input[@type='radio'][@value='{target_value}']/ancestor::div[contains(@class, 'swiper-slide')]"

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        element.click()
        time.sleep(1)


        # 지도 닫기 버튼 클릭 (클래스 이름: mb-8)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-group"))
        ).click()
        time.sleep(1)


    except Exception as e:
        print(f"쌤쌤쌤 오류: {e}")



    
driver.quit()