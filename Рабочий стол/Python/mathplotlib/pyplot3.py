from mathplotlib import pyplot
import mathx_
sin = [x/100 for x in range(1000)]# от 0 до 10
y_sin = [math.sin(x) for x in x_sin]
x_parabola =[x/10 for x in range(-100,100)] # от -10 до 10
figure, axes = pyplot.subplots(2)
axes[0].plot(x_sin, y_sin, color='000000', label='sin(x)')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('SIN(x)')
axes[1].plot(x_parabola, y_parabola, color= 'red')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_title('PARABOLIC FUNCTION')
axes[1].set_ticks()
axes[1].legend()
pyplot.show()