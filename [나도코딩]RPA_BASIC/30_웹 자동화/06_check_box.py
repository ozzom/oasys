from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

browser = webdriver.Chrome()
url = 'https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_display_checkbox_text'
browser.get(url)
browser.switch_to.frame("iframeResult")

# elem = browser.find_element_by_xpath('//*[@id="myCheck"]') 
# elem = browser.find_element(By.XPATH, '//*[@id="myCheck"]')  # from selenium.webdriver.common import By 를 이용한 접근 
elem = browser.find_element(By.ID, "myCheck")

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안함 ")

time.sleep(5)  

# if elem.is_selected() == True:
#     print("선택 되어 있으면 선택 취소하기")
#     elem.click()
# else:
#     print("선택 취소되었으므로 아무것도 안함")

browser.quit()
browser.close()
