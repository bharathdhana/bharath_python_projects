a = 10
print(type(a))

str = "Marvel"
print(type(str))


x = 7
y = 10
print(x != y)

name = "Ram"
age = 24
print("My name is",name,"and my Age is",age)    

weight = 30.05
print(type(weight))

Love = True
print(type(Love))

Tamil = {12,24,25,55,65}
print(type(Tamil))

x = complex(5+5j)
print(type(x))

shoppinglist = ["biscuits","Juice","Ice cream"]
print(type(shoppinglist))

movies = ("Aranmanai","Star","Lover","Dear")
print(type(movies))

list = [1,2,1,1,5,4]
list = list.remove(1)
print(list)

listt = [2,33,222,14,25]
print(listt[-1])
#25

ex = ["Sunday","Monday","Tuesday","Wednesday"];
print(ex[-3:-1])
#mon,tue

def len_of_list():
    alist = [3,67,"cat",3.14,False]
    print(len(alist))


#my_tuple = (1,2,3,4)
#my_tuple.append((5,6,7))
#print(len(my_tuple))

t = (1,2)
print(2*t)


dict = {
    "brand" : "Bmw",
    "Model" : "M5",
    "Color" : "Blue"
    }
print(type(dict))
print(dict)


groceryset = {10,20,15,30,54}
print(type(groceryset))


#cricketlist = list(groceryset)
#print(type(cricketlist))
#print(cricketlist)


weather = "Normal"
if(weather == "Normal"):
    activity = "Ill go outside"
else:
    activity  = "Ill stay in home"
print(activity)

##if else
weather = "Normal"
if weather == "Normal":
    activity = "I'll go outside"
else:
    activity = "I'll stay at home"
print(activity)  # Moved the print statement outside of the if-else block

##if statement
tins = [1,2,3,4,5]
for tins in tins:
    print(tins * 2)

##if elif statement
weather = "Normal"
if(weather == "Normal"):
    activity = "Make some plan"
elif(weather == "Rainy"):
    activity = "Plan Postponed"
else:
    activity = "Plan Cancelled"
print(activity)
    



