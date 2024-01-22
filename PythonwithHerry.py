#Assignment Operators
a = 4
a += 2
the output will be 6 because we added similar variables by +
we can do -, / , * , % , // , ** 

#comparison Operators- for comparing the values
x = 8
y = 3
z = 8
print(x>y)
the output will be true becouse its true for the respetive value
similarly
print(x<y)
"!=" means "not is equal to"
print(x!=y)
output will be true because x and y are not equal
print(x==z)
output will be true because x and z are equal
"==" is used for comparing value in python whether "=" is used for 
assigning a value

#Logical Operators
x = 8
y = 3
z = 8
print(x==z and x<y)# and is a logical operator
output will be false because x<y is false

print(x==z or x<y)# or is a LO
output will be true one of them is true

we can reverse the argument by using LO- not
print(not(false))
output will be true
Print(not(true))
output will be false


#strings and strigs mathods
name='abutareeq'
print=(name.count("t"))# to find word in string 
#output-t,,,because t is in the string

print(name.isalnum())# it is used to check that the string is alpha numric

#INPUT=input is a function which is used for get an output in which we can enter some information
name = input("Enter your name:  ")
print(name)
#you should try input once you like it. remamber one thing the input function always take your argument as a string so you have to change string into integer 
#ex--write a python program to take a number from user as an input form the user and add 6 to it
num = input("enter a number:  ")
print(type(num))
print(int(num)+6)
#output--enter a number:  3
<class 'str'>
9

#List and List Mathods
# in pythone, we can use list[] to store maltiple value or data in a variable. we can use list by using--[].
# bbanefits of making list in python we can store data in a variable for ex
L1 = [1,2,6,4,5,3,]
print(type(L1))
print(L1)
#output-<class 'list'>
#      [1, 2, 6, 4, 5, 3]

#Differnce between String & List is we cannot modified strings if u want change in any string python will be write your code from the beginnig for example- if u want 
#to capitalised then u have to give a whole code "print(x.capitalise()) after that it will work. but in list we can modify our entire data by giving simple command. for example if u want
#to remove some thing form list u have to give remove command.
L1.remove(5)
print(L1)
#output--[1, 2, 6, 4, 3]
L1.sort()
print(L1)
#output--[1,2,3.4,6]#sort in acsending oreder
L1.pop()
print(L1)
#output--[1,2,3,4]#pop commant remove the last num or string or variable
L1.append(76)
print(L1)
#output--[1,2,3,4,76]#appned command add anything in list
L1.extend([7,8,9,10])
print(L1)
#output--[1, 2, 3, 4, 76, 7, 8, 9, 10]


"""Tuple and Tuple mathod"""
#u already learnt it

"""SETS & SETS MATHODES"""
"""sets are denote by { }. sets can be modified. set count a value only once ex-"""
a1 = {1,2,3,45,3,3,3}
print(type(a1))
print(a1)
#output--<class 'set'>
               #{1, 2, 3, 45}

a1.clear()#it clear the set
print(a1)#OUTPUT-set()
print(a2)
#a1.pop()#last element of set will removed and return a random value as a output

"""Dictionaries and mathods"""
#dictionaries denotes by { }. dictionary is changeable, mutable. in dictionaries u can fetch the value of given keys ie.. {"keys":values}.. Ex--
'''
marks = {"abu":9,"muzammil":5,'faizan':5,"Vasefa":8,'indris':4,'mubashera':7,'iram':6,'saeed':5}
print(marks["abu"])#output-9
print(marks['iram'])#output-6
marks["Alhumd"]=8 #add in dictionary
print(marks)'''
#output-{'abu': 9, 'muzammil': 5, 'faizan': 5, 'Vasefa': 8, 'indris': 4, 'mubashera': 7, 'iram': 6, 'saeed': 5, 'Alhumd': 8}

print(marks.get('iram'))#output-6
#we can get perticuler marks by using both 'print(marks['iram']) & 'print(marks.get('iram')). but the difference is we
# dont use inbuilt get function and make a mistake it shows error ex 'print(marks['irum']) the output-error
# if v use get it shows the output- None

print(marks.values())#output-dict_values([9, 5, 5, 8, 4, 7, 6, 5, 8])
print(marks.keys())#output- dict_keys(['abu', 'muzammil', 'faizan', 'Vasefa', 'indris', 'mubashera', 'iram', 'saeed', 'Alhumd'])
print(marks.items())#it shows keys and values in tuple forms
#dict_items([('abu', 9), ('muzammil', 5), ('faizan', 5), ('Vasefa', 8), ('indris', 4), ('mubashera', 7), ('iram', 6), ('saeed', 5), ('Alhumd', 8)])

'''if else statement'''
Age = int(input("Enter your age: "))
if (Age >= 18):
    print("yes u can drive")
elif (Age == 10):
    print("you are a kid")
else:
    print("no, u can go home")
#output-Enter your age: 18
 #yes u can drive


"""MATCH case Satements - aapke diye variable ke hissab se output deta he"""
a = int(input("enter number: "))
match a:
    case 1:
        print('case is 1')
    case 2:
        print('case 2')
    case 43:
        print('case is sensetive')
    case _:
        print('no match found')
#output=enter number: 43
#       case is sensetive



"""'''for loop with range'''
for i in range(10):
    print(i+1)#i+1, because it gives us 0-9, i+1 gives us 9+1=10
    print(i)

'''for loop with list'''
a = [23,21,65,56,90]
for item in a:
    print(item)
'''for can be used is set,dictionary,tuples etc'''"""

'''While loop'''
a = 0
while(0<5):
    print(a)
    a +=1
    

#Fuctions with python
def greethello(name,ending):
    print('hello '+name)
    print('sab kushal mangal')
    print(ending)
greethello('abu','bye')
greethello('tareeq','shaikh')
#output-hello abu
#       sab kushal mangal
#        bye
#       hello tareeq
#       sab kushal mangal
#       shaikh

'''STRING concept- f str concept- '''
def lettergenerator(name,date):
    st=f"Hi mam, this is {name} and i won't come on {date}"
    print(st)
lettergenerator('tareeq','1 dec')
lettergenerator('muzu','2 nov')
# output-Hi mam, this is tareeq and i won't come on 1 dec
#        Hi mam, this is muzu and i won't come on 2 nov


#File Handling
'''IN this topic we are gonna learn about file menipulating(formating,append,creat,remove,open function)'''
f = open("herry.txt","r")#r for read its a command in filehandling
print(f.read())
#output--herry is a iitian and also a youtuber
print(f.readline())#by readline we can read line if we use this command 2 times it give 2 line in output ex.-
print(f.readline())
#output-he is a good gay
#    and he is a programmer
f.close()
f= open('herry','a')#a for appand kuch bhi line badana ya ghtana
f.write('herry is unmarried')
f.close()
f= open('herry','r')
print(f.read())
f.close()
#f= open('newtrail.txt','x')# x is used for creating a new file which is not exist before

import os
os.remove('herry')#it would remove herry named file

#we can use if else and loops in file handling

import os
if os.path.exists('newtrail.txt'):
    os.remove('newtrail.txt')
else:
    print('file does not exist')
#it remove

import os
if os.path.exists('herry.txt'):
    os.remove('herry.txt')
else:
    print('tata')
#output-the file named herry.txt removed


#Exception Handling
# ek user ager koi website chla rha he to wo kuch bhi kr skta he ese ho sakta he wo kuch bhi command dede agr aapne wo comman
# mention nhi ki hogi code me to wo error bategi or crash ho jayegi iske liye
#hm error se bachne ke liye 'try' & 'except' use krte he python me
try:
    a=int(input('enter a number'))
    print(a+2)
except:
    print('something is wrong')

"""Object Oriented Programming"""
'''CLASESS-CLASESS EK TEMPLATE KI TARAH HOTI HE JO KI OBJECTS KO BANANE ME ISTEMAL KI JATI HE'''
class employee:
    def __init__(self, name, salary):#this is a constrocter. constrocter ek esa function hota he jo object banane me automatic run hota he
        self.name=name
        self.salary=salary

    def getsalary(self):
        print(self.salary)

rohan=employee('Rohan', '7000')
print(rohan.salary)
print(rohan.name)
rohan.getsalary()

tareeq=employee('Tareeq', '500')
print(tareeq.name)
print(tareeq.salary)
tareeq.getsalary()
#output--7000
#       Rohan
#       7000
#       Tareeq
#       500
#       500
 