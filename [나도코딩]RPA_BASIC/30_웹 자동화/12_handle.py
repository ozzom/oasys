import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.window_handles  # 현재 윈도우의 핸들 정보 가져오기 임. 
print("최초로 열리는 핸들 : ", curr_handle) # 현재 윈도우 핸들 정보

# Try it yourself 
browser.find_element(By.XPATH,'//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles  
for handle in handles:
    print(handle)       # 각 핸들 정보 
    browser.switch_to.window(handle)    # 각 핸들로 브라우져 이동 
    print(browser.title)        # 출력해 보면 새로운 핸들(브라우져)의 제목 표시 
    print()
    
# 새로 이동 된 브라우져에서 뭔가 자동화 작업 수행 
# 새로 이동한 브라우져를 종료 
time.sleep(5)

print("현재 핸들 닫기", )
browser.close()

time.sleep(5)

print("Close 이후에 남은 핸들:", curr_handle)
time.sleep(5)

# 이전 핸들로 돌아오기 
print("처음 핸들로 돌아가기:", curr_handle)

time.sleep(5)

browser.switch_to.window(curr_handle)   # 내 소스는 왜 여기서 에러가 나지? 

print("돌아갔나?:", curr_handle)

print(browser.title)   # HTML input type="radio"

# 브라우져 컨트롤이 가능한지 확인 
time.sleep(5) 
browser.get("http://daum.net")

time.sleep(5)
browser.quit()

