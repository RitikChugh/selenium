from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager

browser=webdriver.Chrome(ChromeDriverManager().install())
try:
        browser.get("https://en.wikipedia.org")
        print(browser.title)
        input=browser.find_element_by_id("searchInput")
        input.send_keys("Python")
        input.send_keys(Keys.ENTER)
        wait=WebDriverWait(browser,10)
        wait.until(EC.presence_of_element_located((By.ID,"content")))
        print(browser.title)
        print(browser.get_cookies())
        print(browser.page_source)
        time.sleep(10)
finally:
        browser.close()