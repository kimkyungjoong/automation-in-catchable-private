from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# 웨이팅 top
driver.get("https://beta-app.catchtable.co.kr/ct/search/rank/waiting")

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_1hmjc2f6")))
    for element in elements:
        element.click()
        print("요소를 클릭했습니다.")

        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 50 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 100 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("클릭할 요소를 찾을 수 없거나 클릭할 수 없습니다:", e)




# 3월의 트렌드
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/240304_trend_3?uniqueListId=1711585743401")

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_1fnvqs02")))
    for element in elements:
        element.click()
        print("첫 번째 요소를 클릭했습니다.")

        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 1800 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("첫 번째 요소를 클릭할 수 없습니다:", e)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g4")))
    for element in elements:
        element.click()
        print("두 번째 요소를 클릭했습니다.")
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("두 번째 요소를 클릭할 수 없습니다:", e)

#필터 탐색기
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_14v8myn3")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(1)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)







# 3월 히든플레이스
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/event_240318_hidden?uniqueListId=1711587862460")

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_1fnvqs02")))
    for element in elements:
        element.click()
        print("첫 번째 요소를 클릭했습니다.")

        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 1800 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("첫 번째 요소를 클릭할 수 없습니다:", e)

for _ in range(5):
    driver.execute_script("window.scrollBy(0, 700);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)







#밀키트
driver.get("https://beta-app.catchtable.co.kr/ct/search/list/meal-kit")
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "h07s511")))
    for element in elements:
        element.click()
        print("첫 번째 요소를 클릭했습니다.")

        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 1800 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("첫 번째 요소를 클릭할 수 없습니다:", e)





# 웨이팅 맛집 예약 오픈
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/240325_waiting2?uniqueListId=1711604670415A")

for _ in range(4):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 1800 픽셀만큼 스크롤 다운
    time.sleep(1)

# 지역 리스트 생성
region_class_names = ["_14v8myn2"]

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g2")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#국가, 한우 오마카세 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g2z9or2")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)



# 스시 오마카세
driver.get("https://beta-app.catchtable.co.kr/ct/search/list?foodKindCodes=E_73&isMinPriceSet=false&isMaxPriceSet=false&minPrice=0&maxPrice=400000&isUsePrice=false&foodKind=E_73&uniqueListId=1711604815377")
# design_system_1mb4yfk0 design_system_jg3o1w1d design_system_1mb4yfk2"><span>스시오마카세</span></button>

for _ in range(4):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 1800 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)

# region_class_names = ["_14v8myn2"]

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g4")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)




# 우마카세
driver.get("https://beta-app.catchtable.co.kr/ct/search/list?foodKindCodes=E_72&isMinPriceSet=false&isMaxPriceSet=false&minPrice=0&maxPrice=400000&isUsePrice=false&foodKind=E_72&uniqueListId=1711622018509")


for _ in range(3):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
  

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)

# 지역 리스트 생성
#region_class_names = ["_14v8myn2"]

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g4")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#국가, 한우 오마카세 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g2z9or2")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)


# 온라인 웨이팅 바로가기 
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/231208_waiting11?uniqueListId=1711693868682")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
  

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


# 지역 리스트 생성
region_class_names = ["_14v8myn2"]

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g4")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#국가, 한우 오마카세 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g2z9or3")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1);")  # 수직으로 1 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)





# 이 달의 맛집(이 달의 레스토랑)
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/240201_monthly_3?uniqueListId=1711694057101")


for _ in range(3):
    driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 700);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
  

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1800);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)

# 지역 리스트 생성
region_class_names = ["_14v8myn2"]

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g4")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#국가, 한우 오마카세 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g2z9or2")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)


#호텔 
driver.get("https://app.catchtable.co.kr/ct/exhibition/230830_hotel?uniqueListId=1711707790315")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list__tab-menu")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)



#와인 배송
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/240201_winedelivery?tabIndex=0&uniqueListId=1711700171010")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list__tab-menu")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#모임 예약
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/group_reservation?tabIndex=0&uniqueListId=1711700276787")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list__tab-menu")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)



#신규 미식 스팟
driver.get("https://beta-app.catchtable.co.kr/ct/exhibition/240201_newrestaurant?uniqueListId=1711700413090")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("내 주변을 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("내 주변을 클릭할 수 없습니다:", e)


# 지역 리스트 생성

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g2")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#국가, 한우 오마카세 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g2z9or2")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1);")  # 수직으로 1 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)




# 케이크
driver.get("https://app.catchtable.co.kr/ct/search/list/pickup?showTabs=false&location=&uniqueListId=1711702115792")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("내 주변을 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("내 주변을 클릭할 수 없습니다:", e)


# 지역 리스트 생성

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g2")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j2")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#가격 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_14v8myn6")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(2)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1);")  # 수직으로 1 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)






# 2월 저장 top 30
driver.get("https://app.catchtable.co.kr/ct/exhibition/240301_savingtop?uniqueListId=1711702819754")


for _ in range(2):
    driver.execute_script("window.scrollBy(0, 10);")  # 수직으로 10 픽셀만큼 스크롤 다운
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 2500);")  # 수직으로 1000 픽셀만큼 스크롤 다운
    time.sleep(1)

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-wrapper")))
    for element in elements:
        element.click()
        print("내 주변을 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("내 주변을 클릭할 수 없습니다:", e)


# 지역 리스트 생성

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "speb4g3")))
    for element in elements:
        element.click()
        print("네 번째 요소를 클릭했습니다.")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 50);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1500);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("네 번째 요소를 클릭할 수 없습니다:", e)


#지역 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fldt7j0")))
    for element in elements:
        element.click()
        print("지역 필터를 클릭했습니다.")
        time.sleep(1)

except Exception as e:
    print("지역 필터 요소를 클릭할 수 없습니다:", e)

#필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g2z9or2")))
    for element in elements:
        element.click()
        print("국가 필터 요소를 클릭했습니다.")
        time.sleep(1)

except Exception as e:
    print("국가 필터 요소를 클릭할 수 없습니다:", e)

#가격 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_14v8myn6")))
    for element in elements:
        element.click()
        print("가격 요소를 클릭했습니다.")
        time.sleep(1)

except Exception as e:
    print("가격 요소를 클릭할 수 없습니다:", e)

#결과 필터
try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "design_system_v22bhw3")))
    for element in elements:
        element.click()
        print("결과 보기 요소를 클릭했습니다.")
        time.sleep(2)
        # 스크롤 다운
        driver.execute_script("window.scrollBy(0, 1);")  # 수직으로 1 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 1000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 2000);")  # 수직으로 10 픽셀만큼 스크롤 다운
        time.sleep(1)

except Exception as e:
    print("결과 보기 요소를 클릭할 수 없습니다:", e)



# 브라우저를 종료하지 않고 대기
input("Press Enter to close the browser...")  # Enter 키를 누를 때까지 대기
driver.quit
