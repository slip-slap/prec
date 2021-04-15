import numpy as np
import copy

import individual
import laminate_multiple_component as lmc
import lamina_mass_and_cost as lmac
import ga_constant_variable as GCV
import app1_tool


#PARENTS_BY_FITNESS_PERCENT = 0.4
#PARENTS_BY_FITNESS_PERCENT = 0.0
#PROPER_PARENTS_PERCENT = 0.3

def get_fitness(ind):
    fitness = ind.mass
    return fitness

class Genetic_Algorithm(object):

    """Docstring for Genetic_Algorithm. """

    def __init__(self):
        """TODO: to be defined. """
        pass

    def select_parents(self, population,  num_parents):
        # select parents according to fitness
        population1= copy.deepcopy(population)
        population1.sort(key = lambda c: c.fitness)
        active_group= population1[0:int(num_parents * GCV.ACTIVE_GROUP)]
        for i in range(len(active_group)):
            active_group[i].flag = "active_group"

        # potential group
        population2= copy.deepcopy(population)
        potential_group_ = [x for x in population2 if x.strength_raito < GCV.SAFETY_FACTOR]
        potential_group_.sort(key = lambda c:c.strength_raito, reverse=True)
        potential_group = potential_group_[0:int(num_parents * GCV.POTENTIAL_GROUP)]
        for i in range(len(potential_group)):
            potential_group[i].flag = "potential_group"

        population3= copy.deepcopy(population)
        proper_group= [x for x in population3 if x.strength_raito >GCV.SAFETY_FACTOR][\
                0:int(num_parents * GCV.PROPER_PARENTS_PERCENT)]
        for i in range(len(proper_group)):
            proper_group[i].flag = "proper_group"

        return active_group + potential_group + proper_group;

    def crossover(self, parents, offspring_number):
        offspring = []
        while(len(offspring) < offspring_number):
            p1_pos = int(np.random.randint(0, len(parents), 1))
            p2_pos = int(np.random.randint(0, len(parents), 1))
            p1_angle_list    = copy.deepcopy(parents[p1_pos].angle_list)
            p2_angle_list    = copy.deepcopy(parents[p2_pos].angle_list)
            child = copy.deepcopy(parents[0])
            random_number = int(np.random.randint(0,4,1))
            child.angle_list  = app1_tool.list_cross_over(p1_angle_list, p2_angle_list, random_number)
            if(len(set(child.angle_list))==1):
                child.angle_list = app1_tool.modify_one_element_list(child.angle_list)
            child.height_list = [GCV.LAYER_HEIGHT] * len(child.angle_list)
            child.material_list = [GCV.MATERIAL[0]] * len(child.angle_list) 
            child.strength_raito= lmc.get_strength_ratio(child.angle_list,child.height_list,child.material_list,GCV.LOAD)
            child.mass = lmac.get_laminate_mass(child.height_list,child.material_list)
            child.cost = lmac.get_laminate_cost(child.material_list)
            child.fitness =  get_fitness(child);
            child.flag =""
            offspring.append(child)
        return offspring
            

    def mutation(self, offspring, mutation_percent=0.5):
        for i in range(len(offspring)):
            if(GCV.SAFETY_FACTOR > offspring[i].strength_raito):
                number = int(GCV.MUTATION_EFFICIENT * (GCV.SAFETY_FACTOR - offspring[i].strength_raito)) + 2
                offspring[i].angle_list = app1_tool.increase_list_length(offspring[i].angle_list, number)
                offspring[i].angle_list = app1_tool.random_change_list_content(offspring[i].angle_list)
                if(len(set(offspring[i].angle_list))==1):
                    offspring[i].angle_list = app1_tool.modify_one_element_list(offspring[i].angle_list)
                offspring[i].material_list =len(offspring[i].angle_list) * [offspring[i].material_list[0]]
                offspring[i].height_list   = len(offspring[i].angle_list)*[GCV.LAYER_HEIGHT]
            if(GCV.SAFETY_FACTOR < offspring[i].strength_raito):
                number = int(GCV.MUTATION_EFFICIENT * (offspring[i].strength_raito - GCV.SAFETY_FACTOR)) + 2
                offspring[i].angle_list = app1_tool.reduce_list_length(offspring[i].angle_list, number)
                offspring[i].angle_list = app1_tool.random_change_list_content(offspring[i].angle_list)
                if(len(set(offspring[i].angle_list))==1):
                    offspring[i].angle_list = app1_tool.modify_one_element_list(offspring[i].angle_list)
                offspring[i].material_list =len(offspring[i].angle_list) * [offspring[i].material_list[0]]
                offspring[i].height_list   = len(offspring[i].angle_list)*[GCV.LAYER_HEIGHT]


if __name__ == "__main__":
    chromosome = [1,8,5,5,8,1]
    get_chromosome_mutation_(chromosome, 2)
    #get_chromosome_mutation([0,0,0,0,0],[12, 3])
    #a = [4,2.7,1,6,8]
    #a.sort(key = lambda c: np.abs(c-3))
    #print(a)

