cc = float(input('nhap so cc:'))
cn = int(input('nhap so cn:'))
bmi = cn / (cc*cc)

if bmi < 16:
    print('thieu can nang')

if bmi > 16:
    if bmi < 18.5:
        print('thieu can')

if bmi > 18.5:
    if bmi < 25:
        print('binh thuong')

if bmi > 25:
    if bmi < 30:
        print('thua can')
else: 
    print('beo phi')


