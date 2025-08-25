# -------------------------For loop-------------------------------------

# names =["kyaw kyaw","Su Su","Mg Mg","Aung Aung"]

# for name in names:
#     if name == "Mg Mg":
#         print(f"{name} is a instructor.");
#         break;
#     else :
#         print(f"{name} is a student.");



# -------------------------while loop-------------------------------------
# num = 0
# while num < 10:
#     if num > 5:
#         break
#     if num % 2 == 0:
#         print(f"{num}");
#     num += 1;


# -------------------------range.py-------------------------------------------

# for num in range(5): #one parameter accept //0,1,2,3,4
# for num in range(3,5): #two parameter accept  //3,4
for num in range(0,20,4): #three parameter accept  // 0,4,8,12,16
    print(num);

fruits =["Apple","Orange","Mango","Banana","Pine Apple"]

for num in range(len(fruits)):
    print(fruits[num]);