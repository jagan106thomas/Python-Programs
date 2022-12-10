Num=int(input('Enter the Exact Range That a Fibonacci series Can print'))
fno=0
sno=1
print(fno)
print(sno)
tno=fno+sno
while tno<Num:
    print(tno)
    fno=sno
    sno=tno
    tno=fno+sno