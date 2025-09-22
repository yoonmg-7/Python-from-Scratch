# <---------------------------------First way read need close method------------------------------------------->

# file = open('./text.txt')

# for line in file:
#     print(line);

# file.seek(0);   #  //move cursor

# linelists = file.readlines()
# print(linelists);

# <---------------------------------limit read------------------------------------------->
# file = open('./text.txt')
# file.seek(50); 
# paragraph =file.read(100)
# print(paragraph);
# file.close()


# <---------------------------------Next way read not need close method------------------------------------------->
# with open('./text.txt') as file:
#     for line in file:
#         print(line);

# print("Hello world")
