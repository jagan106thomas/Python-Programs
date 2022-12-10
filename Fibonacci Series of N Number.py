num=int(input('The Range Of Number For Getting Fibonacci Series'))
fno=0
sno=1
print(fno)
print(sno)
tno=fno+sno
for i in range(num):
    print(tno)
    fno=sno
    sno=tno
    tno=fno+sno




