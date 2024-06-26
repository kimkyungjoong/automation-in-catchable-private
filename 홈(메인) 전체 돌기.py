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


# try:
#     # '전국' 설정 버튼 클릭
#     # 버튼의 클래스명을 사용하여 선택하여 클릭
#     location_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "button._14vgd1u3"))
#     )
#     location_button.click()

# except Exception as e:
#     print(f"전국 버튼 오류: {e}")


# try:
#     # '수도권' 링크 클릭
#     # XPath를 사용하여 '수도권' 텍스트가 있는 링크를 선택
#     su_do_gwon_link = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//ul[@class='interest_ul']/li/a[text()='수도권']"))
#     )
#     su_do_gwon_link.click()

# except Exception as e:
#     print(f"수도권 버튼 오류: {e}")


# try:
#     # '강남' 텍스트가 포함된 체크박스 클릭
#     # XPath를 사용하여 '강남' 텍스트가 있는 label 내의 체크박스를 선택
#     gangnam_checkbox = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//label[.//span[contains(text(), '강남')]]/input[@type='checkbox']"))
#     )
#     gangnam_checkbox.click()

# except Exception as e:
#     print(f"강남 오류: {e}")

# try:
#     # '관심지역 설정 완료' 버튼 클릭
#     # CSS 선택자를 사용하여 해당 클래스를 가진 버튼을 찾고 클릭
#     complete_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-red"))
#     )
#     complete_button.click()

# except Exception as e:
#     print(f"관심지역 설정 완료 오류: {e}")

###########################################  숏컷  ##################################################

try:

    # 숏컷 탐색
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".__shortcut-list-wrap .list-item")))
    
    for i in range(len(tab_links)):
        try:
            # 해당 숏컷 클릭
            link = tab_links[i]
            link_text = link.text
            link.click()
            print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")
            
            # 페이지가 로드될 때까지 대기 (예: 스크롤 이동 등)
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(0.5)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(0.5)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(0.5)
            
            # 이전 페이지로 돌아가기
            driver.back()
            print("이전 페이지로 돌아감")
            
        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
        
        # 다음 링크로 넘어가기 전에 새로운 요소들을 다시 찾기
        tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".__shortcut-list-wrap .list-item")))
    
except Exception as e:
    print(f"오류 발생: {e}")


try:
    # Safari 웹 드라이버 인스턴스 생성
    driver = webdriver.Safari()
    driver.set_window_size(1200, 1000)
    driver = webdriver.Safari(port=4444)

    # 웹 페이지 열기
    driver.get("https://beta-app.catchtable.co.kr")

    # 필요한 동작 수행
    driver.find_element_by_name("q").send_keys("selenium")
    driver.find_element_by_name("q").submit()

except WebDriverException as e:
    print(f"Safari 웹 드라이버 오류: {e}")

# 10초간 대기
time.sleep(3)



###################################### 어디로 가시나요?  ############################################
tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner a")

max_retries = 1
# 링크를 클릭하여 해당 페이지에 접근
for i in range(len(tab_links)):
    for attempt in range(max_retries):
        try:
            # 링크를 다시 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner a")
            link = tab_links[i]
            link_text = link.text  # 링크 클릭 전에 텍스트를 가져옵니다.
            link.click()
            print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")
            # 페이지가 로드될 때까지 대기하거나 다음 동작 수행
            # WebDriverWait(driver, 10).until(EC.url_to_be("원하는 URL"))
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(0.5)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(0.5)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(0.5)

            driver.back()
            break  # 성공적으로 링크를 클릭했으면 다음 링크로 이동합니다.
        except Exception as e:
            print("링크를 클릭할 수 없습니다:", e)
            print("어디로 가시나요를 종료하겠습니다.")

# 브라우저 닫기
time.sleep(3)
driver.quit()



# Safari 드라이버 초기화
driver = webdriver.Safari()

driver.set_window_size(1200, 1000)

# 웹 페이지 열기
driver.get("https://beta-app.catchtable.co.kr")

# 10초간 대기
time.sleep(2)

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




########################################### [웨이팅 핫플레이스 BEST] ####################################################
try:
    # 매장 목록 로딩 대기
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")))

    # 각 매장 클릭
    for i in range(0, 10):  # 캐테 홈에 있는 레스토랑 리스트 [웨이팅 핫플레이스 BEST]
        try:
            # 다시 매장 목록 요소 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")

            # 원하는 매장 요소 가져오기
            link = tab_links[i]
            link_text = link.find_element(By.CLASS_NAME, "name").text
            print(f"{link_text} (웨이팅 핫플레이스 BEST 매장.)")

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
            print(f"{link_text} 매장 방문 후 이전 페이지로 돌아갑니다.")

            # 다음 매장 방문 전 대기
            time.sleep(0.5)

        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
            print("탐색을 종료합니다.")
            break
        #두 번째 섹션의 전체보기 링크 클릭
    second_section_show_all_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-more")))
    second_section_show_all_link.click()
    print("두 번째 섹션의 전체보기 링크를 클릭했습니다.")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
    time.sleep(1)

    
except Exception as e:
    print("클릭을 더 이상 할 수 없습니다.:", e)

#뒤로 가기
driver.back()
time.sleep(3)





#############################################유저들의 리얼 리뷰############################################

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

#뒤로 가기
driver.back()
time.sleep(3)





########################################## [고객님이 좋아할 매장] ############################################
try:
    # 매장 목록 로딩 대기
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")))

    # 각 매장 클릭
    for i in range(11, 20):  # [고객님이 좋아할 매장]
        try:
            # 다시 매장 목록 요소 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")

            # 원하는 매장 요소 가져오기
            link = tab_links[i]
            link_text = link.find_element(By.CLASS_NAME, "name").text
            print(f"{link_text} (고객님이 좋아할 매장.)")

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
            print(f"{link_text} 매장 방문 후 이전 페이지로 돌아갑니다.")

            # 다음 매장 방문 전 대기
            time.sleep(0.5)

        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
            print("탐색을 종료합니다.")
            break
    
except Exception as e:
    print("클릭을 더 이상 할 수 없습니다.:", e)


#########000님이 좋아할 매장 
try:
    # 전체보기 버튼 목록 찾기
    show_all_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".section-header.section-header-v .btn-more"))
    )

    # 000님이 좋아할 매장 전체보기 
    if len(show_all_buttons) >= 2:
        show_all_buttons[1].click()  # 인덱스는 0부터 시작하므로 3번째는 [2]
        print("000님이 좋아할 매장 전체보기 버튼을 클릭했습니다.")
        # 매장 페이지 로딩 대기
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
    else:
        print("전체보기 버튼이 충분하지 않습니다. 총 버튼 수:", len(show_all_buttons))

    time.sleep(3)  # 전체 항목 로딩을 위해 대기

except Exception as e:
    print("전체보기 버튼을 클릭할 수 없습니다:", e)

#뒤로 가기
driver.back()
time.sleep(3)




############################################[놓치면 안되는 혜택 가득] ###############################################
try:
    # 매장 목록 로딩 대기
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")))

    # 각 매장 클릭 
    for i in range(21, 30):  # 캐테 홈에 있는 레스토랑 리스트 [놓치면 안되는 혜택 가득]
        try:
            # 다시 매장 목록 요소 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")

            # 원하는 매장 요소 가져오기
            link = tab_links[i]
            link_text = link.find_element(By.CLASS_NAME, "name").text
            print(f"{link_text} (놓치면 안되는 혜택 가득 매장.)")

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
            print(f"{link_text} 매장 방문 후 이전 페이지로 돌아갑니다.")

            # 다음 매장 방문 전 대기
            time.sleep(0.5)

        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
            print("탐색을 종료합니다.")
            break

    
except Exception as e:
    print("클릭을 더 이상 할 수 없습니다.:", e)

##놓치면 안되는 혜택 가득 전체보기 
try:
    # 전체보기 버튼 목록 찾기
    show_all_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".section-header.section-header-v .btn-more"))
    )

    # 놓치면 안되는 혜택 가득 전체보기 
    if len(show_all_buttons) >= 3:
        show_all_buttons[2].click()  # 인덱스는 0부터 시작하므로 3번째는 [2]
        print("놓치면 안되는 혜택 가득 전체보기 버튼을 클릭했습니다.")
        # 매장 페이지 로딩 대기
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
    else:
        print("전체보기 버튼이 충분하지 않습니다. 총 버튼 수:", len(show_all_buttons))

    time.sleep(3)  # 전체 항목 로딩을 위해 대기

except Exception as e:
    print("전체보기 버튼을 클릭할 수 없습니다:", e)

#뒤로 가기
driver.back()
time.sleep(3)






############################################ [캐치테이블 on] ###################################################
try:
    # 매장 목록 로딩 대기
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")))

    # 각 매장 클릭
    for i in range(31, 40):  #  [캐치테이블 on]
        try:
            # 다시 매장 목록 요소 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")

            # 원하는 매장 요소 가져오기
            link = tab_links[i]
            link_text = link.find_element(By.CLASS_NAME, "name").text
            print(f"{link_text} (캐치테이블 ON 매장.)")

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
            print(f"{link_text} 매장 방문 후 이전 페이지로 돌아갑니다.")

            # 다음 매장 방문 전 대기
            time.sleep(0.5)

        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
            print("탐색을 종료합니다.")
            break

    
except Exception as e:
    print("클릭을 더 이상 할 수 없습니다.:", e)

try:
    # 전체보기 버튼 목록 찾기
    show_all_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".section-header.section-header-v .btn-more"))
    )

    # 캐치테이블 ON 전체보기 버튼 클릭
    if len(show_all_buttons) >= 4:
        show_all_buttons[3].click()  # 인덱스는 0부터 시작하므로 3번째는 [2]
        print("캐치테이블 ON 전체보기 버튼을 클릭했습니다.")
        # 매장 페이지 로딩 대기
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
    else:
        print("전체보기 버튼이 충분하지 않습니다. 총 버튼 수:", len(show_all_buttons))

    time.sleep(3)  # 전체 항목 로딩을 위해 대기

except Exception as e:
    print("전체보기 버튼을 클릭할 수 없습니다:", e)



#######################################[미쉐린 가이드 2024] #####################################################3
try:
    # 매장 목록 로딩 대기
    tab_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")))

    # 각 매장 클릭 (두 번째 섹션, 인덱스 10부터 20까지)
    for i in range(41, 50):  # 캐테 홈에 있는 레스토랑 리스트 [미쉐린 가이드 2024]
        try:
            # 다시 매장 목록 요소 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .restaurant-list-item")

            # 원하는 매장 요소 가져오기
            link = tab_links[i]
            link_text = link.find_element(By.CLASS_NAME, "name").text
            print(f"{link_text} (미쉐린 가이드 2024 매장.)")

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
            print(f"{link_text} 매장 방문 후 이전 페이지로 돌아갑니다.")

            # 다음 매장 방문 전 대기
            time.sleep(0.5)

        except Exception as e:
            print(f"링크를 클릭할 수 없습니다: {e}")
            print("탐색을 종료합니다.")
            break


    
except Exception as e:
    print("클릭을 더 이상 할 수 없습니다.:", e)

try:
    # 전체보기 버튼 목록 찾기
    show_all_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".section-header.section-header-v .btn-more"))
    )

    # 미쉐린가이드 전체보기 버튼 클릭
    if len(show_all_buttons) >= 5:
        show_all_buttons[4].click()  # 인덱스는 0부터 시작하므로 3번째는 [2]
        print("미쉐린 가이드 전체보기 버튼을 클릭했습니다.")
        # 매장 페이지 로딩 대기
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
    else:
        print("전체보기 버튼이 충분하지 않습니다. 총 버튼 수:", len(show_all_buttons))

    time.sleep(3)  # 전체 항목 로딩을 위해 대기

except Exception as e:
    print("전체보기 버튼을 클릭할 수 없습니다:", e)
   
#뒤로 가기
driver.back()
time.sleep(3)




########################### 음식종류별 BEST  ##################################################

# tab_links 변수 정의
tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .best-food-list-item")

max_retries = 1
# 링크를 클릭하여 해당 페이지에 접근 (음식종류별 BEST)
for i in range(len(tab_links)):
    for attempt in range(max_retries):
        try:
            # 링크를 다시 찾기
            tab_links = driver.find_elements(By.CSS_SELECTOR, ".v-scroll-inner .best-food-list-item")
            link = tab_links[i]
            link_text = link.text  # 링크 클릭 전에 텍스트를 가져옵니다.
            link.click()
            print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")
            # 페이지가 로드될 때까지 대기하거나 다음 동작 수행
            # WebDriverWait(driver, 10).until(EC.url_to_be("원하는 URL"))
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
            time.sleep(1)

            driver.back()
            break  # 성공적으로 링크를 클릭했으면 다음 링크로 이동합니다.
        except Exception as e:
            print("링크를 클릭할 수 없습니다:", e)
            print("어디로 가시나요를 종료하겠습니다.")





#######################################  가격대별 BEST  ##################################################

try:
    # 탭 링크 요소 찾기
    tab_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".saved-restaurant-list .saved-restaurant-list-item"))
    )

    max_retries = 1

    # 링크를 클릭하여 해당 페이지에 접근
    for i in range(len(tab_links)):
        for attempt in range(max_retries):
            try:
                # 링크 다시 찾기
                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".saved-restaurant-list .saved-restaurant-list-item"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

                # 페이지 로드를 기다림
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

                # 스크롤 다운
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

try:
    # 탭 링크 요소 찾기
    tab_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mt-0"))
    )

    max_retries = 2

    # 링크를 클릭하여 해당 페이지에 접근
    for i in range(len(tab_links)):
        for attempt in range(max_retries):
            try:
                # 링크 다시 찾기
                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mt-0"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

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

                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mt-0"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

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
                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mt-0"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

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

                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mt-0"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 링크를 클릭하여 해당 페이지에 접근했습니다.")

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
                max_retries += 1
                print("링크를 찾고 있습니다.:", e)

except Exception as e:
    print(f"오류 발생: {e}")





#######################################  상황별 주제별 BEST  ##################################################

try:
    # 상황별 주제별 BEST 찾기
    tab_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".swiper-slide.best-list-item"))
    )

    max_retries = 1

    # 링크를 클릭하여 해당 페이지에 접근
    for i in range(len(tab_links)):
        for attempt in range(max_retries):
            try:
                # 링크 다시 찾기
                tab_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".swiper-slide.best-list-item"))
                )
                link = tab_links[i]
                link_text = link.text
                link.click()
                print(f"{link_text} 상황별 주제별 BEST 페이지에 접근했습니다.")

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




#######################################  다이닝 매거진  ##################################################

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