# with open('./about.txt','w') as file:
#     file.write("Hello")

# # other work


# # a(ammend)
# with open('./about.txt','a') as file:
#     file.write("\nGood morning")

lists = ["Hello","\nGood morning"]
with open('./about.txt','w') as file:
    file.writelines(lists)