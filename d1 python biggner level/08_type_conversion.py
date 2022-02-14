x=10
y=10.2
z="hello"
print(type(x))#int
print(type(y))#float
print(type(z))#str
x=x*y
print(type(x)) #kisi num ko float num k sath multiply karain to class float ho jae gi

#implicit type conversion ..... 
# implicit ka mean andruni tor pe us ko hm ne multiplication ya kisi bi dusre tareke se kar dia
x=x+y
print(x,"type of x:",type(x))

# #explicit type conversion 
# age=input("what is your age?  ")
# age=int(age)
# print(type(age))
# print(age,type(int(age)))

#float
# age=input("what is your age?  ")
# print(type(age))
# print(age,type(float(age))) #int dont count float numbers so give command float

#string if you want to write 18 as string then
# age=input("what is your age.?  ")
# print(type(age))
# print(age,type(str(age))) 

#name (str)
# name=input("what is your name? ")
# print(name, type(str(name)))
#name if int
name=input("what is your name? ")
print(name, type(int(name))) #to wo khta h invalid literal for int()




