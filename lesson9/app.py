import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

data=pd.read_csv('currencyes.csv')
x,ax=plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.grid(True)
ax.set_xlabel('dates')
ax.set_ylabel('value')
ax.plot(data['dates'],data['source1_val'])
ax.plot(data['dates'],data['source2_val'])
plt.show()