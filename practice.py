if 5>2:      print("hello world") #first Program




b="Hello hwo are you"
a = 243;
oh=True;
num=20.5

# print(type(a),type(b),type(oh),type(num)) #getting the data type


#type Casting
#type casting is a method Through which we can specify the data type during the time of variable initialization

name = float(True) #in this example we have type casted True as float so True chnage to 1.0
print(type(name),name)



# in python one variable could be redeclared infinite Times
x = 5
x = 10
x = 15
print(type(x))




#Legal variable names in Python 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Multiple variable at one line 


name,designation,age= "aman","Developer",20

print(name,designation,age) #print is the output method in python that means it is used to output values 


x = "awesome" # this is a globally Declared variable and can be accessed by function

def myfunc():
  x = "fantastic" # this variable can be accessed from the inside of the function
  print("Python is " + x) #this will print fantastic as the x here is pointing in the function

myfunc()

print("Python is " + x) # this will print awesome as it is Pointing to The global Variable




def myFunction():
  x=122;
  y=67;
  print(122-67)
  return 122+67

total = myFunction()

print(total)


#indentation in Python


if(144>54):
    print(True)
    print("yes 144 iss greated than 54")
    print("Yes This is Indentation")
    print("see the flow of program")

v=90



