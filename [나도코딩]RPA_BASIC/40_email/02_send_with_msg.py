import smtplib
from accout import *
from email.message import EmailMessage 

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"]= EMAIL_ADDRESS
msg["To"]="twmoon@glovis.net"

# 여러 사람에게 보낼 때.. 
# msg["To"]="taiwoong.moon@ggmail.com, ozzom@daum.net"
to_list = ['taiwoong.moon@ggmail.com','ozzom@daum.net','lapaula@naver.com']
msg["To"] = ",".join(to_list)


# 참조 
msg["Cc"] = "ozzom@naver.com"

# 비밀참조 
msg["BCc"] = "ozzom@naver.com"

# 메일 본문 
body = '테스트 메일입니다.'
msg.set_content(body) 

with smtplib.SMTP(SMTP_SERV, SMTP_PORT) as smtp :
    # 아래 두 줄은 항상 기본이라고 생각하면 됨. 
    # ----------------------------------------------
    smtp.ehlo()      # 연결이 잘 수립되는지 확인       
    smtp.starttls()  # 모든 내용이 암호화되어 전송     
    # --------------------------------------------
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWD)
    smtp.send_message(msg)
    
    
    
