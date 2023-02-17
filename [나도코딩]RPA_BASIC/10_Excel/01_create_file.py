from openpyxl import Workbook

wb = Workbook()            # 새 workbook 생성 
ws = wb.active             # 현재 활성화된 sheet를 가져옴 
ws.title = "WenTaixiong"   # sheet의 이름을 변경 
wb.save("sample.xlsx")     # 파일을 생성 
wb.close()