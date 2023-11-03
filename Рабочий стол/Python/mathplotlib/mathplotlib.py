from mathplotlib import pyplot
#mathplotlib
import math
#xs
xs = [x/10 for x in range(100)]
# ys
ys = [math.sin(x) for x in xs]
pyplot.xlabel('X')
pyplot.ylabel('Y')
pyplot/plot(xs, ys, label = 'sin(x)')
pyplot.show()