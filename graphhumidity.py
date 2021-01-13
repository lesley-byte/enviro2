from requests import get
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys =[]

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

def animate(i, xs, ys):
    humidity = bme280.get_humidity()
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(humidity)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs, ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('humidity over time')
    plt.ylabel("humidity percent")
    
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=60000)
plt.show()



