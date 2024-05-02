from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
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

driver.execute_script("window.scrollBy(0, 4380);")
time.sleep(1)


try:
    # label 요소들 선택
    labels = driver.find_elements(By.CSS_SELECTOR, ".swiper-slide a.__active")
    
    # 각 label에 대해 반복
    for label in labels:
        label_text = label.text

        # label 클릭
        label.click()
        print(f"{label_text} 라벨을 클릭했습니다.")

        # 대기 시간 추가 (요소가 로드될 때까지 대기)
        time.sleep(2)  # 페이지가 완전히 로드될 때까지 대기

        # article 요소들 다시 선택
        articles = driver.find_elements(By.CSS_SELECTOR, "article.restaurant-list-item")

        # 각 article 요소 클릭 후 뒤로 가기
        for i in range(len(articles)):
            try:
                # article 다시 찾기
                articles = driver.find_elements(By.CSS_SELECTOR, "article.restaurant-list-item")
                article_text = articles[i].find_element(By.CSS_SELECTOR, "h3.name").text
                articles[i].click()
                print(f"{article_text} article을 클릭했습니다.")

                # 스크롤 다운
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(2)

                # 뒤로 가기
                driver.back()
                time.sleep(2)  # 페이지가 로드될 때까지 충분한 대기

            except StaleElementReferenceException:
                print("StaleElementReferenceException 발생: 요소가 더 이상 존재하지 않습니다.")
                continue  # 다음 article로 넘어가기
            except NoSuchElementException:
                print("NoSuchElementException 발생: 요소를 찾을 수 없습니다.")
                continue  # 다음 article로 넘어가기

        # 다음 label 클릭을 위해 뒤로 가기
        driver.back()
        time.sleep(2)  # 페이지가 로드될 때까지 충분한 대기

        # mt-30 버튼 클릭
        mt_30_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mt-30"))
        )
        mt_30_button.click()
        print("레스토랑 전체보기 버튼을 클릭하여 다음 작업을 수행합니다.")
        time.sleep(3)  # 페이지가 로드될 때까지 대기
        driver.back()
        time.sleep(2)

        next_active_area = label.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'swiper-slide')]/span.__label")
        next_active_area.click()
        print("다음 영역으로 이동했습니다.")
        time.sleep(2)  # 페이지가 로드될 때까지 대기


except Exception as e:
    print(f"오류 발생: {e}")

finally:
    # WebDriver 종료
    driver.quit()
