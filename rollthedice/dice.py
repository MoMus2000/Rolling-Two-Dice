from random import randint
import pygal

class dice():

    def __init__(self, numsides = 6):
        self.numsides = numsides

    def rolls(self):

        return randint(1,self.numsides)



results = []

die = dice()
for num in range(1000):
    result = die.rolls()
    results.append(result)



frequencies = []

for value in range(1,die.numsides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title= "Rolling a dice 1000 times"

hist.x_title= "Sides of the Die"
hist.y_title= "Frequencies"
hist.x_labels = ['1','2','3','4','5','6']

hist.add('d6',frequencies)
hist.render_to_file('die_visual.svg')


