import network_with_chromosome as train


class Individual(object):

    """Docstring for Individual. """
    def __init__(self):
        self.fitness = None 
        self.connection_gene = None
        self.activation_function_gene = None
        self.model_save_path = None
        self.model_traing_process_path = None

    def __str__(self):
        fitness = str(self.fitness)
        chromosome = str(self.connection_gene)
        model_save_path = str(self.model_save_path )
        return "fitness is: " + fitness + "\n; chromosome is: " + chromosome + "\n; model_save_path: " + model_save_path


    def calculate_individual_fitness(self):
        """TODO: Docstring for calculate_individual_fitness.
        self.fitness = int(np.random.randint(0,15,1))
        """
        self.fitness = train.train_network(self.connection_gene,
                                                self.activation_function_gene, self)
        #self.fitness = valuate.get_cell_result(test_data_input, \
        #               test_data_output, \
        #               meta_graph=str(self.model_save_path)+"/model.meta",\
        #               checkpoint=self.model_save_path)





