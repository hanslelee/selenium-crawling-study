from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("http://the-internet.herokuapp.com/upload")

driver.find_element(By.ID, "file-upload").send_keys("/Users/hssarah/PycharmProjects/test/data/test.png")


# 창 닫기
# driver.close()
