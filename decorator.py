def greet(fun):
   
   def wrapper(name):
       #before
       print("hello")
       fun(name) 
       #after 
       print("Good Bye")   
   return wrapper   


@greet
def sayname(name):
    print(name)

sayname("Yoon Nandar Maung")