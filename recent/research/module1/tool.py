import numpy as np
import copy

import ga_constant_variable as GCV


def get_safety_factor_pos_flag(population):
    safety_factor_pos_flag = -1
    max_strength_ratio = -1
    max_strength_ratio_pos = -1000
    for i in range(len(population)):
        if(population[i].strength_raito > max_strength_ratio):
            max_strength_ratio = population[i].strength_raito
            max_strength_ratio_pos = i

        if(population[i].strength_raito > GCV.SAFETY_FACTOR):
            safety_factor_pos_flag = i
            break

    if(safety_factor_pos_flag == -1):
        print("no strength_raito is great then specified safety factor")
        safety_factor_pos_flag = max_strength_ratio_pos
    return safety_factor_pos_flag

def get_symmetry_list(half_list):
    upper_half = copy.deepcopy(half_list)
    half_list.reverse()
    return upper_half + half_list


if __name__ == '__main__':

    #ma=[-45{gr_9} 45{gr_9}     -45 {ca_2}    45 {ca_2}
                 

    get_positive(angle)



