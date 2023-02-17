from openpyxl import load_workbook
wb = load_workbook("7_insert_cols.xlsx")
ws = wb.active

ws.delete_rows(8)       #8행 삭제 
ws.delete_rows(8, 5)     #8행부터 5개 행 삭제 

ws.delete_cols(2)        #B열 삭제 
ws.delete_cols(2, 3)     #B열로 부터 3개의 열 삭제            

wb.save("7_deleted_cols_rows.xlsx")
