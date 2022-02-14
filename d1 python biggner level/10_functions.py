# #print phly jese use kia y function h ..
# # function ka matlab jo chez ap write karain wo ak maqsad k teht output mai ap ko show ho jay
# print("we are learning with aammar? ") #print ak function h or call karraha h output mai y wali string ko
# print("we are learning with aammar? ")
# print("we are learning with aammar? ")
# print("we are learning with aammar? ")
# print("we are learning with aammar? ")
# print("we are learning with aammar? ")

#defining a function
# def# y aik function ko define karny k lye python ki command h
# def print_codanics #pir ap function ka koi bi name dete hn  eg print_codanics
# def print_codanics() # pr ap function ko define karny k lye parenthesis lage ge 
#1st way


# def print_codanics():
#     print("we are learning with aammar? ")
#     print("we are learning with aammar? ")
#     print("we are learning with aammar? ")

# print_codanics()

#2nd way
def print_codanics():
    text = "we are learning with aammar..? " 
    print(text)
    print(text)
    print(text)
print_codanics()
#aik line mai change karainge to sari lines ,mai changes ho jae gi eg ammar k bd youtube agaradd karain
def print_codanics():
    text = "we are learning with aammar youtube ..? " 
    print(text)
    print(text)
    print(text)
print_codanics()

#3rd way
def print_codanics(text):
        print(text)
        print(text)
        print(text)

print_codanics("we are ")

#defining a function with if,elif, else stament
#hm ne school education ka aik calculator bananna h 
def school_calculator(age,text):
    if age==5:
        print("hammad can join the school.")
    elif age>5:
        print("hammad should go to higher school")
    else:
        print("hammad is still a baby!")
school_calculator(5,"hammad")

#if age 15 likhain then 
def school_calculator(age,text):
    if age==5:
        print("hammad can join the school.")
    elif age>5:
        print("hammad should go to higher school")
    else:
        print("hammad is still a baby!")
school_calculator(15,"hammad")

#if age 2 year
def school_calculator(age,text):
    if age==5:
        print("hammad can join the school.")
    elif age>5:
        print("hammad should go to higher school")
    else:
        print("hammad is still a baby!")
school_calculator(2,"hammad")

#agar sirf age likhain ar text na likhain
def school_calculator(age):
    if age==5:
        print("hammad can join the school.")
    elif age>5:
        print("hammad should go to higher school")
    else:
        print("hammad is still a baby....!")
school_calculator(2)

#defining a function of future
def future_age(age): 
    new_age=age+20
    return new_age
    print(new_age)
future_predicted_age= future_age(18)
print(future_predicted_age)

