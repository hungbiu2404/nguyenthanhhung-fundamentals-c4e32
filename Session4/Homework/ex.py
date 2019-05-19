ds = [
    {'ten':'Trinh','tuổi':'22','toán': 2,'lý': 3,'hóa': 4,'sdt':['0123456789'],'diachi':'Lào Cai'},
    {'ten':'Chou','tuổi':'22','toán': 3,'lý': 4,'hóa': 5,'sdt':['0924459789'],'diachi':'Ninh Bình'},
    {'ten':'Trang','tuổi':'22','toán': 1,'lý': 2,'hóa': 3,'sdt':['0823445789'],'diachi':'Bắc Giang'},
    {'ten':'Chi','tuổi':'20','toán': 9,'lý': 9,'hóa': 9,'sdt':['0943456789'],'diachi':'Thanh Hóa'},
    {'ten':'Lê','tuổi':'22','toán': 0,'lý': 1,'hóa': 2,'sdt':['0163456789'],'diachi':'Cao Bằng'},
]
max_toan = 0
ten = []
for k in ds:
    if k['toán'] > max_toan:
        max_toan = k['toán']
        ten = k['ten']
print(max_toan, ten)

sdt = input('nhap sdt:')
ten = []
for i in ds:
    if sdt in i['sdt']:
        ten.append(i['ten'])
if len(ten) != 0:  
    print(*ten)
else:
    print("Không có tên và số điện thoại")
