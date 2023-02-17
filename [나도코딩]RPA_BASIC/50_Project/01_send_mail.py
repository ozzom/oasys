#[신청메일 양식]
# 제목 : 파이썬 특강 신청합니다 .
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)   ex)herlock/1234

import smtplib
from email.message import EmailMessage
from account import * 
from random import * 

# nickNames = ["Iron Man", "Hulk", "Torr", "Caption America"]
nick_names = {"Iron Man":"ozzom@daum.net", "Hulk":"twmoon@glovis.net","Torr":"ozzom@daum.net", "Caption America":"twmoon@glovis.net"}

with smtplib.SMTP(SMTP_SERV, SMTP_PORT) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWD)
    
    for nick_name, email_address in nick_names.items():
        msg = EmailMessage()
        msg["Subject"]="파이썬 특강 신청합니다."
        msg["From"]=EMAIL_ADDRESS
        msg["To"]=email_address#
        content = "/".join([nick_name, str(randint(1000, 9000))])
        msg.set_content(content)
        
        smtp.send_message(msg)
        
        print(f"{nick_name} 님에게 메일 발송 완료")
        
        
        



