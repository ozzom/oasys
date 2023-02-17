from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option' 
browser.get(url)

browser.switch_to.frame('iframeResult')

time.sleep(5)

# 1. XPath를 통해서 찾는 방법
# cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택 
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
#option[1]: 첫 번째 항목 
#option[2]: 두 번째 항목 
# ... 

# 2. 텍스트 값이 완전히 일치하는  값을 통해서 찾는 방법 
# 옵션 중에서 텍스트가 Opel 인 항목을 선택 
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Opel"]')

# 3. 텍스트 값이 부분 일치하는 항목 선택 ()
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Op")]')
               
elem.click()
time.sleep(5)

browser.quit()
browser.close()






