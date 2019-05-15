sizes = [5, 7, 8, 300, 90, 50, 75]
print('Hello, my name is Hiep and these my ship sizes:')
print(*sizes, sep=',')
print('now my bigest sheep has size', max(sizes), 'let is shear it')
sizes.pop(2)
print('After shearing, here is my flock:')
print(*sizes, sep=',')


for a in range (4):
    print('month ', a+1)
    for i in range(len(sizes)):
        sizes[i] = sizes[i] + 50
    print ('One month has passed, now here is my fock:')
    print(sizes)

a = sum(sizes)
print('My flock has sizes total: ', a)
print('I would get ', a , "*2$", a*2 ,"$")