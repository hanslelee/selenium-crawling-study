from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://velog.io/@hssarah")

# css selector로 선택하는법
# driver.find_element(By.CSS_SELECTOR, "#root > div.sc-efQSVx.kdrjec.sc-cTAqQK.gdjBUK > div.sc-hiwPVj.dezvna.sc-fXEqDS.hmUoNK > div:nth-child(4) > div.sc-evcjhq.dAPqfe > div > div:nth-child(1) > a:nth-child(1)").click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[4]/div[3]/div/div[1]/a[1]').click()

driver.maximize_window()  # For maximizing window

# 페이지 로딩 후 요소를 찾기 위해 기다린다.
driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[8]/div/div[1]/textarea').send_keys('굳')
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[8]/div/div[1]/div/button').click()

# 너무 로봇이 하는 것 같을 수 있으니 3초정도 쉬고 다음 댓글 달기
time.sleep(3)


# 새로고침
driver.refresh()

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[8]/div/div[1]/textarea').send_keys('두번째')
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[8]/div/div[1]/div/button').click()

# 창 닫기
driver.close()
