from cmath import pi
from distutils.archive_util import make_archive
from itertools import count
from msilib.schema import SelfReg
from random import random
from traceback import print_tb
import random
from venv import create
from xxlimited import new


L1 = [1,2,3]
L2 = ['a','b','c']
L3 = L1 + L2
print(L3)

adict = {'GR':'Greece','IT':'Italy'}
print(len(adict))

word_dict = {'one':'ena'}

key_list = ['Ca', 'Cn', 'Br']
value_list = ['Canada', 'China', 'Brazil']
adict = {key_list[i]:value_list[i] for i in range(3)}
print(adict)

d1 = {'a' : 1, 'b' : 2}
for key in d1:
    print(d1[key])

d = {2:'dyo', 1: 'ena'}
for i in d:
    print(i)

adict = {x:x**2 for x in range(1,6)}
for key,val in adict.items():
    print(key,val)

adict = {'H' : 'Υδρογόνο', 'He': 'Ήλιο'}
adict['H'] = 'Hydrogen'

mydict = {}
alist = ['1',0,'One']
mydict[alist[0]] = alist[2]

alist = ['1','2','3','4','5']
blist = ['A','B','C','D','E']
adict = {alist[k]:blist[-k] for k in range(1,5,2)}
print(adict)

alist = [1,2,3]
adict = {10:1,2:20}
i = alist[adict[10]]
if i in adict:
    print('true')
else:
    print('false')

alist = [{'α':'ΑΛΦΑ', 'β':'ΒΗΤΑ'},{'π':3.14,'e':2.718,'b':2}]
print(alist[1]['b'])

adict = {'letters':{'α':'ΑΛΦΑ','β':'ΒΗΤΑ'},
'numbers':{'π':3.14, 'e':2.718, 'b':2}}
print(adict['numbers']['b'])

data = [{'City':{'North':40, 'West':20},
'Distance':[1000,1500]},['kilometers','Celsius']]
print(data[0]['Distance'][1])

country = {}
country['GR'] = ['Greece','Athens',11]
country['IT'] = ['Italia','Rome',60]
country['ES'] = ['Spain','Madrid',50]
print(country)
country['ES'] = 'Spain'
print(country)


#diafaneia 46
country = {}

def asum(x,y):
    print(a,b)
    return x+y
a = 5
b = 10
c = asum(a,b)

def test(x,deflist):
    x = 4
    deflist[0] = 500
    return
a = 1 
mainlist = [100,200,300]
test(a,mainlist)
print(a,mainlist)

def power(x,y=2):
    return x**y
a = 5
print(power(a, 3))

def myfunc(a,b=10):
    print(a+b)
print(myfunc(5))

def f1(m,v):
    v[0] = m
    return v
a = 200
b = [1,2,3]
print(f1(a,b))

class Car:
    '''The Car class creates car instances'''
    pass
def create_new_car(CarClass):
    '''create_new_car method creates new class instance'''
    newcar = CarClass()
    return newcar
mynewcar = create_new_car(Car)
help(Car)
help(create_new_car)

print("μαλακας")

class Person:
    def setname(self,name):
        self.person_name = name
    def myprint():
        print("self.person_name")

p1 = Person()
Person.myprint()

class Test:
    x = 0
    def __init__(self, z):
        self.z = z
a = Test(5)
print(self.z)

class Car:
    carnum = 0

    def __init__(self,make):
        Car.carnum += 1
        self.make = make
        self.carnum = None
    def print_carnum():
        print("Πλήθος οχημάτων = ", Car.carnum)

mycar = Car("Citroen")
yourcar = Car("Toyota")
print(Car.carnum)
print(mycar.carnum)
Car.print_carnum()
# diafaneia 44 oop
def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def myprint():
    print('factorial: ',par)

num = 6
myprint()
par = factorial(num)
print(par)

n = input('n = ')
if n.isdigit():
    asum = 0
    for i in range(1, int(n)+1):
        asum += i
    print(asum)
else:
    alist = list(n)
    alist.sort(reverse=True)
    alist.insert(len(alist),'$')
    print(alist)

with open('myfile.txt', 'w') as f:
    f.write('Δημιουργία αρχείου για εγγραφή')

with open('xfile', 'w') as fix:
    xline='newline'
    fix.write(xline)

with open('data.txt','r') as f:
    print(f.read(5))

class Foo:
    def printLine(self, line='Python'):
        print(line)
o1 = Foo()
o1.printLine('Java')

class Point:
    def __init__(self, x=0,y=0):
        self.x = x+1
        self.y = y+1
p1 = Point()
print(p1.x,p1.y)

class Sales:
    def __init__(self,id):
        self.id = id
        id = 100
val = Sales(123)
print(Sales.id)

class Pelatis:
    pelnum = 0
    pel_list = []
    def __init__(self):
        Pelatis.pelnum+=1
        Pelatis.pel_list.append('pl'+str(Pelatis.pelnum))
    def pel_print(self):
        print(Pelatis.pel_list)
pel1 = Pelatis()
pel1.pel_list.append('pl100')
pel1.pel_print()

class Vehicle:
    def __init__(self,ms,k):
        self.max_speed = ms
        self.kilometers = k
    def print_attributes(self):
        print(self.max_speed,self.kilometers)
v1 = Vehicle(5,5)
v1.print_attributes()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * 3.14
c = Circle(4)
print(c.area())

class Rectangle:
    '''Κλάση τετράγωνου'''
    num = 0
    def __init__(self, l = 1, w = 1):
        self.length = l
        self.width = w
        Rectangle.num += 1
    def area(self):
        return self.length * self.width
    def numofrec():
        return Rectangle.num

list = [Rectangle() for i in range(2)]
print(Rectangle.numofrec())
help(Rectangle)

# klhronomikothta diaf. 11
import random

class CardGame:

    cards = {'A':{'num':1,'points':5},
             'K':{'num':2,'points':4},
             'Q':{'num':3,'points':3},
             'J':{'num':4,'points':2}}

    def __init__(self, d = [], score = 0):
        self.d = d
        self.score = score
        self.createDeck()

    def createDeck(self):
        for key in CardGame.cards:
            for i in range(CardGame.cards[key]['num']):
                self.d.append(key)

    def guessCard(self):
        random.shuffle(self.d)
        r = random.choice(self.d)
        self.d.remove(r)
        guess = input("guess the letter (A,K,Q,J): ")
        if guess == r:
            self.score += CardGame.cards[r]['points']
        return r
    
    def deckLength(self):
        return len(self.d)

    def printScore(self):
        print("Score = ", self.score)
        
    def printDeck(self):
        print(self.d)

# exit = False
new_card_game = CardGame()
new_card_game.printDeck()
while new_card_game.deckLength() != 0:
    r = new_card_game.guessCard()
    print("picked card was : ", r)
    new_card_game.printScore()
    new_card_game.printDeck()
    
    # answer = input("do you want to exit? (y/n)")
    # if answer == 'y':
    #     exit = True
    #     print("exiting game")
new_card_game.printScore()




import classes
sak = classes.SakClass()
sak.print_sak()
letters = ['ΣΣΣΣΣΣΣΣΣΣΣ']
sak.putbackletters(letters)
sak.print_sak()

import random
l = ["a", "b", "c", "d", "e", "f", "g"]
sample = random.sample(l, 8)
print(sample)
for s in sample:
    l.remove(s)
print(l)
