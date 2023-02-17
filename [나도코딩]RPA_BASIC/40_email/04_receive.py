from imap_tools import MailBox
from accout import *

# MailBox 객체 생성 
mailbox = MailBox(IMAP_SERV, IMAP_PORT)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWD, initial_folder="INBOX")  # initial_folder 받은 폴더함, 다른 폴더인 경우는 직접 이름 입력 

# limit : 최대 메일 개수 
# reverse : 최근메일 부터 가져오면 True, False는 오래된 메일 부터 
for msg in mailbox.fetch(limit=1, reverse=True):  
    print("제목 :", msg.subject)
    print("발신자 :", msg.from_)
    print("수신자 :", msg.to)
    # print("참조자 :", msg.cc)
    # print("비밀참조자 :", msg.bcc)
    print("날짜 :", msg.date) 
    print("본문 :", msg.text.strip())
    # print("HTML 메시지", msg.html)
    # 첨부파일 다운로드
    for index, att in enumerate(msg.attachments) :
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)
        
        with open ("down_loaded_"+ att.filename, "wb") as f:
            f.write(att.payload)
            print("{}번 첨부파일 {} 다운로드 종료,  ".format(index, att.filename), end="\n")
            
    print("*"*100)
    
mailbox.logout()
    


