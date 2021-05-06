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

def save_best_ind(population):
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
            train_handler.write("\n")
            train_handler.write("#########################################################################")


if __name__ == "__main__":
    my_ga = ga.Genetic_Algorithm()
    population = initilize_population()
    population.sort(key = lambda c: c.fitness)

    round_counter = 0
    while(round_counter < 10):
        print("GA round")
        round_counter + 1
        parents = my_ga.select_parents(population,int(CGA.POPUPATION * CGA.PARENT_PERCENT))
        offspring = my_ga.crossover(parents, CGA.POPUPATION - len(parents))
        my_ga.mutation(offspring)
        for i in range(len(offspring)):
            offspring[i].calculate_individual_fitness()
        population[0:int(CGA.POPUPATION * CGA.PARENT_PERCENT)] = parents
        population[CGA.POPUPATION - len(parents):] = offspring

        population.sort(key = lambda c: c.fitness)
        print("save the best individual")
        save_best_ind(population)
        for i in range(len(population)):
            population[i].train_existed_model()

