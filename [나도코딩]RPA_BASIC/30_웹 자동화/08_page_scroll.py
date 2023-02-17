from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Chrome()
url = 'https://shopping.naver.com/home/p/index.naver'
browser.get(url)

# 무선마우스 입력 
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선마우스')

# 검색 버튼 클릭
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤을 한번 내리고, 얼마나 내려갔나 저장해 놓음. 
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 한번 더 실행해서 이전 높이랑 비교 
    # 높이가 같으면 끝까지 내려 간 것임. 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    curr_height = browser.execure_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
        
    prev_height = curr_height
    
# 스크롤을 맨 위로 올리기 
browser.execute_script("window.scrollTo(0, 0)")

time.sleep(3)
browser.quit()
browser.close()
 
 
 
 