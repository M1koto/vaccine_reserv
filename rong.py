import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
import time

PATH = '/Users/kenny/Downloads/chromedriver'

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

driver = webdriver.Chrome(desired_capabilities=caps, executable_path=PATH)

start = time.time()
driver.set_page_load_timeout(1)
try:
    driver.get('https://www6.vghtpe.gov.tw/reg/c19vaccLine.do')
except:
    driver.close()
    sys.exit(1)

end = time.time()
print(end - start)
name = driver.find_element_by_name('linename')
name.send_keys('楊典憲')


ID = driver.find_element_by_name('lineid')
ID.send_keys('A130725557')


phone = driver.find_element_by_name('phone')
phone.send_keys('0911176217')

types = driver.find_element_by_xpath("//*[@value='MD'][@name='rdo_bank']")
driver.execute_script("arguments[0].click();", types)

flag = False
try:
    send = driver.find_element_by_xpath("//*[@type='button'][@value='送出']")
    driver.execute_script("arguments[0].click();", send)
    flag = True
except:
    pass

try:
    send = driver.find_element_by_xpath("//*[@type='button'][@value='提交']")
    driver.execute_script("arguments[0].click();", send)
    flag = True
except:
    pass

try:
    send = driver.find_element_by_xpath("//*[@type='button'][@value='submit']")
    driver.execute_script("arguments[0].click();", send)
    flag = True
except:
    pass

if flag:
    time.sleep(30)

driver.close()