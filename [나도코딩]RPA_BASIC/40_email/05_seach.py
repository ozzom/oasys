from os import terminal_size
from typing import Sized
from imap_tools import MailBox
from account import * 
import datetime 

# 메일 박스 만들고, 로그인 하기 
# mailbox = MailBox(IMAP_SERV, IMAP_PORT)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWD, initial_folder="INBOX")
# mailbox.fetch().. 
# mailbox.logout()
# 아래 방법으로 하면 logout을 할 필요 없다. 


with MailBox(IMAP_SERV, IMAP_PORT).login(EMAIL_ADDRESS, EMAIL_PASSWD, initial_folder="INBOX") as mailbox:
    # 전체 메일 다 가져오기 
    for msg in mailbox.fetch('SINCE 17-NOV-2021') : 
        if "파이썬 특강" in msg.subject and msg.from_=="ozzom@hanmail.net" : 
            print("msg.uid : ",msg.uid)
            print("msg.subject : ",msg.subject)
            print("msg.from_ : ",msg.from_)
            print("msg.to : ",msg.to)
            print("msg.cc : ",msg.cc)
            print("msg.bcc : ",msg.bcc)
            print("msg.reply_to : ",msg.reply_to)
            print("msg.date : ",msg.date)
            print("msg.date_str : ",msg.date_str)
            print("msg.text :", msg.text.replace("\r\n","").split("/"))         # str: 'Hello 你 Привет'
            # print("msg.html : ",msg.html)
            print("msg.flags : ",msg.flags)   # tuple: ('\\Seen', '\\Flagged', 'ENCRYPTED')
            # print("msg.headers : ",msg.headers)
            print("="*100)
            
        # # 읽지 않은 메일 가져오기   
        # for msg in mailbox.fetch('(UNSEEN)') :  
        #     print("[{}, {}]".format(msg.from_, msg.subject))
            
        # 특정인이 보낸 메일 가져오기 
        # for msg in mailbox.fetch('FROM twmoon@glovis.net', limit=5, reverse=True):
        #     print("[{}, {}]".format(msg.from_, msg.subject))
        
        # 어떤 글자를 포함하는 메일 (제목, 본문)
        # TEXT="테스트","공고"  각각의 단어를 포함하는 메일 검색
        # for msg in mailbox.fetch('(TEXT="테스트")', limit=5, reverse=True ):
        #     print("[{}, {}]".format(msg.from_, msg.subject))
        # 
        # 제목에 테스트 가 포함되어 있는 메일 
        # for msg in mailbox.fetch('(SUBJECT "account")', limit=5, reverse=True):
        #    print("[{}, {}]".format(msg.from_, msg.subject))
        
        # 한글은 서비스가 안되고 있음. 
        # # 어떤 글자(한글)을 포함하는 메일 필터링(제목만) 
        # for msg in mailbox.fetch(limit=5, reverse=True):
        #     if "테스트" in msg.subject:
        #       print("[{}, {}]".format(msg.from_, msg.subject))
        
        #            
        # 특정 날짜 이후의 메일만 가져오기 
        # 날짜를 변경시켜줘야 함. 
        # 1. datetime.datetime.strptime("yyyy-mm-dd", "%Y-%m-%d")
        # 2. 변환한 날짜를 strftime("%d-%b-%Y) 로 포맷 변환 진행   %a:요일(sun, mon, tue....), %b:월(Jan, Feb, Mar,.... ) 
        # date = datetime.datetime.strptime("2020-11-01", "%Y-%m-%d")
        # for msg in mailbox.fetch('SENTSINCE {}'.format(date.strftime('%d-%b-%Y')), reverse=True , limit=1):
        #     print("[{}, {}]".format(msg.from_, msg.subject))
            
        # 특정 날짜에 발송한 메일만 가져오기 
        # date = datetime.datetime.strptime("2020-11-01", "%Y-%m-%d")
        # for msg in mailbox.fetch('ON {}'.format(date.strftime('%d-%b-%Y')), reverse=True , limit=5):
        #     print("[{}, {}]".format(msg.from_, msg.subject))                    
        
        # 2 가지 이상의 조건을 모두 만족하는 메일 → 한칸 띄우고 조건 명시 (and)
        # date = datetime.datetime.strptime("2020-11-01", "%Y-%m-%d")
        # for msg in mailbox.fetch('ON {} SUBJECT "test mail"'.format(date.strftime('%d-%b-%Y')), reverse=True , limit=5):
        #     print("[{}, {}]".format(msg.from_, msg.subject))            

        # 2 가지 조건 중 하나라도 만족하는 메일 (or 조건 )
        # date = datetime.datetime.strptime("2020-11-01", "%Y-%m-%d")
        # for msg in mailbox.fetch('OR ON {} SUBJECT "account"'.format(date.strftime('%d-%b-%Y')), reverse=True , limit=5):
        #     print("[{}, {}]".format(msg.from_, msg.subject))            
        







