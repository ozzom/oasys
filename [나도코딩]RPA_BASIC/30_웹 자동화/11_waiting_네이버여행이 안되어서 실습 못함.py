import time 
from selenium import webdriver

option = webdriver.ChromeOptions()
option.headless = True

browser = webdriver.Chrome()

url = 'https://m-flight.naver.com'
browser.get(url)   #url로 이동 

# 가는 날 
elem1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').clcik()
# browser.find_element_by_link_text('가는날 선택').click()
#browser.find_elements_by_link_text('17')[0].click()       # 30 일이 두개 나올 수 있으니...두개 중 첫번째 선택 
print(type(elem1))
print("elem1 value :", elem1)

# # 오는 날 
# #//*[@id="__next"]/div/div[1]/div[3]/div/div[1]/div/div/div/div[2]/div[2]/button[2]

# browser.find_element_by_link_text('오는날 선택').click()
# browser.find_elements_by_link_text('30')[0].click()       # 30 일이 두개 나올 수 있으니...두개 중 첫번째 선택 
 

# # 괌 클릭 
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[7]/div/ul/li[1]/button')

# #항공권 검색 클릭 
# browser.find_element_by_text('항공권 검색').click()

# time.sleep(5)
# browser.quit()  

