import numpy as np

import matplotlib.pyplot as plt

import matplotlib

matplotlib.rcParams['font.family']='SimHei'

matplotlib.rcParams['font.sans-serif']=['SimHei']

plt.figure(figsize=(8,4))

plt.subplot(2,2,1)

x=np.linspace(0,5,50)

y=np.cos(2*np.pi*x)*np.exp(-x)

plt.plot(x,y,'',linewidth=3,linestyle='-')

plt.scatter(x,y)

plt.title('2-1-1 subplots-区域')

plt.ylabel('衰减的震荡')

#plt.xlabel('时间（s）')

plt.subplot(2,2,3)

x=np.linspace(0.00,2.00,40)

y=np.sin(2*np.pi*x)

plt.plot(x,y,'',linewidth=3,linestyle='-')

plt.scatter(x,y)

plt.title('2-1-2 subplots-区域')

plt.ylabel('sin函数')

plt.xlabel('时间（s）')

new_ticks1 = np.linspace(0,2,9)

plt.xticks(new_ticks1)

plt.show()

