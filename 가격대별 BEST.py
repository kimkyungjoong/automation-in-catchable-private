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

driver.execute_script("window.scrollBy(0, 3280);")
time.sleep(1)

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
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(2)

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
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(2)

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
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(2)

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
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(2)

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
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(2)

                # 뒤로 가기
                driver.back()
                time.sleep(2)
                break  # 성공적으로 링크를 클릭했으면 다음 링크로 이동

            except Exception as e:
                max_retries += 1
                print("링크를 찾고 있습니다.:", e)

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    # 웹 드라이버 종료
    driver.quit()

