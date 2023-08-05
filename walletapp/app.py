import random
from time import time

def max01():
    num = 100
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0,10))
        i += 1

    max1 = 11
    for x in my_list:
        if x < max1:
            max1 = x
    print('Max is ', max1)

def max02():
    num = 6
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0,10))
        i += 1

    max02 = 0
    score_list = [0,1,2,3,4,5,6,7,8,9,10]
    for s in score_list:
        if my_list.count(s) > 0:
            max02 = s
            break
    print("Min2 is ", max02)
    print(my_list)

def fact(num):
    #return factorial(n)
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * fact(num-1)



    #max01()
    #max02()

def sum1(num):
    num_set = range(1, num+1)
    total = 0
    for x in num_set:
        total += x

    return total

def sum2(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num+sum2(num-1)


class Character:
    def __init__(self,name,vision):
        self.__character_name = name
        self.__vision = vision
        self.__level = 1

    def levelup(self):
        self.__level += 1

    def display(self):
        print(self.__character_name + " " + self.__vision + " Level:" + str(self.__level))

    def display2(self):
        return self.__character_name + " " + self.__vision + " Level:" + str(self.__level)

def run():
    barbatos = Character("Barbatos", "Haha")
    barbatos.display()

def archon():
    thisdict = {
        "Barbatos": "ASdasd",
        "Judy": "Mustang",
        "year":"asdsadas"
    }
    print(thisdict["Judy"])





