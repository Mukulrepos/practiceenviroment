import sys

# p1 a program enter string and display hello with name

# name = str(input("enter the name : "))
# print(name+" hello.. ")

# p2 accept chaharacter as a string
# character = input("enter the character")
# print("u entered is "+character)


# p3 accept only sigle character
# cahr = input("enter the characteres")
# print("u can enter character :"+cahr[0])

# p4 accept the inetergers

# integers = input("enter the integers :")
# print("u entered is :"+integers)


# p5 entered the integer convert into float
# itn =input("entered the  numebr ")
# x = float(itn)
# print(x)


# p6 enter two integers if u want to display it
# x = int(input("enter  the number 1 "))
# y = int(input("entered  the numebr 2"))

# print("u entered the number is ",x,y)

# p7 enter the number fimd there sum
# x = int(input("enter  the number 1 "))
# y = int(input("entered  the numebr 2"))
# sum = x+y
# print("Sum is:> ",sum)

# p8 sum of two number and their products
# x = int(input("enter  the number 1 "))
# y = int(input("entered  the numebr 2"))
# sum   = x+y
# product = x*y
# print("SUM IS :-> ",sum)
# print("Product is :->",product)

# p9 enter the number system is octal decimal biany and hexadecimal
# Converting hexadecimal to decimal
# strs = input("Enter the hexadecimal number:-> ")
# x = int(strs, 16)
# print("Hexadecimal to decimal is :=> ", x)

# # Converting octal to decimal
# strs = input("Enter the octal number:-> ")
# x = int(strs, 8)
# print("Octal to decimal is :=> ", x)

# # Converting binary to decimal
# strs = input("Enter the binary number:-> ")
# x = int(strs, 2)
# print("Binary to decimal is :=> ", x)

# p10enter the number in same line
# a ,b,c =[int (x) for x in input("enter three numbers ").split(',')]
# print("value added is ",a+b+c)


# p11 enter the numebr of three stringd
# lst =[x for x in input("enter the string is :").split(',')]
# print("you entered is:\n ",lst)

# p12 enter the numberfor evaluation
# a,b =5,10
# x=eval("a+b-4")
# print(x)


# p13 accept a list  eval
# lst = eval(input("enter a list:"))
# print("List :->",lst)

# p14 display command line arguments

# import sys
# n=len(sys.argv)
# args=sys.argv
# print("no of command  line argumanemts",n)
# print("the argumntnent",args)
# print("the args one by one")
# for a in args:
#     print(a)


# p15 find sum of two numbers using


# Convert command line arguments to integers and sum them
# sum = int(sys.argv[1]) + int(sys.argv[2])

# # Print the result
# print("sum =", sum)


args = sys.argv[1:]
print(args)

sum = 0
for a in args:
    x=int(a)
    if x%2==0:
        sum+=x
print(sum)