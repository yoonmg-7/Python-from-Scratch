# -------------------------For loop-------------------------------------

names =["kyaw kyaw","Su Su","Mg Mg","Aung Aung"]

for name in names:
    if name == "Mg Mg":
        print(f"{name} is a instructor.");
        break;
    else :
        print(f"{name} is a student.");



# -------------------------while loop-------------------------------------
num = 0
while num < 10:
    if num > 5:
        break
    if num % 2 == 0:
        print(f"{num}");
    num += 1;

