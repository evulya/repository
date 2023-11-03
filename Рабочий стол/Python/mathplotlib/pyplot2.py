from mathplotlib import pyplot
import math
xs = [x/100 for x in range(1000)]
y_sin = [math.sin(x) for x in xs]
y_cos = [math.cos(x) for x in xs]
pyplot.plot(xs, y_sin, label='sin(x)', color='blue')
pyplot.plot(xs, y_cos, label='cos(x)', color='green')
pyplot.legend()
pyplot.show()