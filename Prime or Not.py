Number_Given=int(input("Enter the Number"))
Flag=0
for i in range(2,Number_Given-1):
    if Number_Given%i==0:
        Flag=1
if Flag==0:
    print('prime')
else:
    print('Not Prime')
