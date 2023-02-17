from openpyxl import load_workbook

f = "5_cell_range_modified.xlsx"
wb = load_workbook(f)
ws = wb.active

ws.insert_rows(8)   # 8번째에 행을 하나 삽입
ws.insert_rows(8, 5)# 8번째 행부터 5 줄 삽입하기 

wb.save("7_insert_rows.xlsx")
wb.save("7_insert_rows.xlsx.dprtpf")


ws.insert_cols(2)   # B번째 열에 새로운 열이 추가
ws.insert_cols(2, 3) # B번째 열에 3개의 열 추가
wb.save("7_insert_cols.xlsx")
wb.save("7_insert_cols.xlsx.dprtpf")

