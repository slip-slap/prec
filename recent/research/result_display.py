import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
#import selection_method_comparsion_result as result
import main_result as result
import constant_variable as cv

##################################
problem = 'fitness(problem I)'

fitness = result.coeff_high_fitness_
strength_raito = result.coeff_high_strength_ratio_
active_group= result.coeff_high_active_group_number
potential_group = result.coeff_high_potential_group_number
proper_group = result.coeff_high_proper_group_number

#fitness = result.coeff_mid_fitness_
#strength_raito = result.coeff_mid_strength_ratio_
#fitness = result.coeff_low_fitness_
#strength_raito = result.coeff_low_strength_ratio_

x_coordinate = list(np.arange(1,cv.GA_RUNTIMES+1,1))
fig, ax1 = plt.subplots()
color = 'tab:red'
color= 'k'
ax1.set_xlabel('generation (s)', fontsize=18)

ax1.set_ylabel(problem, color=color,fontsize=18)
#ax1.set_ylim([0,max(fitness)+2])
#ax1.set_ylim([0,max(proper_group)+2])
#ax1.set_ylim([0,max(fitness)+2])
ax1.set_ylim([0,10])
#ax1.plot(x_coordinate, fitness, color=color, label="fitness")
ax1.plot(x_coordinate, active_group, color=color, linestyle='dotted')
ax1.plot(x_coordinate, potential_group, color=color, linestyle='dashed')
ax1.plot(x_coordinate, proper_group, color=color,linestyle='solid')
ax1.tick_params(axis='y', labelcolor=color)

custom_lines = [lines.Line2D([0],[0],color='black',linestyle='dotted'),
                        lines.Line2D([0],[0],color='black',linestyle='dashed'),
                        lines.Line2D([0],[0],color='black',linestyle='solid')]

"""
ax1.plot(x_coordinate, result.coeff_low_strength_ratio_, color=color)
ax1.plot(x_coordinate, result.coeff_mid_strength_ratio_, color=color)
ax1.plot(x_coordinate, result.coeff_high_strength_ratio_, color=color)
ax1.tick_params(axis='y', labelcolor=color)
"""

#ax1.legend(custom_lines_fitness,['$\sigma=5$','coeff='],loc='right', 
#        bbox_to_anchor=[1,0.1],fontsize=13,)
"""
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'k'
ax2.set_ylabel('strength ratio(SR)', color=color,fontsize=18)  # we already handled the x-label with ax1
ax2.set_ylim([0,3])
ax2.plot(x_coordinate, strength_raito, color=color,
        linestyle=':',label="SR")
#ax2.tick_params(axis='y', labelcolor=color)


custom_lines = [lines.Line2D([0],[0],color='black', linestyle='-'),
                lines.Line2D([0],[0],color='black', linestyle=':')]
fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.annotate("Load:      $N_{xy}=1e6$ N \nMaterial: GR",xy=(25,8.5),fontsize=13)
#plt.annotate("$\sigma=8$",xy=(25,2.5),fontsize=13)
#plt.annotate("$\sigma_2=3$",xy=(12,4.2),fontsize=13)
#plt.annotate("$\sigma_3=0.5$",xy=(15,3),fontsize=13)

"""
plt.legend(custom_lines,['Number of active individual','Number of potential individual', 'Number of proper individual'],loc="upper right",
                        bbox_to_anchor=[0.9,0.3], fontsize=13)
plt.rcParams.update({'font.size': 18})

plt.show()
