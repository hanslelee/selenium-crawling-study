from selenium import webdriver
from selenium.webdriver.common.by import By

# /Users/hssarah/PycharmProjects/test/chromedriver <= 이거 이름임
driver = webdriver.Chrome("./chromedriver")

# 크롬웹드라이버가 네이버 로그인창띄움
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# 아이디 요소 가져와서 인풋에 넣어봄
driver.find_element(By.ID, "id").send_keys("룰루")