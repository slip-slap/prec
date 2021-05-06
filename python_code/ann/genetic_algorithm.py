import numpy as np
import copy
import yaml
import individual
import tool_ga



class Genetic_Algorithm(object):

    """Docstring for Genetic_Algorithm. """

    def __init__(self):
        """TODO: to be defined. """
        self.child_counter = 0
        self.CONFIGURATION = None
        with open('configuration.yaml') as input_stream:
            self.CONFIGURATION = yaml.load(input_stream, Loader=yaml.FullLoader)
        pass

    def select_parents(self, population,  num_parents):
        parents = population[0:num_parents]
        return parents

    def crossover(self, parents, offspring_number):
        """TODO: Docstring for crossover.
        :returns: offspring
        """
        offspring = []
        print("crossover operation")
        for i in range(offspring_number):
            parent1_pos = int(np.random.randint(0, len(parents), 1))
            parent2_pos = int(np.random.randint(0, len(parents), 1))
            parent1_node_number = len(parents[parent1_pos].connection_gene)
            parent2_node_number = len(parents[parent2_pos].connection_gene)

            child_node_number = int(parent1_node_number/2 + parent2_node_number/2)
            child = copy.deepcopy(parents[0])
            child.connection_gene = tool_ga.get_connection_gene(child_node_number)
            child.activation_function_gene = tool_ga.get_activation_function_gene(child_node_number)
            child.node_number = child_node_number
            child.fitness = -1
            child.model_save_path = self.CONFIGURATION['SAVING_PLACE_OF_TRAINING_MODEL'] + "/child" + str(self.child_counter)+ "/model"
            child.model_traing_process_path = self.CONFIGURATION['SAVING_PLACE_OF_TRAINING_PROCESS']+ "/child"+  str(self.child_counter) + "/model"
            offspring.append(child)
            self.child_counter = self.child_counter + 1
        return offspring
            

    def mutation(self, offspring):
        """TODO: Docstring for mutation.
        :returns: None
        """
        pass
        

                 






