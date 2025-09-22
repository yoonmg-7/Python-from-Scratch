# <----------------------------------filter way----------------------------->

# nums =[1,2,3,4,5,6,7,8,9]
# def even(num):
#     return (num%2) == 0     #return true or false

# # filter(Function,list)
# evenNums = list(filter(even,nums))
# print(evenNums)



# <----------------------------------comprehension way----------------------------->

# nums =[1,2,3,4,5,6,7,8,9]
# evenNums = [ num for num in nums if (num%2) == 0]
# print(evenNums)




# <----------------------------------Traditional way----------------------------->

# nums =[1,2,3,4,5,6,7,8,9]
# evenNums=[]

# for num in nums:
#     if (num%2) == 0 :
#         evenNums.append(num)

# print(evenNums)