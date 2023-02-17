# 실습 사이트 : https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download

from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 특정 폴더로 복사하기 위한 옵션 
import time

# 파일 저장을 위한 절대 경로 지정 
chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':r'D:\#900.WorkSpace\venv_Workspace'})
                                                 
# 크롬 browser 열 때, 옵션을 준다.  
browser = webdriver.Chrome(options=chrome_options)
url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download'
browser.get(url)

# frame 전환
browser.switch_to.frame("iframeResult")

# download link 클릭 -> 링크에 있는 파일을 다운로드 함. 
elem = browser.find_element_by_xpath('/html/body/p[2]/a').click()

time.sleep(5)

browser.quit()
browser.close()