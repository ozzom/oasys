import  smtplib
from email.message import EmailMessage
import smtplib
from accout import * 
 
msg = EmailMessage()
 
msg["To"] = "twmoon@glovis.net"
msg["From"] = EMAIL_ADDRESS
msg["Subject"] ="Python 을 이용한 첨부파일 보내기 테스트"
 
text="첨부한 파일 참고바랍니다."
msg.set_content(text)
 
# 파일 첨부
# MINE 타입
# msg에 파일 첨부하기.  
# Mine 타임 유형 : text, image, audio, video, application(모든 종류 이진 데이터) 
# 문서인 경우 text를 , 그림은 image, 음악파일은 audio, 동영상은 video, 프로그램은 application 전달 
# 참조 : https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

# 1. 그림 파일 전송 
path = f'D:\\#900.VPN\\WireGuard 설정파일\\산호세\\'
file_nm = 'ozzom.png'
file =path + file_nm
with open(file,"rb") as f :  
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=file_nm)

# 2. PDF 파일 전송     
path = f'C:\\Users\\ozzom\\Downloads\\'
file_nm = "011002100211_73086907_北京中都格罗唯视物流有限公司.pdf"
file =path + file_nm    
with open(file,"rb") as f :  
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=file_nm)

# 3. EXCEL 파일 전송
path = f'C:\\Users\\ozzom\\Downloads\\'
file_nm = "三厂服务器硬件配件价格及软件服务内容-20211116 (1).xlsx"
file =path + file_nm    
with open(file,"rb") as f :  
    msg.add_attachment(f.read(), maintype="application", subtype="xlsx", filename=file_nm)
    
      
# 메일 발송 
with smtplib.SMTP(SMTP_SERV, SMTP_PORT) as smtp :
    smtp.ehlo()        # 연결 확인 
    smtp.starttls()    # 내용 암호화 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWD) # 로그인 
    smtp.send_message(msg)





     
 