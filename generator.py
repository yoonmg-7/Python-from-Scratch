#< ------------------------------------gibberish generator-------------------------------->
from random import randint

words = ['apple','orange','grape','strawberry','lime'];

def randomsetencegenerator(word):
   randomIndex = randint(0,len(words)-1)
   return f'{words[randomIndex]} {word}'

with open('./text.txt') as file:
   paragraph = file.read();
   wordlist = paragraph.split(); #['asdf','asdf']
   setencelist = list(map(randomsetencegenerator,wordlist)) #[]

   paraCount = int(input("How many paragraph :")) #3

   for count in range(paraCount):
      with open('./generator.txt','a') as write_file:
         write_file.write(''.join(setencelist )+'\n\n') #list to string using join method