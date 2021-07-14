from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

PATH = '/Users/kenny/Downloads/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('http://localhost:3000/submit')

time.sleep(1)

send = driver.find_element_by_xpath("//*[@type='submit'][@value='Upload']")
driver.execute_script("arguments[0].click();", send)

time.sleep(3)
driver.close()