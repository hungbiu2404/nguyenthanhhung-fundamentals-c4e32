print('Answer the following algebra question')
print('if x=8, then what is value of 4(x+3)')
da = {
    '1':35,
    '2':36,
    '3':40,
    '4':44
}
cx = 4
for v,i in da.items():
    print(v,i)
choice = int(input('choice:'))
if choice == cx:
    print('bingo')
else:
    print(':((')

