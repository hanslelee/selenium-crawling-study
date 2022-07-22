from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.co.kr/search?q=dogs&tbm=isch&hl=ko&tbs=il:cl&sa=X&ved=0CAAQ1vwEahcKEwiQq8jexoz5AhUAAAAAHQAAAAAQAg&biw=1145&bih=834")

for i in range(1, 11):
    driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot("data/dogs/" + str(i) + ".png")



# 창 닫기
# driver.close()
