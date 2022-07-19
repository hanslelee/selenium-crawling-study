from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")

driver.get("https://pann.nate.com/")

# 뉴스, 연예를 띄워봄
driver.find_element(By.CLASS_NAME, "svc1").click()
driver.find_element(By.CLASS_NAME, "svc2").click()

# 창 닫기
driver.close()
