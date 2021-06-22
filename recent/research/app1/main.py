import sys
sys.path.insert(1,"/Users/kismet/Documents/github/prec/recent/research/module1")
import copy
import numpy as np
import collections

import individual as ind
import laminate_multiple_component as lmc
import lamina_mass_and_cost as lmac
import ga_constant_variable as GCV
import genetic_algorithm as my_ga
import app1_tool

def counter_item(a):
    if(isinstance(a,list)==False):
        print("input argument is not a list")
        return
    if(len(a)==0):
        print("element length is zero")
        return
    return  dict(collections.Counter(a))

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

def crossover_and_mutation(ga, parents, number_of_offspring):
    offspring = ga.crossover(parents, number_of_offspring)
    ga.mutation(offspring)
    for i in range(len(offspring)):
        offspring[i].strength_raito  = lmc.get_strength_ratio(offspring[i].angle_list,offspring[i].height_list,offspring[i].material_list,GCV.LOAD)
        offspring[i].mass = lmac.get_laminate_mass(offspring[i].height_list,offspring[i].material_list)
        offspring[i].cost = lmac.get_laminate_cost(offspring[i].material_list)
        offspring[i].fitness =  get_fitness(offspring[i]);
    return offspring;

def get_population_strength_ratio(population):
    strength_ratio = []
    for i in range(len(population)):
        strength_ratio.append(population[i].strength_raito)
    return strength_ratio

def get_active_potential_proper_group_number(population,ga_active_group, ga_potential_group, ga_proper_group):
    active_group_number = 0
    potential_group_number = 0
    proper_group_number = 0
    for i in range(len(population)):
        if(population[i].flag == "active_group"):
            active_group_number = active_group_number + 1;
        if(population[i].flag == "potential_group"):
            potential_group_number = potential_group_number+ 1;
        if(population[i].flag == "proper_group"):
            proper_group_number = proper_group_number + 1;
    ga_active_group.append(active_group_number) 
    ga_potential_group.append(potential_group_number)
    ga_proper_group.append(proper_group_number)

def get_best_individual_fitness_and_strength_ratio(ind, ga_fitness, ga_strength_ratio, ga_number_angle0, ga_number_angle90):
    ga_fitness.append(ind.fitness)
    ga_strength_ratio.append(ind.strength_raito)
    dict_result =  dict(collections.Counter(ind.angle_list))
    for key in dict_result:
        if(key==0):
            ga_number_angle0.append(dict_result[key])
        else:
            ga_number_angle90.append(dict_result[key])


def GA(ga_active_group,ga_potential_group,ga_proper_group,ga_fitness,ga_strength_ratio,ga_number_angle0, ga_number_angle90):
    population = get_initial_population()
    population.sort(key = lambda c: c.fitness)
    best_individual_pos = app1_tool.get_specified_value_pos(get_population_strength_ratio(population), GCV.SAFETY_FACTOR,population)
    ga = my_ga.Genetic_Algorithm()
    d = 0
    while( d<GCV.GA_RUNTIMES ):
        d = d+1 
        parents = ga.select_parents(population,int(GCV.POPULATION_NUMBER * GCV.ELITIST_PERCENT))
        get_active_potential_proper_group_number(parents,ga_active_group, ga_potential_group, ga_proper_group)
        offspring = crossover_and_mutation(ga, parents, int(GCV.POPULATION_NUMBER*(1 - GCV.ELITIST_PERCENT)));
        number_of_vacant_spot = GCV.POPULATION_NUMBER - len(offspring) - len(parents)
        vacant_offspring = []
        if(number_of_vacant_spot > 0):
            vacant_offspring = crossover_and_mutation(ga, parents, number_of_vacant_spot);
        population[0:len(parents)] = parents
        population[len(parents):len(parents)+len(offspring)] = offspring
        population[GCV.POPULATION_NUMBER - number_of_vacant_spot:] = vacant_offspring;
        population.sort(key = lambda c: c.fitness)
        best_individual = app1_tool.get_specified_value_pos(get_population_strength_ratio(population), GCV.SAFETY_FACTOR,population)
        print("best: "+ str(population[best_individual]))
        get_best_individual_fitness_and_strength_ratio(population[best_individual],ga_fitness, ga_strength_ratio,ga_number_angle0, ga_number_angle90)
    return population[best_individual]

def average_ga(times):
    total_fitness  = [0]; total_strength_ratio = [0]; total_sr = 0; total_mass= 0; total_cost = 0; total_layer = 0;
    best_mass = 1000000;   best = []
    worst_mass = -1000000; best = []
    for i in range(times):
        ga_active_group=[]; ga_potential_group=[]; ga_proper_group=[];
        ga_fitness=[]; ga_strength_ratio=[]; ga_number_angle0=[]; ga_number_angle90=[];
        ind = GA(ga_active_group,ga_potential_group,ga_proper_group,ga_fitness,ga_strength_ratio,ga_number_angle0, ga_number_angle90)
        if(ind.strength_raito < GCV.SAFETY_FACTOR):
            continue
        if(ind.mass < best_mass):
            best_mass = ind.mass
            best = ind
        if(ind.mass > worst_mass):
            worst_mass = ind.mass
            worst = ind 
        total_sr = total_sr + ind.strength_raito
        total_mass = total_mass + ind.mass
        total_cost = total_cost + ind.cost
        total_layer = total_layer + len(ind.material_list)
        total_fitness = np.add(total_fitness, ga_fitness)
        total_strength_ratio = np.add(total_strength_ratio, ga_strength_ratio)
        print('----------------------------------------')
    app1_tool.save_individual(worst)
    app1_tool.save_individual(best)
    app1_tool.save_average_result(total_fitness,total_strength_ratio, total_sr, total_mass,total_cost, total_layer,times)
    
if __name__ == "__main__":
   average_ga(10)
                    

