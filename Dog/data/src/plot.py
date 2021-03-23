import matplotlib.pyplot as plt
import pandas as pd


def draw_stock_plot(stock_code="000820"):
    stock_dataframe = pd.read_csv("data/"+ stock_code + ".csv")
    fig, axes = plt.subplots()
    axes.plot(stock_dataframe["date"].tolist(), stock_dataframe["open"].tolist())
    plt.show()

draw_stock_plot()
"""
mean = statistics.mean(open_list)
variance = statistics.variance(open_list)
print("mean: "+ str(mean))
print("variance: "+ str(variance))
"""



#'date' 'open'  'high'  'low'  'close'  'volume'  'adjclose' 


