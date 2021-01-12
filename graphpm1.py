from requests import get
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

import time
from pms5003 import PMS5003, ReadTimeoutError as pmsReadTimeoutError


try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys =[]

pms5003 = PMS5003()

def animate(i, xs, ys):

    try:
        data = pms5003.read()
    except pmsReadTimeoutError:
        logging.warning("Failed to read PMS5003")
    else:
        data = float(data.pm_ug_per_m3(1.0))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(data)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs, ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('pm1 over time')
    plt.ylabel("pm1 ug/m3 ")
    
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()



