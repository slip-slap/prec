import sys
sys.path.insert(1,"/Users/kismet/Documents/github/prec/recent/research/module1")

import individual as ind
import copy
import numpy as np
import laminate_multiple_component as lmc
import lamina_mass_and_cost as lmac
import ga_constant_variable as GCV
import genetic_algorithm as my_ga
import collections


def get_fitness(ind):
    fitness = ind.mass
    return fitness

def get_angle_list(length):
    angle_list = []; 
    for k in range(length):
        random_angle_pos = int(np.random.randint(low=0,high=len(GCV.ANGLE),size=1))
        random_material_pos = int(np.random.randint(low=0,high=len(GCV.MATERIAL),size=1))
        angle_list.append(GCV.ANGLE[random_angle_pos])
    if(len(set(angle_list)) == 1):
        angle_list = app1_tool.modify_one_element_list(angle_list)
    return angle_list 


def get_laminate_individual(length):
    angle_list = get_angle_list(length) 
    height_list = [GCV.LAYER_HEIGHT] * len(angle_list)
    material_list = [GCV.MATERIAL[0]] * len(angle_list) 
    temp_ind = ind.Individual(angle_list,height_list,material_list)
    temp_ind.strength_raito =  lmc.get_strength_ratio(angle_list, height_list, material_list, GCV.LOAD)
    temp_ind.mass = lmac.get_laminate_mass(height_list,material_list)
    temp_ind.cost = lmac.get_laminate_cost(material_list)
    temp_ind.fitness = get_fitness(temp_ind)
    return temp_ind

def get_initial_population():
    #np.random.seed(0)
    initial_population = []
    while(len(initial_population)<GCV.POPULATION_NUMBER):
        length = int(np.random.randint(low=GCV.CHROMOSOME_LENGTH_LOWER_BOUND, high=GCV.CHROMOSOME_LENGTH_UPPER_BOUND, size=1))
        temp_ind = get_laminate_individual(length)
        initial_population.append(temp_ind)
    return initial_population


def save_to_output(result_fitness, result_strength_ratio, \
        my_best_individual,result_active_group, result_potential_group, \
        result_proper_group,result_number_angle0, result_number_angle90):

    dict_result =  dict(collections.Counter(my_best_individual.angle_list))
    number_of_angle_0 = 0
    number_of_angle_90 = 0
    for key in dict_result:
        if(key==0):
            number_of_angle_0 = dict_result[key]
        else:
            number_of_angle_90 = dict_result[key]

    with open("result.py","a") as result_handler:
        result_handler.write("##################################")
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_value=  " + str(GCV.MUTATION_EFFICIENT))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_load=  " + str(GCV.LOAD))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_material=  " + str(GCV.MATERIAL))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_angle=  " + str(GCV.ANGLE))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_fitness_ =  " + str(result_fitness))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_strength_ratio_= "+ str(result_strength_ratio))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_cost= "+ str(my_best_individual.cost))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_mass= "+ str(my_best_individual.mass))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_strength_raito= "+ str(my_best_individual.strength_raito))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_number_of_layer= "+ str(len(my_best_individual.material_list)))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_result_number_angle0= "+ str(result_number_angle0))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_result_number_angle90= "+ str(result_number_angle90))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) \
                +"_active_group_number= "+ str(result_active_group))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) \
                +"_potential_group_number= "+ str(result_potential_group))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) \
                +"_proper_group_number= "+ str(result_proper_group))
        result_handler.write("\n")
        result_handler.write("number_of_angle_90= "+ str(number_of_angle_90))
        result_handler.write("\n")
        result_handler.write("number_of_angle_0= "+ str(number_of_angle_0))
        result_handler.write("\n")

        stacking_sequence = []
        angle_list_copy = copy.deepcopy(my_best_individual.angle_list)
        for i in range(len(angle_list_copy)):
            angle_list_copy[i] = get_concerter_angle(angle_list_copy[i])
        for i in range(len(angle_list_copy)):
            stacking_sequence.append(angle_list_copy[i])
            stacking_sequence.append(my_best_individual.material_list[i])
        result_handler.write("#stacking sequence= "+ str(stacking_sequence))
        result_handler.write("\n")
        result_handler.write("##################################")
        result_handler.write("\n")

def crossover_and_mutation(ga, parents, number_of_offspring):
    offspring = ga.crossover(parents, number_of_offspring)
    ga.mutation(offspring)
    for i in range(len(offspring)):
        offspring[i].strength_raito  = \
            lmc.get_strength_ratio(offspring[i].angle_list,offspring[i].height_list,offspring[i].material_list,GCV.LOAD)
        offspring[i].mass = \
            lmac.get_laminate_mass(offspring[i].height_list,offspring[i].material_list)
        offspring[i].cost = lmac.get_laminate_cost(offspring[i].material_list)
        offspring[i].fitness =  get_fitness(offspring[i]);
    return offspring;

def GA():
    result_fitness  = []
    result_times = []
    result_strength_ratio = []
    result_active_group = []
    result_potential_group = []
    result_proper_group = []
    result_number_angle0 = []
    result_number_angle90 = []
    print("loading             : "+str(GCV.LOAD))
    print("mutation coefficient: "+str(GCV.MUTATION_EFFICIENT))
    population = get_initial_population()
    population.sort(key = lambda c: c.fitness)

    best_individual_pos = tool.get_safety_factor_pos_flag(population)
    current_fitness = population[best_individual_pos].fitness

    print("initial fitness: " + str(current_fitness) + " strength_raito " + \
                str(population[best_individual_pos].strength_raito))

    result_fitness.append(current_fitness)
    result_times.append(1)
    result_strength_ratio.append(population[best_individual_pos].strength_raito)
    
    ga = my_ga.Genetic_Algorithm()
    d = 0
    while( d<GCV.GA_RUNTIMES ):
#        break;
        d = d+1 
        active_group_number = 0;
        potential_group_number = 0;
        proper_group_number = 0;
        parents = ga.select_parents(population,int(GCV.POPULATION_NUMBER * GCV.ELITIST_PERCENT))
        offspring = crossover_and_mutation(ga, parents, int(GCV.POPULATION_NUMBER*(1 - GCV.ELITIST_PERCENT)));
        number_of_vacant_spot = GCV.POPULATION_NUMBER - len(offspring) - len(parents)
        vacant_offspring = []
        if(number_of_vacant_spot > 0):
            vacant_offspring = crossover_and_mutation(ga, parents, number_of_vacant_spot);

        population[0:len(parents)] = parents
        population[len(parents):len(parents)+len(offspring)] = offspring
        population[GCV.POPULATION_NUMBER - number_of_vacant_spot:] = vacant_offspring;

        population.sort(key = lambda c: c.fitness)

        #print("curent fitness: " + str(current_fitness) + " strength_raito " + \
        #        str(population[best_individual].strength_raito))
        print(population[best_individual])

    return  {'fitness':result_fitness, 'strength_raito':result_strength_ratio, \
            'best_individual':population[best_individual], 'active_group':result_active_group, \
            'potential_group':result_potential_group, 'proper_group':result_proper_group, \
            'number_of_angle0':result_number_angle0, 'number_of_angle90':result_number_angle90}



if __name__ == "__main__":
    RUN_BATCH = 50 
    result_fitness  = [0]
    result_strength_ratio = [0]
    total_sr = 0
    total_mass = 0
    total_cost = 0
    total_layer = 0
    best_mass = 1000000
    best = []
    worst_mass = -1000000
    best = []
    for i in range(RUN_BATCH):
        one_time = GA()
        if(one_time['best_individual'].mass < best_mass):
            best_mass = one_time['best_individual'].mass
            best = one_time['best_individual']
        if(one_time['best_individual'].mass > worst_mass):
            worst_mass = one_time['best_individual'].mass
            worst = one_time['best_individual']
        total_sr = total_sr + one_time['best_individual'].strength_raito
        total_mass = total_mass + one_time['best_individual'].mass
        total_cost = total_cost + one_time['best_individual'].cost
        total_layer = total_layer + len(one_time['best_individual'].material_list)
        result_fitness = np.add(result_fitness, one_time['fitness'])
        result_strength_ratio = np.add(result_strength_ratio, one_time['strength_raito'])
    save_individual(best)
    save_individual(worst)

                    

"""
save_to_output(one_time['fitness'], one_time['strength_raito'], one_time['best_individual'], 
               one_time['active_group'],one_time['potential_group'],one_time['proper_group'],
               one_time['number_of_angle0'],one_time['number_of_angle90'])
"""
