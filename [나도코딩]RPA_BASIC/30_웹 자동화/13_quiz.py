import time 
from selenium import webdriver
from selenium. webdriver.common.by import By   # 이 스크리

browser = webdriver.Chrome()
browser.maximize_window() 

# 1. https://www.w3schools.com 접속
browser.get('https://www.w3schools.com')

# 2. 화면 중간 LEARN HTML  클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
time.sleep(1)

# 3. 상단 메뉴 중 HOW To 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div/a[10]').click()
time.sleep(1)

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭 - 좌표 정보를 활용해서 Scroll 이동 
# location_once_scrolled_into_view  좌표 값까지 스크롤 하라는 건데.. 굳이 없어도 되지만 학습을 위해 입력함. 
time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/a[117]') 
# 일부 텍스트가 같은 경우 발생을 대비해서 아래 코드가 가장 좋다고 할 수 있는데,,,,, 왜 작동을 안할까? 
# elem = browser.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]') 
# 일부 텍스트 비교하는 방법 
# elem = browser.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/a[contains(text(),"Contact Form")]') 

elem.click() 

# 5. 입력란에 아래 값 입력 
#     First Name : PAUL 
#     Last Name : MOON
#     Country : USA
#     Subject : 퀴즈 완료 
f_name = 'PAUL'
l_name = 'MOON'
cntry = 'USA'
subj = '퀴즈완료'

browser.find_element(By.XPATH,'//*[@id="fname"]').send_keys(f_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(l_name)
browser.find_element(By.XPATH, '//*[@id="country"]/option[3]').click()
# browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]').format(cntry).click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subj)

# 6. 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
browser.find_element(By.XPATH , '//*[@id="main"]/div[3]/a').click() 

# 7. 5초 대기 후 브라우져 종료     
time.sleep(5)
browser.quit()
