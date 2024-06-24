from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pandas as pd

import time

options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
options.add_argument("user-agent=" + user_agent)
options.add_argument("headless")
options.add_argument("lang=ko_KR")
options.add_argument("window-size=1920x1080")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)


driver.get("https://www.naver.com")

serch_box = driver.find_element(By.NAME, "query")
serch_box.send_keys("파이썬")
serch_box.submit()

driver.save_screenshot("naver2.png")

driver.quit()
