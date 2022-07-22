from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.co.kr/search?q=dog&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj3vvLhvYz5AhVcmVYBHfhTDHsQ_AUoAXoECAEQBA&biw=712&bih=834&dpr=2")

driver.get_screenshot_as_file('data/test.png')

for i in range(1, 5):
    scroll_index = i * 1000
    driver.get_screenshot_as_file('data/test' + str(scroll_index) + '.png')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0," + str(scroll_index) +")")



driver.get_screenshot_as_file('data/test.png')

# 스크롤 1000만큼 내리기
driver.execute_script("window.scrollTo(0,1000)")

# 로딩위해 3초 기다리기
time.sleep(3)

driver.get_screenshot_as_file('data/test1000.png')

# 스크롤 1000만큼 내리기
driver.execute_script("window.scrollTo(0,2000)")

# 로딩위해 3초 기다리기
time.sleep(3)

driver.get_screenshot_as_file('data/test2000.png')

# 스크롤 1000만큼 내리기
driver.execute_script("window.scrollTo(0,3000)")

# 로딩위해 3초 기다리기
time.sleep(3)

driver.get_screenshot_as_file('data/test3000.png')

# 창 닫기
driver.close()
