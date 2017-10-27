import random

print "Learning Python"
print random.randint(1,10) ## intiger

## variables
a_integer = 1
a_float = 10.2

name = "alejandro"

## Boolean
something_true = True

## Lists
names = ["alejandro", "cris", "paula"]
other_list = ["alejandro", "cris", 1, [1,2,3]]
empty_list = []

## Random Name
name_unique = random.choice(names)
print name_unique + " random name"

## Iterate
names[0] # alejandro
names[-1] # paula
print names[1:3] # cris, paula

names.append("ariana")

for name in names:
    print name

# for i, name in enumerate(names):
#     print i
#     print name


## If Statement

if 1 == 1:
    print "1 equal to 1"
elif 1 == 2:
    print "this is weird"
else:
    print "1 is not equal to 1"


## Functions

def say_hi(who):
    return who ## keep value of variable
    if who == "phone":
        print "i'm your " + who
    else:
        print "hello " + names[0] + " from: " + who

say_hi("computer") ## hello alejandro from: computer
say_hi("phone") ## I'm your phone
say_hi(name_unique) ## ## hello alejandro from: random_name

range(0,10) ## [0,1,2,3,4.....]
