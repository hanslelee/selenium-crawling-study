from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.co.kr/search?q=dog&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj3vvLhvYz5AhVcmVYBHfhTDHsQ_AUoAXoECAEQBA&biw=712&bih=834&dpr=2")

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img')).perform()

# 창 닫기
driver.close()
