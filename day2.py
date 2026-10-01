#subscripting the string
print("hello"[0])

print("hello"[-1])

#string concatenation
print("123"+"123")

#integer=whole number
print(123+345)

#you can also use _ in larger numbers
a=10_00_000
print(a)

#float number=decimal number
b=10.00
print(b)#gives 10.0 not 10.00

#boolean
b=True
c=False

#type checking using type class
print(type("hello"))
print(type(True))
print(type(123))
print(type(1234.9345))

#type conversion
a=10
b=20
print(a+b)
print(str(a)+str(b))

#mathamtical operations
print(7-2)
print(7+2)
print(7*2)
print(10**4)
print(type(6/3))#gives floating result=2.0
print(6//3)#//gives only q result=2

print(5/3)#1.66666666666666667
print(5//3)#1

#precendence and succedenence(/,*,+,-)
# **
# * or /
# + or -
print(10+20*30)
print((10+20)*30)

## assesment-bmi calculator
weight=int(input())
height=int(input())
bmi=weight/(height**2)
print(bmi)

#usage of round function-->round function/method takes two classes round(variable,a) 
#here a represents number of digits the number needs to be rounded after decimal
bmi=34.29384789237498374
print(type(round))
print(round(bmi,3))

#shorthand operator
score=0
score+=1
print(score)

score=20
score-=10
score*=20
score/=10

#f{} strings
apples=10
bananas=20
print(f"you have{apples} apples and {bananas} bananas")

#bill calculating assessment
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_before_split=(bill+(tip/100)*bill)
bill_after_split=bill_before_split/people
print(f"your bill is per each person is going to be {round(bill_after_split,2)}")







