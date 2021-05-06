import matplotlib.pyplot as plt
import numpy as np

def my_plot(data_x, data_y):
    fig = plt.figure(111)
    axes1 = fig.add_subplot(111)
    axes1.plot(data_x,data_y,color='black')
    axes1.set_xlabel("generation")
    axes1.set_ylabel("fitness")
    axes1.set_xlim(1,12)
    axes1.scatter(data_x, data_y, color='black')
    plt.yticks(np.arange(4,7,1))
    plt.show()

if __name__=="__main__":
    x_data = range(1,11,1)
    y_data=[0.20715496, 0.19046323, 0.18901621, 0.1887618, 0.18860738, 0.18846482, 0.18832617,
  0.18819045, 0.1880573, 0.18792664]
    my_plot(x_data, np.divide(1,y_data))
