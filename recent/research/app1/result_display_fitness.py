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

#ax1.legend(custom_lines_fitness,['$\sigma=5$','coeff='],loc='right', 
#        bbox_to_anchor=[1,0.1],fontsize=13,)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'k'
ax2.set_ylabel('Strength ratio(SR)', color=color,fontsize=18)  # we already handled the x-label with ax1
ax2.set_ylim([0,3])
ax2.plot(x_coordinate, strength_raito_low, color=color, linestyle=':',label="SR")
#ax2.plot(x_coordinate, strength_raito_high, color=color, linestyle=':',label="SR")
#ax2.tick_params(axis='y', labelcolor=color)


custom_lines = [lines.Line2D([0],[0],color='black', linestyle='-'),
                lines.Line2D([0],[0],color='black', linestyle=':')]
fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.annotate("Load:      $N_{xy}=1e6$ N \nMaterial: GR",xy=(25,8.5),fontsize=13)
"""
#plt.annotate("$\sigma=8$",xy=(25,2.5),fontsize=13)
#plt.annotate("$\sigma_2=3$",xy=(12,4.2),fontsize=13)
#plt.annotate("$\sigma_3=0.5$",xy=(15,3),fontsize=13)

"""
plt.axvline(4,-3, 2,c='k',linestyle=':')
plt.rcParams.update({'font.size': 18})

plt.show()
