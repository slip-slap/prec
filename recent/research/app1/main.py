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

def GA():
    print("loading             : "+str(GCV.LOAD))
    print("mutation coefficient: "+str(GCV.MUTATION_EFFICIENT))
    population = get_initial_population()
    population.sort(key = lambda c: c.fitness)
    best_individual_pos = app1_tool.get_safety_factor_pos_flag(population)
    current_fitness = population[best_individual_pos].fitness
    print("initial fitness: " + str(current_fitness) + " strength_raito " + str(population[best_individual_pos].strength_raito))
    ga = my_ga.Genetic_Algorithm()
    d = 0
    while( d<GCV.GA_RUNTIMES ):
        d = d+1 
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
        best_individual = app1_tool.get_safety_factor_pos_flag(population)
        for i in range(len(population)):
            print(population[i])
        print("best: "+ str(population[best_individual]))

if __name__ == "__main__":
    GA()
                    

