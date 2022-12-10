Number_words=input('Enter the number to be Reversed')
string=str(Number_words)
lists=list(string)
reverse=[]
length=len(str(Number_words))
for i in range(length-1,-1,-1):
    reverse.append(lists[i])
string2=''
for i in reverse:
    string2=string2+i
print(string2)
