import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as lines

def my_plot(data_x, data_y):
    fig = plt.figure()
    axes1 = fig.add_subplot()
    axes1.set_xlabel("Generation", fontsize=22)
    axes1.set_ylabel("Fitness", fontsize=22)
    axes1.set_xlim(1,12)
    axes1.plot(data_x, data_y,color='black')
    plt.yticks(np.arange(4.5,6.5,1.5))

    ax1_2 = axes1.twinx()  
    ax1_2.set_ylabel('Error', fontsize=22)  
    ax1_2.plot(data_x, np.divide(1,data_y), color='black', linestyle="--") 
    ax1_2.set_yticks(np.arange(0.1,0.4,0.1))
    custom_lines = [lines.Line2D([0],[0],linestyle='solid',color='black'),
                        lines.Line2D([0],[0],linestyle='dashed',color='black')]
    plt.legend(custom_lines,['Fitness', 'Error'],loc="upper right",
                        bbox_to_anchor=[0.95,0.95], fontsize=18)
    plt.show()

if __name__=="__main__":
    x_data = range(1,11,1)
    y_data=[0.20715496, 0.19046323, 0.18901621, 0.1887618, 0.18860738, 0.18846482, 0.18832617,
  0.18819045, 0.1880573, 0.18792664]
    my_plot(x_data, np.divide(1,y_data))
