from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("D:\\#900.WorkSpace\\venv_Workspace\\img.png")

# C3 위치에 img.png 파일의 이미지를 삽입 
ws.add_image(img, "C3")  
wb.save("sample_image.xlsx")
