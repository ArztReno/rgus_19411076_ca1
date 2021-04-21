# date : 25/11/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question : 4

from abc import ABC, abstractmethod 
class Animals(ABC): 
  
 # abstract method 
    def move(self): 
        pass
  
class Snake(Animals): 
   # overriding abstract method 
    def move(self): 
        print("I can slither, I am the abstract base class") 
  
class Cheetah(Animals): 
   # overriding abstract method 
    def move(self):
        print("I can run really fast, I am the sublclass") 
  
class Elephant(Animals): 
   # overriding abstract method 
    def move(self): 
        print("I can walk really slowly, I also have a long trunk") 
  
class Lion(Animals): 
   # overriding abstract method 
    def move(self): 
        print("I can roar, I am the King of the Jungle") 
          
# Driver code
R = Snake() 
R.move() 
  
K = Cheetah() 
K.move() 
  
R = Elephant() 
R.move() 
  
K = Lion() 
K.move()  