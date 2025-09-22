# def add(n1,n2):
#     return n1+n2

# print(add(4,5))

# add =lambda n1,n2: n1+n2
# print(add(4,5))


nums =[1,2,3,4,5,6,7,8,9]
# def even(num):
#     return (num%2) == 0     #return true or false

evenNums = list(filter(lambda num:(num%2) == 0,nums))
print(evenNums)