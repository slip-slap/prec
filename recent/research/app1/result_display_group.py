import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
#import selection_method_comparsion_result as result
import result 
import ga_constant_variable as cv

##################################
problem = 'Number'

fitness = result.coeff_low_fitness_
strength_raito = result.coeff_low_strength_ratio_
active_group= result.coeff_low_active_group_number
potential_group = result.coeff_low_potential_group_number
proper_group = result.coeff_low_proper_group_number

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
ax1.set_ylim([0,max(proper_group)+2])
ax1.plot(x_coordinate, proper_group, color=color,linestyle='solid')
ax1.plot(x_coordinate, potential_group, color=color, linestyle='dashed')
ax1.plot(x_coordinate, active_group, color=color, linestyle='dotted')
ax1.tick_params(axis='y', labelcolor=color)

custom_lines = [lines.Line2D([0],[0],color='black',linestyle='solid'),
                        lines.Line2D([0],[0],color='black',linestyle='dashed'),
                        lines.Line2D([0],[0],color='black',linestyle='dotted')]

"""
ax1.plot(x_coordinate, result.coeff_low_strength_ratio_, color=color)
ax1.plot(x_coordinate, result.coeff_mid_strength_ratio_, color=color)
ax1.plot(x_coordinate, result.coeff_high_strength_ratio_, color=color)
ax1.tick_params(axis='y', labelcolor=color)
"""

#ax1.legend(custom_lines_fitness,['$\sigma=5$','coeff='],loc='right', 
#        bbox_to_anchor=[1,0.1],fontsize=13,)
plt.legend(custom_lines,[ 'Number of proper individuals','Number of potential individuals','Number of active individuals'],loc="upper right",
                        bbox_to_anchor=[0.7,0.3], fontsize=12)
plt.rcParams.update({'font.size': 18})

plt.show()
