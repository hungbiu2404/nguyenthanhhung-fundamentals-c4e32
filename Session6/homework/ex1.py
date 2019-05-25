import requests
import bs4
import pyexcel

# Lấy html từ trang 
data = requests.get('https://www.apple.com/itunes/charts/songs/') 
html = data.content.decode()
soup = bs4.BeautifulSoup(html, "html.parser")
bxh100 = soup.find("section",{"class":"section chart-grid"}).find_all("li")
tonghop = []

for i in bxh100:
    dsbaihat = {}
    dsbaihat ['xếp hạng'] = i.strong.text
    dsbaihat ['Tên Bài Hát'] = i.h3.text
    dsbaihat ['Singer'] = i.h4.text
    tonghop.append(dsbaihat)

for v in tonghop:
    print(v['xếp hạng'],":",v['Tên Bài Hát'],"of",v['Singer'])

pyexcel.save_as(records=tonghop, dest_file_name="Itunes top songs.xlsx")
