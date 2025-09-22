# ---------------------------------sorted function---------------------------------------

nums =[2,3,1,6,4,5,9,12,45,23]
print(sorted(nums))   # [1, 2, 3, 4, 5, 6, 9, 12, 23, 45]


names =['Aung Aung','bo bo','aye aye','Mg Mg','Aung la', "Baby"]
print(sorted(names))   # ['Aung Aung', 'Aung la', 'Baby', 'Mg Mg', 'aye aye', 'bo bo']


# -----------------------------set function-------------------------------------------------

numbers = [1,3,2,4,3,5,7,6,8,7,9,2]
print(set(numbers))   # {1, 2, 3, 4, 5, 6, 7, 8, 9}

for num in set(numbers):
    print(num)          # 1
                        # 2
                        # 3
                        # 4
                        # 5
                        # 6
                        # 7
                        # 8
                        # 9


# ------------------------------------------------------------------------------------------------
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

ages = list(person.values()) 
# print(ages)        #['20','40','20']

for age in set(ages):
    # print(age)    # 40 , 20 
    count = ages.count(age)
    print(f"{age} years old - {count}")  # 20 years old - 2
                                         # 40 years old - 1



# --------------------------------------------End--------------------------------------------------------------
