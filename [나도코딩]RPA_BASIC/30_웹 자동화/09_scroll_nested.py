# 페이지 내 특정 영역 스크롤 해야 할 경우 
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
url = 'https://www.w3schools.com/html/'
browser.get(url)

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 스크롤 방법 
# 1. ActionChain  : elem가 윈도우 맨 아래에 보이는 위치까지 스크롤
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 2.좌표 정보 이용 
xy = elem.location_once_scrolled_into_view  # 함수가 아니고 elem가 위치하고 있는 좌표 정보 return  
print("type :", type(xy))
print("value : ", xy )

elem.click()

time.sleep(5)
browser.quit()

