import maya.cmds as cmds

# create polygon sphere

cmds.polySphere()

# create polygon sphere with radius of 10
cmds.polySphere(radius=10)

# help command
cmds.help("polySphere")

# query sphere radius
cmds.polySphere("polySphere2", query=True, radius=True)

# edit radius sphere
cmds.polySphere("polySphere2", edit=True, radius=5)

# don't forget about Truncation!
10/3

# modulus 
10 % 3

# comparison

10 > 2  # greater
10 < 2  # lesser
10 >= 2 # greater and equal to 
10 <= 2 # lesser and equal to 

10 != 2 # not equal to

# getAttr - get attribute on named object
import maya.cmds as cmds
cmds.polyCube(name="cube")
cmds.getAttr("cube.visibility")

# setAttr - set attribute on object
import maya.cmds as cmds 

cmds.polyCube(name="cube")
cmds.setAttr("cube.tx", 10)
cmds.setAttr("cube.ty", 20)

cmds.setAttr("cube.rotate", 10, 20, 30, type="double3")


# Indexing
s1 = "abcdefg" # created string
s1[0] # first in string
s1[3] # third in string
s1[-1] # negative 1 from the end
s1[-3] # negative 3 from the end

#slicing
s1[0:3]
s1[2:5]

s1[2:] # 2nd and onwards
s1[:3] # up to 3rd
s1[:-1] # doesn't include the last indexed position


s1[0:5:2] # 1st to 5th, every 2nd
s1[0:5:3] # 1st to 5th, every 3rd


s = "Beginning Python for Maya"

s.upper()

s.lower()

s.isupper()
s.islower()

s.find("Python") # results starting index of the word Python

number = "1"
number.isdigit()
s.isdigit()
number.zfill(4)

s.split(" ")


# sorting lists

a = [443, 26, 1, 55, 101]
b = ["dog", "cat", "DOG", "CAT"]

a.sort() # sorts a list
sorted(a) # same as above but using the sorted function

a.sort(reverse=True) # sorts a list in reverse
sorted(a, reverse=True) # same as above but using sorted function

b.sort() # string objects with UPPER case will come before lower case objects
b.sort(key=str.lower) # lists UPPER case object, then lower case object, then in alphabetical order
sorted(b, key=str.lower) # same as above using sorted function


# ls command tutortial
import maya.cmds as cmds
cmds.ls(transforms=True) # displays transform nodes in the scene
cmds.ls(shapes=True) # displays shape nodes in the scene
cmds.ls(cameras=True) # displays camera nodes in the scene
cmds.ls(sl=True) # displays selected nodes in the scene

# ls command to turn visibility on and off based on selection
selection = cmds.ls(sl=True) # create a variable called selection and assign to this variable the currently selected nodes in the scene
for sel in selection:                                # for loop to set visibility in selection variable to OFF
    cmds.setAttr("{0}.visibility".format(sel), False)

selection = cmds.ls(sl=True, showType=True) # creates a new selection variable which shows the object followed by its type
cmds.ls(type="transform") # here I am explicityly telling the ls function to look for transform, you can change this to a specific type.
cmds.ls(transforms=True") # as an alternate you can just use the specific flag and set it to True however the above example is a far more precise and superior method
cmds.ls(type="mesh")      # here I am saying list only mesh nodes
cmds.ls(assemblies=True) # only returns the nodes at the top level of your scene
cmds.ls(references=True) # lists references in your scene

cmds.ls("persp") # here we are listing anything that contains the word persp
cmds.ls("*Sphere*", transforms=True) # here we are listing anything with a wildcard surrounding the word Sphere and then flagging it to show transforms only
cmds.ls("*Sphere*", type="transform") # here we are doing a list based on wild card Sphere again but this time filtering it by the type flag and explicitly stating to list only transform nodes


# dictionaries
d = {} # Empty dictionary
d = {"red":255, "grey":128, "blue":255} # dictionary with three items
d["red"]  # returns the contents of red
d["green"] = 255 # adding green with 255 as its value
d["black"] = 0 # adding black with 0 as its value

d["cyan"] # now we try accessing the dictionary and pulling cyan but it errors....so we get around this by using the below instead...
d.get("cyan") # ...now we are trying to get the cyan but it returns nothing since it doesn't so far exist

# dictionary continued - memberships 
"red" in d  # returns True as it exists in the dictionary
"cyan" in d  # returns False as it doesn't exist in the dictionary

# dictionary continued - method
d.keys() # returns keys only, 1st tuple 0
d.values() # returns values, 2nd tuple  1
d.items() # returns the items with a tuple

for key in d.keys(): # returns the values for all the keys in the dictionary
    print(d[key]) # prints the values in the keys

for item in d.items(): # now we are returning the tuple via the items flag
    print("{0} - > {1}".format(item[0], item[1])) # here I am formatting a print function so it's legible
    



# tuples - cannot be changed it's immutable
t = () # empty tuple

t = (1, "abc") # two item tuple
t[0] # returns first item in tuple in this case 1
t[1] # returns second item in tuple in this case abc


# python statements
a = 11
b = "python"

# print statement
print("Hey man this is just a print message.")

# if/else
if a < 10:     # if a is lesser than 10, then print less than
    print("less than")
elif a == 10:   # if not the above then if a equals 10 then print equal to
    print("equal to")
else:           # if nothing from the above then it must be greater than so print greater than
    print("greater than")


# if / else continuation in detail
# 
if True:
    print("This is a true statement")
    
    
if 10 > 0:
    print("This is a true statement")
    
    

test = 3
    
if test:
    print("This is a true statement")
else:
    print("This is a false statement")
    
    
sel = cmds.ls(sl=True)

if len(sel) >= 2:
    for s in sel:
        print(s)
elif len(sel) == 1:
            print("Please select at least two objects")
else:
    print("Select something...")


# for loop (iterate over a sequence)
for x in range(0, 10):
    if x % 2:
        continue # Continue execution of the loop
    else:
        print(x)
        

# while loop
while True:
    if exitloop():
        break # exit the loop

# function
def add(input_a, input_b):
    return input_a + input_b # return statement
    
