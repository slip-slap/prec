import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import result_ind as result
import ga_constant_variable as cv

##################################
problem = 'Fitness'

fitness_low = np.subtract(0,result.coeff_low_fitness).tolist()
strength_raito_low = result.coeff_low_strength_ratio

#fitness_high = result.coeff_high_fitness_
#strength_raito_high = result.coeff_high_strength_ratio_

x_coordinate = range(1, len(fitness_low)+1,1)
fig, ax1 = plt.subplots()
color = 'tab:red'
color= 'k'
ax1.set_xlabel('generation (s)', fontsize=18)

ax1.set_ylabel(problem, color=color,fontsize=18)
ax1.set_ylim([min(fitness_low)-0.5,0])
ax1.plot(x_coordinate, fitness_low, color=color, label="fitness")
#ax1.plot(x_coordinate, fitness_high, color=color, label="fitness")
ax1.tick_params(axis='y', labelcolor=color)


"""
ax1.plot(x_coordinate, result.coeff_low_strength_ratio_, color=color)
ax1.plot(x_coordinate, result.coeff_mid_strength_ratio_, color=color)
ax1.plot(x_coordinate, result.coeff_high_strength_ratio_, color=color)
ax1.tick_params(axis='y', labelcolor=color)
"""

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'k'
ax2.set_ylabel('Strength ratio(SR)', color=color,fontsize=18)  # we already handled the x-label with ax1
ax2.set_ylim([0,3])
ax2.plot(x_coordinate, strength_raito_low, color=color, linestyle=':',label="SR")
#ax2.plot(x_coordinate, strength_raito_high, color=color, linestyle=':',label="SR")
#ax2.tick_params(axis='y', labelcolor=color)


fig.tight_layout()  # otherwise the right y-label is slightly clipped

custom_lines = [lines.Line2D([0],[0],color='black', linestyle='-'), lines.Line2D([0],[0],color='black', linestyle=':')]
plt.legend(custom_lines, [ 'Fitness','SR'],loc="upper right", bbox_to_anchor=[0.95,0.95], fontsize=12)
plt.annotate("1",xy=(29.5, 0.36), xytext=(29.5,0.8),arrowprops=dict(arrowstyle="->"))
plt.annotate("$1^{\prime}$",xy=(29.5, 1.9), xytext=(29.5,1.2),arrowprops=dict(arrowstyle="->"))
plt.annotate("2",xy=(56, 0.18), xytext=(58,0.8),arrowprops=dict(arrowstyle="->"))
plt.annotate("$2^{\prime}$",xy=(56, 2.01), xytext=(56,1.5),arrowprops=dict(arrowstyle="->"))
plt.annotate("3",xy=(79, 0.21), xytext=(80,0.7),arrowprops=dict(arrowstyle="->"))
plt.annotate("$3^{\prime}$",xy=(79, 2.0), xytext=(80,1.6),arrowprops=dict(arrowstyle="->"))
             
#plt.annotate("Load:      $N_{xy}=1e6$ N \nMaterial: GR",xy=(25,8.5),fontsize=13)
plt.axvline(36.5, 0.05, 0.68,c='k',linestyle='dashed')
plt.rcParams.update({'font.size': 18})

plt.show()
