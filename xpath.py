from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.co.kr/")

# 구글에서 검색
driver.find_element(By.NAME, "q").send_keys("IT 최신 기술")

# 엔터
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

# xpath 사용해서 뉴스창 들어가기
driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[3]/a').click()


# 창 닫기
# driver.close()
