Start_Range=int(input("Enter the Start_Range"))
End_Range=int(input("Enter the End_Range"))

Flag=0
for Range_Numbers in range(Start_Range,End_Range):
    for Div in range(2,Range_Numbers):
        if Range_Numbers%Div==0:
            Flag=1
    if Flag==0:
        print('prime',Range_Numbers)
    else:
        print('Not Prime',Range_Numbers)
    Flag=0
