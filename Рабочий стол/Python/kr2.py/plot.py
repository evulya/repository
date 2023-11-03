from matplotlib import pyplot
import math
xs =[x/10 for x in range(100)]
ys =[math.sin(x) for x in xs]
figure, axes = pyplot.subplots(2)
axes[0].plot(xs, ys, color='purple', label='sin(x)')
pyplot.show()