# 수강 대상을 선정하는 메일 
# 선정 기준 : 메일 수신 시간 기준 선착순 1명 
# 제목 : 파이썬 특강 신청합니다 .
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)   ex)herlock/1234
from account import * 
from imap_tools import MailBox

applicant_list = []

with MailBox(IMAP_SERV, IMAP_PORT).login(EMAIL_ADDRESS, EMAIL_PASSWD, initial_folder="INBOX") as mailbox: 
    # TEXT가 "파이썬 특강 신청" 중이고 시간이 가장 빠른 대상을 Filtering 해서 이메일에 저장 
    # 저장 순서 : 이름/메일주소/전화번호 
    for index, msg in enumerate(mailbox.fetch('SINCE 17-NOV-2021')):
        if "파이썬 특강" in msg.subject:
            # 네이버 메일은 Text를 찾으면 전부 다 가져 오게 되어있음. 
            # glovis.net은 reply 내용이 다 오고, hanmail 은 text 내용이 들어 있지 않음. 
            nick_name, phone = msg.text[:30].replace('\r\n','').split("/")
            # applicant_list.append((msg, index, nick_name, phone[:3]))
            print("{}번 도착, 닉네임 : {}, 전화번호 : {} ".format(index, nick_name, phone))

for applicant in applicant_list:
    print(applicant)
            
            
    
 