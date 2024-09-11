#Working with Variables
"""
a = 10
str = "Singer"
b = 10.01
c = a+int(b)
print(c)
print(type(c))
"""

#Getting inputs from user
"""
name = input("Enter your name: ")
print("Given name is: ",name)
print(type(name))
"""
#Comment linese
#Single_line
#Multiple line
"""
name
Age
"""
print("--------------------")

#String Concatenatin
"""
a = input("Enter a value:")
b = input("Enter b value:")
c = a+b
print(c)
print(type(c))
"""

#Adding two numbers
"""
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = a+b
print(c)
print(type(c))
"""


#Adding Two DEcimal numbers
"""
a = float(input("Enter a value:"))
b = float(input("Enter b value:"))
c = a+b
print(c)
print(type(c))
"""


#Multiple Inputs in single line --- Split keyword is used
"""
name1,name2,name3 = input("get 3 names:").split()
print("name1 :",name1)
print("name2 :",name2)
print("name3 :",name3)
"""


#Multiple Inputs in single line --- Split keyword is used --- If name with surname
"""
name1,name2,name3 = input("get 3 names:").split(',')
print("name1 :",name1)
print("name2 :",name2)
print("name3 :",name3)
"""

#Multiline string:
"""
a =
"""
"""Lorem Ipsum is simply dummy text of the printing and typesetting
industry. Lorem Ipsum has been the industrys standard dummy text ever
since the 1500s, when an unknown printer took a galley of type and
scrambled it to make a type specimen book. It has survived not only five
centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularised in the 1960s with the release
of Letraset sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including versions
of Lorem Ipsum """
"""
print(type(a))
print(a)
"""

#Working with List
"""
para = [10,20,30,40]
print(type(para))
print(para)
print(para[0])
print(para[2])
"""


#joining list --- Strings into list
"""
para = ["10","20","30","40"]
print(','.join(para))
print('|'.join(para))
"""


#Append
"""
para = []
print("Enter the para:")
while True:
    line = input()
    if line:
        para.append(line)
    else:
            break
    print(para)

    output = '\n'.join(para)
    print(output)
"""

#Working with strings
"""
a = "Bharath Dhanavan"
print(type(a))
print(a)
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.count("a")) #Shows how many a's present in the string
print(a.endswith("an")) #Boolean value
print(a.endswith("ar")) #Boolean value
print(a.find("D")) #Displays the index value
print(a.find("a",5)) #that the Character present, after the given index
print(a.replace("h","g"))
print(a.isupper())
print(a.islower())
print(a.isalnum())
print(a.isalpha())
"""

#Splitting lines in strings
"""
s = "he\nis\nGenius"
print(s)
print(s.splitlines())
print(s.splitlines(True))
"""

#Space btw Strings
"""
a = "Learning python is quite ease"
print(a.split(" "))
print(a.split(","))
"""

#Remove space btw strings
"""
s = "    Good   "
print(len(s))
print(len(s.strip())) #Reduce te space and print the data
print(len(s.lstrip()))
print(len(s.rstrip()))
"""

#Partition in string
"""
s = "26-12-2000"
print(s.partition('-')) #To display the date into date , month and year
"""

#String manipulation in string
"""
s = "sample"                            # s  a  m  p  l  e
print(s)                                # 0  1  2  3  4  5
print(s[0:2])                           #-6 -5 -4 -3 -2 -1 
print(s[2:])
print(s[:5])
print(s[-1])
print(s[:-1])
print(s[-3:-1])
print(s[::-1])
"""


#Operators in python
#Arithmetic Operators
"""
a = 10
b = 15
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)
"""

#Assignment Operators
"""
a = 125
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a%=5
print(a)
"""

#Comparison Operators
"""
a = 10
b = 20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
"""

#Logical Operators
"""
a = 25
print(a>=10 and a<=20)
print(a>=10 or a<=20)
print(not(a>=10 and a<=20))
"""

#Bitwis Operators
"""
a = 10
b = 45
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
"""

#Control Statements
#if and else statement
#Finding the Even number
"""
n = int(input("Enter the value: "))
if n%2==0:
    print(n,"Even number")
else:
    print(n,"Odd number")
"""

#elif statement
"""
days = int(input("Enter the days:"))
if days == 0:
    print("Good no Fine")
elif  days>=1 and days<=5:
    print("fine amount:",days * 0.5)
elif days>5 and days<=10:
    print("fine amount:",days * 1)
elif days>10 and days<=30:
    print("fine amount:",days * 8)
else:
    print("Membership cancelled")
"""

#Nested if statement
"""
m1 = int(input("Enter mark1:"))
m2 = int(input("Enter mark2:"))
m3 = int(input("Enter mark3:"))

total = m1 + m2 + m3
average = total/3
print(f"total : {total}")
print(f"average : {average:.2f}")
if m1>=35 and m2>=35 and m3>=35:
    print("All pass")
    
    if average>=90 and average<=100:
        print("Grade A")
    elif average>=80 and average<=89:
        print("Grade B")
    elif average>=70 and average<=79:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Fail")
    print("No Grade")
"""

#While loop
"""
i = 1
while i<=10:
    print(i)
    i+=1
#odd numbers
n = 20
i = 1
print("Odd numbers")
while i<=20:
    print(i)
    i+=2
#even numbers
i = 2
n = 20
print("even numbers")
while i<=20:
    print(i)
    i+=2
"""

#Continue statement
"""
i = 1
while i<=20:
    if i%2==0:
        i+=1
        continue;
    print(i)
    i+=1
"""

#Break statement
"""
i = 1
while i<=20:
        if i == 7:
            break;
        print(i)
        i+=1
"""

#Range in python
"""
print(list(range(4)))
print(list(range(2,5)))
print(list(range(0,20,2)))
print(list(range(1,21,2)))
a = list(range(5))
print(a)
"""

#For Loop:
"""
for i in range(0,21,2):
    print(i)
#Storing and disp
total_sum=0
for i in range(5):
    a = int(input("Enter value a:"))
    b = int(input("Enter valur b:"))
    c = a+b
    total_sum += c
print(total_sum)
"""

#Nested Loop
"""
for i in range(5):
    for j in range(i):
        print("*",end="") # To print in Single line  
        print("") 
"""
#Reversal order
"""
for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
        #print("")
"""
"""
for i in range(65,70,1):
    print(i)
for i in range(65,70,1):
    print(chr(i))  #Displays the Ascii character
for i in range(97,102,1):
    print(chr(i))
    """
"""
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end=" ")
        print()
        print("")
"""

#While else and for loop
"""
i=1
while i<=5:
    #if(i==4):
        # break;
    print(i)
    i += 1
else:
    print("loop completed")
for i in range(1,21):
    #if i==5:
       # break;
        print(i)
else:
        print("loop completed")
"""

#List and its function: #Sequence type #mutable -- Changeable
"""
a = [1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print("Slicing Array")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[:2])
print(a[3:])
"""
"""
a = [1,True,"str",'a',2.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[0],type(a[0]))
print(a[1],type(a[1]))
print(a[2],type(a[2]))
print(a[3],type(a[3]))
print(a[4],type(a[4]))
print(a[5],type(a[5]))
"""
"""
a = [10,20,30,40]
print(a)
a.clear()
print(a)
a = [5,15,25,35,45]
b = a.copy()
print(b)
a = [10,20,25,30,35,40,45,47]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0) #Removes the element from the index
print(a)
a.remove(40)    #Removes the element from the list
print(a)
"""
"""
name = ["Ram"]
print(name)
name.append("Sam")
name.append("Abi")
name.append("Mano")
name.append("Kile")
print(name)
name2 = ["Nisha","Harini"]
name.extend(name2) #Adds this into that
print(name)
name.insert(0,"Gayathri")
print(name)
"""
"""
print(list(range(5)))
print(list("bharath"))
a = [10,100,2,20,50]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a = ["Orange","Apple","Grapes"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)
"""

#Tuples in python #Surrounded by Round braces #Immutable ---- unchangabble
"""
a = (1,2.5,True,"Ram")
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a) #Type conversion
print(b)
b.append("Rahman")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))
"""
"""
a = ['banana', 'fig', 'apple', 'kiwi','Raj']
for i in a:
    print(i)
    if "Raj" in a:
        print("Raj is not Found")
    else:
        print("Raj is Found")
    print(len(a))
"""
"""
a=(1)
print(type(a))
a=(1,)
print(type(a))
del a
print(a)        #Output -- NameError:name 'a' is not defined
"""
"""
a = (1,2,3,4)
b = (5,6,7,8)
c = a+b        #Concatenation
print(c)    
print(type(c))
print(c.count(7))
"""

#Nested Tuples
"""
a = (1,2,3,4)
b = (5,6,7,8)
c = (a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
x = ('Johnny',)*5
print(x)
"""

#Minimum and Maximum in Tuples
"""
a = (1,2,3,4)
print(max(a))
print(min(a))
"""

#Sets and its Function in Tuples -- Unordered and Unindexed datatype -- Curly braces
"""
names = {'Ram','Sita','Laxman'}
print(names)
print(type(names))

#Accessing values using for loop
for name in names:
    print(name)
    
#Adding names
names.add('Anu')
print(names)


#Update another set of data
a = {'Kumar','Bharath','Dhanvan'}
names.update(a)
print(names)
names.remove('Kumar')
print(names)
names.discard('Dhanvan')    #If available removes else discard
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names

#Set removes duplicates automatically
names = {'Ram','Ram','Sita','Dhanavan','Laxman'}
print(names)
#Union function
a = {1,2,3,4}
b = {'a','b','c','d'}
c = a.union(b)
a.update(b)
print(a)
#Intersection
a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

#Symmetric difference -- Different values from one set are stored on another set

a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.symmetric_difference(b) 
print(c)
a.symmetric_difference_update(b)
print(a)

#Disjoints subsets and Superset
a = {5,6,7}
b = {5,6,7}
c = a.isdisjoint(b) #matched->false unmatched->true
print(c)
c = a.issubset(b)   #matched->true unmatched->false
print(c)
c = a.issuperset(b) #matched->true unmatched->false
print(c)
"""

#Dictionary and its function  --- keypar() --> contains keys and values
"""
user = {
    "name" : "Ram",
    "age" : 25,
    "ismarried" : "True"
    }
print(type(user))
print(user)
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

#Loop
for x in user:
    #print(x)
    #print(user[x])
    print(x," ",user[x])
for x in user.values():
    print(x)
for x in user.keys():
    print(x)
for x,y in user.items():

#if statement
if "gender" in user:
    print("present")
else:
    print("Not present")

#Changing valuese
user.update({"gender":"Male"})
print(user)
user["age"]=27
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
"""
#Nested Dictionary
"""
users = {
    "user1":
    {
        "name" : "Sam",
        "age" : 55,
        "isMarried" : "True"
        },
    "user2":
    {
        "name" : "Ram",
        "age" : 15, 
        "isMarried" : "False"
        }
    }
print(users)
"""

#Identity Operators  --- Comparing objects -- Equal or not --- #is #isnot
"""
a = [1,2]
b = [1,2]
c=a
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(a is b)
print(a==b)
print(a is not b)
print(a is not c)
print(a!=b)
"""

#Membership operators  -- Check the member is availabl or not
"""
a = [10,20,3,30,40]
print(3 in a)
print(3 not in a)
"""

#User defined functions  -- def keyword is used
"""
def welcome():
    print("Phython")
welcome()
"""
#No return type w/o args
"""
def add():
    a=int(input("Enter value a:"))
    b=int(input("Enter value b:"))
    c=a+b
    print("Total",c)
add()
"""

#No return type with args
"""
def sub(a,b):
    c=a-b
    print("Difference",c)
sub(24,2)

#Return type w/o args

def mul():
    a=int(input("Enter value a:"))
    b=int(input("Enter value b:"))
    c=a*b
    return c

x=mul()
print("Mul:",x)

#Return type with args

def div(a,b):
    c=a/b
    return c

x=div(20,2)
print("Div:",x)
"""

#Arbitary arguments -- Pass multiple args in function and converted into list -- * Symbol used
"""
def class_10(*students):
    print(students)
    for user in students:
        print(user)
        
class_10("Ram","Sam","Tom")


# args -- Functions
def message(name,age):
    print("name:",name,"age:",age)

message("Ram",25)
message(age=25,name="Ram")

#Arbitary args in function  -- Requests as **
`
def biodata(**data):
    print(data)

biodata(name="Ram Kumar",age=25,gender="male")

#Default parameterized function

def user(name,age=20):
    print(name,"age is:",age)

user("ram",52)
user("Sam")

#List of args -- Function
def total(marks):
    return sum(marks)

print("Total:",total([55,80,35,54,68]))

"""
#Recursive function -- calls itself
"""
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
print(f"Factorial:",factorial(5))
"""

#Lambda function
"""
c=lambda a:a+50
print(c(5))

c=lambda a,b:a*b
print(c(10,25))
"""

#Datetime package
"""
import datetime as dt
current_date =dt.date.today()
print("Current Date:",current_date)

#new = dt.date(2024,12,26)
#print(new)
print("Year:",current_date.year)
print("Month:",current_date.month)
print("Day:",current_date.day)

#Using time
time = dt.datetime.now().today()
print("Current Time:",time)

print("Hour:",time.hour)
print("Minute:",time.minute)
print("Seconds:",time.second)
print("Microsecond:",time.microsecond)

#user defined date and time
a = dt.time(10,45,5,555055)
print("Hour:",a.hour)
print("Minute:",a.minute)
print("Seconds:",a.second)
print("Microsecond:",a.microsecond)

a = dt.datetime(2026,12,26,12,2,10)
print("Year:",a.year)
print("Month:",a.month)
print("Day:",a.day)
print("Time:",a.time())
#print("Day:",a.day())


#Difference btw dates
current = dt.datetime.now().today()
new_year = dt.datetime(2025,1,1)
difference = new_year - current
print(difference)

#Custom style
current = dt.datetime.now()
print(current)
s=current.strftime("%A %b %d %Y")  #A->Day b->Month d->date Y->year
print(s)
"""

#Math Package
"""
import math
print(math.sqrt(4))
print(math.ceil(1.5555))
print(math.ceil(1.556))
print(math.factorial(5))
print(math.fabs(-5))
print(math.pow(2,3))
print(math.log2(2))
print(math.log10(2))
print(math.pi)
print(math.e)
"""


#Exception handling --- try except block
"""
a=10/0
print(a)
"""


"""
try:
    a = 10 / 0
except Exception as e:
    print(e)
    

#try except using else block
try:
    a=10/25
except Exception as e:
    print(e)
else:
    print("a value:",a)

#try except using finally block
try:
    a=10/22
except Exception as e:
    print(e)
else:
    print("a value:",a)
finally:
    print("Completed")

#Types of Exception in phython
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

#Name error exception
try:
    print(ss)
except Exception as e:
    print("A is not defined")
    

#zero error/Zero Division error
try:
    print(25/0)
except Exception as e:
    print("Determination cant be zero")

#Value error Exception
try:
    a=int("Dome")
except Exception as e:
    print("Please enter only numbers!!")

#IndexError Exception
try:
    a=[10,20,30,40]
    print(a[10])
except Exception as e:
    print(e)

#FilenotFound Exception
try:
    f=open("file.txt")
except Exception as e:
    print(e)
    print("File not found")
else:
    print(f.read())
"""


#Handling multiple exceptions

"""
try:
    a=10/0
    print(a)
    b=[10,20,30]
    print(b[5])
except ZeroDivisionError:
    print("zero division error")
except IndexError:
    print("Index error")
"""

