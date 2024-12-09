from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹드라이버 설정 (사파리 설정으로 사이즈는1200, 1000)
driver = webdriver.Safari()
driver.set_window_size(1200, 1000)

# 웹사이트 열기
driver.get("https://beta-app.catchtable.co.kr/ct/loginPhone")  # 실제 로그인 페이지 URL로 변경
time.sleep(2)

try:
    # 1. ID 입력
    login_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-id"))
    )
    login_id.clear()
    login_id.send_keys("********")  # 아이디 입력

    # 2. 비밀번호 입력
    login_pw = driver.find_element(By.ID, "login-pw")
    login_pw.clear()
    login_pw.send_keys("********")  # 비밀번호 입력

    # 3. 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[form='login-form'][type='submit']"))
    )
    login_button.click()
    print("로그인 버튼 클릭 완료!")

    # 페이지 로딩 대기
    time.sleep(2)    

except Exception as e:
    print(f"오류 발생: {e}")


# R_QA_마침내찾아온
driver.get("https://beta-app.catchtable.co.kr/ct/shop/Y2F0Y2hfY0VybEJLRDQvdXlNdDFLbGFxcFdDQT09?type=DINING")
time.sleep(2)

try:
    # 세 번째 예약 가능 영역 선택
    third_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".q9ov9u9:nth-of-type(3)"))
    )
    # 클릭 실행
    third_element.click()
    print("세 번째 영역 클릭 성공")
    time.sleep(2)
except Exception as e:
    print(f"오류 발생: {e}")


try:
    # 세 번째 swiper-slide 선택
    third_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "._1tamkx10:nth-of-type(3) "))
    )
    # 클릭 실행
    third_element.click()
    print("세 번째 영역 클릭 성공")
    time.sleep(2)
except Exception as e:
    print(f"오류 발생: {e}")


try:
    # "확인" 버튼 선택
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-red"))
    )
    # 버튼 클릭
    confirm_button.click()
    print("확인 버튼 클릭 성공")
    time.sleep(2)
except Exception as e:
    print(f"오류 발생: {e}")


#캐치페이 팝업
try:
    # 버튼 찾기
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button._1ty9tmod._1ty9tmoe._1ltqxco26"))
    )
    # 버튼 클릭
    confirm_button.click()
    print("자동결제로 예약하기")
    time.sleep(2)

except Exception as e:
    print(f"오류 발생: {e}")


try:
    # 체크박스 요소 선택
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.c2yywn4"))
    )

    # JavaScript로 readonly 속성 제거
    driver.execute_script("arguments[0].removeAttribute('readonly');", checkbox)

    # 체크박스 클릭
    checkbox.click()
    print("체크박스 클릭 성공")
    time.sleep(2)

except Exception as e:
    print(f"오류 발생: {e}")



try:
    # "결제하기" 버튼 대기 및 클릭
    payment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button._1qh1syp7._1ltqxco27"))
    )
    payment_button.click()
    print("결제하기 버튼 클릭 성공")
    time.sleep(2)

except Exception as e:
    print(f"오류 발생: {e}")



#캐치페이 팝업
wait = WebDriverWait(driver, 10)
try:
    # 입력할 숫자 리스트 
    numbers_to_input = [1,2,3,4,5,6,7,8,9]

    for number in numbers_to_input:
        # 숫자 버튼을 CSS 선택자로 찾기
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@class='__key' and text()='{number}']"))
        )
        button.click()  # 버튼 클릭
        print(f"숫자 {number} 입력 완료")

    print("모든 숫자 입력 완료")
    time.sleep(3)

except Exception as e:
    print(f"오류 발생: {e}")


####절대 삭제 금지

# try:
#     # "다시 보지 않기" 버튼 찾기 및 클릭
#     dont_show_again_button = driver.find_element(By.CSS_SELECTOR, "button._1qn1ik44._1ltqxco21")
#     dont_show_again_button.click()
#     print("'다시 보지 않기' 버튼을 클릭했습니다.")
#     time.sleep(1.5)
# except NoSuchElementException:
#     print("'다시 보지 않기' 버튼을 찾을 수 없습니다.")


# time.sleep(1)

# #검색하기 gnb 클릭
# try:
#     # 검색 링크 클릭
#     # 'href' 속성을 사용하여 요소를 찾음
#     search_link = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/ct/search']"))
#     )
#     search_link.click()
#     time.sleep(1)

# except Exception as e:
#     print(f"An error occurred: {e}")

# time.sleep(1.5)


# #상단 app 으로 사용하라는 팝업 없애기
# try:
#     # 닫기 버튼 요소를 대기 후 선택
#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn-close"))
#     )
    
#     # 클릭 수행
#     close_button.click()
#     print("닫기 버튼을 성공적으로 클릭했습니다.")

# except NoSuchElementException:
#     print("닫기 버튼을 찾을 수 없습니다.")



# # # 팝업 노출 없애버리는 로직
# # try:
# #     # 팝업 노출 없애버리는 로직
# #     confirm_button = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.CSS_SELECTOR, "button._1080nhti._1ltqxco26"))
# #     )
# #     confirm_button.click()
# #     print("확인 버튼 클릭 완료!")

# #     time.sleep(1)
# # except TimeoutException:
# #     print("버튼을 찾지 못했습니다. 시간을 초과했습니다.")


# #검색창 클릭
# try:
#     # 요소 클릭을 위한 대기
#     clickable_element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "div._10xd4bu5"))
#     )
    
#     # 요소 클릭
#     clickable_element.click()
#     print("요소가 클릭되었습니다.")
#     time.sleep(1)
 
# except Exception as e:
#     print(f"오류 발생: {e}")


# time.sleep(1.5)

# # 매장명 리스트 (테스트용 데이터)
# store_names = ["R_QA_마침내찾아온"]

# try:
#     # 검색창 대기 및 찾기
#     for store in store_names:
#         search_box = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "input.k7k5xi6._1ltqxco1h"))
#         )
        
#         # 검색창 초기화 및 매장명 입력
#         search_box.clear()
#         search_box.send_keys(store)
#         print(f"검색어 입력: {store}")
        
#         # 검색 실행
#         search_box.send_keys(Keys.RETURN)
#         time.sleep(2)  # 검색 결과 대기  
# except Exception as e:
#     print(f"오류 발생: {e}")



finally:
    # 드라이버 종료
    driver.quit()