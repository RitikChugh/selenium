from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
email=driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('em')
password=driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('pp')
loginbutton=driver.find_element_by_xpath('//*[@id="u_0_b"]')
loginbutton.click()
#messenger=driver.find_element_by_xpath('//*[@id="js_87"]/div')
#messenger.click()
ritik=driver.find_element_by_xpath('//*[@id="cch_fccfbfe5513e64"]/div/div/div[2]/div/div/div/div//*[@id="placeholder-73o7d"]')
ritik.send_keys('hi')