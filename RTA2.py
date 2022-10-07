%matplotlib notebook
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [9.8, 6]
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates

plt.style.use('fivethirtyeight')

index = count()

def animate(i):
    dane = pd.read_csv("real time stock data.csv")
    
    x = dane['Date']
    y1 = dane['AAPL']
    
    plt.cla()

    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    plt.xticks(rotation=90, size=7)
    plt.yticks(size=10)
    plt.title('Price History')
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Price USD ($)',fontsize=15)
    plt.plot(x, y1, label='AAPL', linewidth=1)

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()