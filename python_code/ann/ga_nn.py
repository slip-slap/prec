import numpy as np
import yaml

import configuration_ga as CGA
import individual  
import tool_ga 
import genetic_algorithm as ga



CONFIGURATION = None;
with open('configuration.yaml') as input_stream:
    CONFIGURATION = yaml.load(input_stream, Loader=yaml.FullLoader)

def initilize_population():
    """TODO: Docstring for initize_population.
    :arg1: TODO
    :returns: initilize population
    """
    individual_list = list()
    for i in range(CGA.POPUPATION):
        node_number = np.random.randint(CGA.NODE_NUMBER_OF_HIDDEN_LAYER_LOWER_BOUND,CGA.NODE_NUMBER_OF_HIDDEN_LAYER_UPPER_BOUND,1)[0]
        temp_individual = individual.Individual()
        temp_individual.connection_gene = tool_ga.get_connection_gene(node_number)
        temp_individual.activation_function_gene = tool_ga.get_activation_function_gene(node_number)
        temp_individual.model_save_path = CONFIGURATION['SAVING_PLACE_OF_TRAINING_MODEL'] + "/model" + str(i)+ "/model"
        temp_individual.model_traing_process_path = CONFIGURATION['SAVING_PLACE_OF_TRAINING_PROCESS']+ "/log"+  str(i) + "/model"
        temp_individual.calculate_individual_fitness()
        individual_list.append(temp_individual)
        print(temp_individual)
    return individual_list

#if __name__ == "__main__":
#    initilize_population()

            
my_ga = ga.Genetic_Algorithm()
population = initilize_population()
population.sort(key = lambda c: c.fitness)

previous_fitness = 0 
current_fitness = population[0].fitness
print("current_fitness "+str(current_fitness))

while(current_fitness-previous_fitness>0.001):
    parents = my_ga.select_parents(population,int(CGA.POPUPATION * CGA.PARENT_PERCENT))
    offspring = my_ga.crossover(parents, CGA.POPUPATION - len(parents))
    my_ga.mutation(offspring)
    for i in range(len(offspring)):
        offspring[i].fitness = offspring[i].calculate_individual_fitness()
    population[0:int(CGA.POPUPATION * CGA.PARENT_PERCENT)] = parents
    population[CGA.POPUPATION - len(parents):] = offspring
    population.sort(key = lambda c: c.fitness)

    previous_fitness = current_fitness
    current_fitness = population[0].fitness
    print(population[0])

    for i in range(1):
        with open("network_train_result.txt","a") as train_handler:
                train_handler.write("ANN model:")
                train_handler.write("\n")
                train_handler.write("active function: " + str(population[0].activation_function_gene))
                train_handler.write("\n")
                train_handler.write("connection:  " + str(population[0].connection_gene))
                train_handler.write("\n")
                train_handler.write("fitness:  " + str(population[0].fitness))
                train_handler.write("\n")
                train_handler.write("model_save_path:  " + str(population[0].model_save_path))
                train_handler.write("\n")
                train_handler.write("model_traing_process_path:  " + str(population[0].model_traing_process_path))


                    


#data_x = np.arange(0,1,0.01) 

"""
def binary_to_decimal(binary_number):
    decimal = 0
    for i in range(len(binary_number)):
        decimal = decimal + binary_number[i]*np.power(2,len(binary_number)-i-1)
    return int(decimal)

def activation_function_name(activation_function_code):
    if(activation_function_code == 0):
        return "sigmoid"
    if(activation_function_code == 1):
        return "relu"
    if(activation_function_code == 2):
        return "tanh"
    if(activation_function_code == 3):
        return "softmax"


def chromosome_to_gene_list(chromosome,unit_length):
    gene_number = len(chromosome)/unit_length
    gene_list= list()
    i = 0
    while(i<gene_number):
        temp = chromosome[i:i+unit_length]
        gene_list.append(temp)
        i=i+1
    return gene_list
"""

