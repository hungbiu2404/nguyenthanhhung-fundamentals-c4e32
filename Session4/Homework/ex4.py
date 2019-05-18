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


print("Estimate this answer (exact calculation not needed):")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
ds = {
    '1': 'About 55',
    '2': 'About 65',
    '3': 'About 75',
    '4': 'About 85'
}
da = 2
for v,i in ds.items():
    print(v,i)
choice = int(input('choice:'))
if choice == da:
    print('bingo')
    da +=1
else:
    print(':((')
print("You correctly answer",da,"out of 2 questions")