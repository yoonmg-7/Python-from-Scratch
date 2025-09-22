nums =[1,2,3,4,5,6,7,8,9]

def mapFunction(num):
    return num*2

# map(Function,list)
nums = list(map(mapFunction,nums))
print(nums)