import smtplib
from accout import * 

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    # 아래 두 줄은 항상 기본이라고 생각하면 됨. 
    smtp.ehlo()      # 연결이 잘 수립되는지 확인       
    smtp.starttls()  # 모든 내용이 암호화되어 전송     
    
    # 로그인 하기 
    smtp.login(AOL_SERVER_ADDR, AOL_SERVER_PORT) 
    
    # 내용 작성하기 
    subject = "test mail"   #   메일 제목 
    body = "mail body"      #   메일 본문 
    
    msg = f"Subject: {subject}\n{body}"
    
    # 발신자, 수신자, 정해진 형식의 메시지 
    smtp.sendmail(AOL_EMAIL_ADDR, "ozzom@naver.com", msg)   
    
    
    