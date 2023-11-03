from matplotlib import pyplot as plt
from psutil import cpu_percent, virtual_memory
# интерактивный график пилы(пилообразный) из  y =x  в   y=-x
#xs=ys=list(range(100))
#figure, ax = plt.subplots(1)
#line, =ax.plot(xs,ys)
xs =list(range(100))
cpu_load = [0 for _in xs]
mem_load = [0 for _in xs]
figure, axes =plt.subplots(2)
line_cpu, = axes[0]
plt.ion()
plt.show()
def close(_):
    exit(0)
figure.canvas.mpl_connect('close_event', close)
step=1
while True:
    cpu_load.pop(0)
    mem_load.pop(0)
    current_cpu, current_mem = cpu_percent(), virtual_memory().percent
    cpu_load.append(current_cpu)
    mem_load.append(current_mem)
    line_cpu.set_color(get_color(current_cpu))
    line_cpu.set_ydata(cpu_load)
    line_mem.set_ydata(mem_load)
    figure.canvas.draw()
    figure.canvas.flush_events()


# %%
