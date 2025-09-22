# ----------------function--------------------

def greet(name,time):
    print(f"Hello,{time}! {name}.");

greet("Kyaw Kyaw","Good Morning") #Hello,Good Morning! Kyaw Kyaw.
greet("Mg Mg","Good Evening") #Hello,Good Evening! Mg Mg.


# -----------------default parameter-------------------


def greet(name="Kaung Kaung",time="morning"):
    print(f"Hello,{time}! {name}.");

greet();   #Hello,morning! Kaung Kaung.
greet("Kyaw Kyaw","Good Morning") #Hello,Good Morning! Kyaw Kyaw.
greet(time = "Good Morning", name = "Kyaw Kyaw")  #Hello,Good Morning! Kyaw Kyaw.


# -------------------what is variable scope-------------------(local & global variable)-----------------------


name = "Mg Mg" #global varialbe

def callmyName():
    name = "Shwe Shwe" #local variable
    print(name) #Shwe Shwe

callmyName();
print(name)  # Mg Mg



name = "Mg Mg" #global varialbe

def callmyName():
    global name;
    name = "Shwe Shwe" #local variable
    print(name) #Shwe Shwe

callmyName();
print(name)  #Shwe Shwe


# ----------------------------Dictionary in Python------------------------------

person ={
    'name' : "yoon nandar mg",
    'age' : "26"
}

person['hair_color'] = 'black'
print(person);                #// {'name': 'yoon nandar mg', 'age': '26', 'hair_color': 'black'}

#check "key" to use "in" person
print('name' in person)        // True
print('nothing' in person)     // False

# Using condition 
if 'name' in person:
    print("work");

person_keys = list(person.keys())
print(person_keys)              // ['name', 'age']

person_values = list(person.values())
print(person_values)     //['yoon nandar mg', '26']


# -----------------------------------Example----------------------------------------------------------
#(eg=1)
person = {}

name = input('name:')
age = input('age:')
person[name] = age
print(person)  # {'YNDM': '26'}



#(eg=2)
person = {}
while True:
    name = input('name:')
    age = input('age:')
    person[name] = age

    another = input("another y/n :")
    if another == 'y':
        continue;
    else :
        break;

print(person);    #{'mgmg': '18', 'kgkg': '10'}
print(person.items());  #dict_items([('mgmg ', '18'), ('kgkg', '10')])

for (key,value) in person.items():
    print(f"{key} is {value} years old.")   # mgmg is 18 years old.
                                            # kgkg is 10 years old.


# -------------------------------------------------End------------------------------------------------------------------                                            