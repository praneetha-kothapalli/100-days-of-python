# write a print statement
print("Hello World\n")

#write print statement 3 times
print("hello world!\n"*3)

#print("HEllo"#hi)------->this line gives error
#print("Hello")#hello---->this line print Hello

#print and take input from same line
print("hello "+input("what is ur name?\n"))


#values of strings can be changed
name="john"
print(name)
name="prani"
print(name)


#how to find the lenght of the string using len
name="praneetha"
length=len(name)
print("lenght of the string is "+str(length)+"\n")
#this can be done in the same line
print(len(input("what is ur name")))


#swapping the values of string using thrid variable
a="hi"
b="bye"
print(a,b)
c=a;
a=b;
b=c;
print(a,b)

#rules of creating a variable
#a_1 is valid
#1_1 is not valid
#any special characters or any spaces or key words are not to be used