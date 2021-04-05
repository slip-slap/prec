import numpy as np
import copy
import individual
import tool
import laminate_multiple_component as lmc
import lamina_mass_and_cost as lmac
import ga_constant_variable as GCV
import symmetry_list_operator as slo


#PARENTS_BY_FITNESS_PERCENT = 0.4
#PARENTS_BY_FITNESS_PERCENT = 0.0
#PROPER_PARENTS_PERCENT = 0.3

def get_fitness(ind):
    fitness = ind.mass
    #fitness = ind.cost
    #fitness = np.divide(ind.mass, 0.636) + np.divide(ind.cost, 23)
    #fitness = np.divide(ind.mass, 1.377) + np.divide(ind.cost, 80)
    #fitness = np.divide(ind.mass, 0.318) + np.divide(ind.cost, 12)
    #fitness = np.divide(ind.mass, 1.271) + np.divide(ind.cost, 105)
    return fitness

def get_combine_offspring_list(a_list, b_list,random_number):

    a_quarter_pos = int(len(a_list)/4 + 1) 
    a_half_pos    = int(len(a_list)/2 + 1)
    b_quarter_pos = int(len(b_list)/4 + 1)
    b_half_pos    = int(len(b_list)/2+ 1)
    if(random_number == 0):
        result = a_list[0:a_quarter_pos] + b_list[0:b_quarter_pos]
    if(random_number == 1):
        result = a_list[0:a_quarter_pos] + b_list[b_quarter_pos:b_half_pos]
    if(random_number == 2):
        result = a_list[a_quarter_pos:a_half_pos] + b_list[0:b_quarter_pos]
    if(random_number == 3):
        result = a_list[a_quarter_pos:a_half_pos] + b_list[b_quarter_pos:b_half_pos]

    if(np.mod(random_number, 2)== 0):
        return tool.get_symmetry_list(result)
    if(np.mod(random_number, 2)== 1):
        if(len(result) == 0):
            return tool.get_symmetry_list(a_list);
        mid_element = result[-1]
        rest = tool.get_symmetry_list(result[0:len(result)-1])
        rest.insert(len(result)-1,mid_element)
        return rest


    return tool.get_symmetry_list(result)

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
            #print(active_group[i])

        # potential group
        population2= copy.deepcopy(population)
        potential_group_ = [x for x in population2 if x.strength_raito
                < GCV.SAFETY_FACTOR]
        potential_group_.sort(key = lambda c:c.fitness, reverse=True)
        potential_group = potential_group_[0:int(num_parents * \
            GCV.POTENTIAL_GROUP)]
        for i in range(len(potential_group)):
            potential_group[i].flag = "potential_group"
            #print(potential_group[i])

        population3= copy.deepcopy(population)
        proper_group= [x for x in population3 if x.strength_raito >GCV.SAFETY_FACTOR][\
                0:int(num_parents * GCV.PROPER_PARENTS_PERCENT)]
        for i in range(len(proper_group)):
            proper_group[i].flag = "proper_group"
            #print(proper_group[i])

        return active_group + potential_group + proper_group;

    def crossover(self, parents, offspring_number):

        offspring = []
        while(len(offspring) < offspring_number):
        #for i in range(offspring_number):
            p1_pos = int(np.random.randint(0, len(parents), 1))
            p2_pos = int(np.random.randint(0, len(parents), 1))
            p1_angle_list    = parents[p1_pos].angle_list
            p2_angle_list    = parents[p2_pos].angle_list
            p1_height_list   = parents[p1_pos].height_list
            p2_height_list   = parents[p2_pos].height_list
            p1_material_list = parents[p1_pos].material_list
            p2_material_list = parents[p2_pos].material_list

            child = copy.deepcopy(parents[0])
            random_number = int(np.random.randint(0,4,1))
            child.angle_list  = get_combine_offspring_list(p1_angle_list, \
                    p2_angle_list,random_number)
            child.height_list = \
            get_combine_offspring_list(p1_height_list,p2_height_list,random_number)
            child.material_list = get_combine_offspring_list(p1_material_list, \
                    p2_material_list,random_number)
            child.strength_raito  = \
                lmc.get_strength_ratio(child.angle_list,child.height_list,child.material_list,GCV.LOAD)
            child.mass = \
                lmac.get_laminate_mass(child.height_list,child.material_list)
            child.cost = lmac.get_laminate_cost(child.material_list)
            child.fitness =  get_fitness(child);
            child.flag =""
            offspring.append(child)
        return offspring
            

    def mutation(self, offspring, mutation_percent=0.5):
        for i in range(len(offspring)):
            while True:
                #print("in the loop")
                if(offspring[i].flag=="active_group"):
                    continue
                offspring[i].angle_list = \
                    slo.get_chromosome_mutation_(offspring[i].angle_list,\
                                    offspring[i].strength_raito, GCV.ANGLE_CODE);
                offspring[i].material_list= \
                        slo.get_chromosome_mutation_(offspring[i].material_list,\
                        offspring[i].strength_raito,GCV.MATERIAL_CODE);
                assert len(offspring[i].angle_list) == len(offspring[i].material_list)
                offspring[i].height_list = \
                    len(offspring[i].angle_list)*[GCV.LAYER_HEIGHT]
                if(len(set(offspring[i].angle_list)) == 1):
                    if(len(offspring[i].angle_list) == 1):
                        break
                    offspring[i].angle_list[0] = GCV.ANGLE[0]
                    offspring[i].angle_list[1] = GCV.ANGLE[1]
                if(len(set(offspring[i].angle_list)) == 2):
                    break

if __name__ == "__main__":
    chromosome = [1,8,5,5,8,1]
    get_chromosome_mutation_(chromosome, 2)
    #get_chromosome_mutation([0,0,0,0,0],[12, 3])
    #a = [4,2.7,1,6,8]
    #a.sort(key = lambda c: np.abs(c-3))
    #print(a)

