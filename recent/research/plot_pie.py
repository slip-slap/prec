import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Perentage of    \nactive individuals ', 'Perentage of      \npotential individuals  ','   Percentage of   \nproper individuals ']
sizes = [30, 30, 40]
#explode = (0, 0.1, 0 )  # only "explode" the 2nd slice (i.e. 'Hogs')
explode = (0, 0, 0 )  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
cmap = plt.get_cmap("Greys")

ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90, colors=cmap(np.array([50, 120, 200])))
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
