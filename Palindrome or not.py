num=int(input("Enter a number to check whether the number is palindrome or not"))
temp=num
rev=0
while num>0:
    last=num%10
    num=num//10
    rev=(rev*10)+last
if rev==temp:
    print('The Number is Plaindrome')
else:
    print('The Entered Number is not a palindrome')