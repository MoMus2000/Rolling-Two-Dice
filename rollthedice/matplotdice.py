# creating a graph on matplot lib for sums of two 6 sided dice

from random import randint
import matplotlib.pyplot as plt
import numpy as np


class dice1():
    def __init__(self, sides=6):
        self.sides = sides

    def rolls(self):
        return randint(1, self.sides)


class dice2():
    def __init__(self, sides=6):
        self.sides = sides

    def rolls(self):
        return randint(1, self.sides)


results = []
die1 = dice1()
die2 = dice2()
max = 12
for val in range(1000):
    sum = die1.rolls() + die2.rolls()
    results.append(sum)

frequencies = []

for value in range(2, max + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

vx = []
x=1
while x< max:

    x= x+1
    vx.append(str(x))



print(frequencies)
print(vx)
plt.xlabel("SUMS")
plt.ylabel("FREQUENCIES")
plt.title("SUMS OF TWO DIE")
plt.plot(vx,frequencies)
plt.savefig('sumsoftwodie.png')
