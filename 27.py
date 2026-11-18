#level advanced

# scoping is a technical word for when variables are avaliable -> in pyret there is a program directory for the entire program and then when you define certain functions you create local definitions
# Python throws some curver balls -> main thing that complicates it is that python makes no distinction between <=> that is used to define something with a new name which adds something to the directory and <=> which is updating an exisiting name with something new 

# var x = 1- 
# fun my_fun(): 
#  x := 20 
#  end -> pyret 

x = 10 

def my_fun(): 
    global x 
    x = x + 20 
    return x
# does that mean the first or the second definition of x -> should you update the second x or create a new definition for the first x 
# use global to redefine x in the function 

def my_fun2(): 
    x = 20 
    return x + 20

def my_fun3(x: int): 
    return x + 20 

