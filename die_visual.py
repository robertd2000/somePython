import pygal
from die import Die

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die()

results = []

for _ in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for i in range(3, max_result + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [str(i) for i in range(3, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
