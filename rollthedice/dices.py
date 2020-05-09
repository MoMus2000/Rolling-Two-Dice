from random import randint
import pygal

class dice1():

    def __init__(self, numsides = 6):
        self.numsides = numsides

    def rolls(self):

        return randint(1,self.numsides)

class dice2():

    def __init__(self, numsides = 6):
        self.numsides = numsides

    def rolls(self):

        return randint(1,self.numsides)



results = []

die1 = dice1()
die2 = dice2()

for num in range(10000):
    result = die1.rolls() + die2.rolls()
    results.append(result)



frequencies = []

for value in range(1,13):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title= "Rolling two dice 1000 times"

hist.x_title= "sums"
hist.y_title= "Frequencies"
hist.x_labels=['','2','3','4','5','6','7','8','9','10','11','12']
hist.add('d6+d6',frequencies)
hist.render_to_file('die_visual2.svg')