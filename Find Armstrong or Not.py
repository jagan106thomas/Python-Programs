Number=int(input("Enter the Number To Check Whether its is Armstrong or Not"))
Temp=Number
Sqaure_plus=0
while Number>0:
    Last=Number%10
    Number=Number//10
    Sqaure_plus=Sqaure_plus+(Last*Last*Last)
if Sqaure_plus==Temp:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')