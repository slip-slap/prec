import numpy as np
import yaml

CONFIGURATION = None;
with open('configuration.yaml') as input_stream:
    CONFIGURATION = yaml.load(input_stream, Loader=yaml.FullLoader)

def get_activation_function_gene(number=5):
    gene = list()
    for i in range(5):
        a = int(np.random.randint(0,2,1))
        b = int(np.random.randint(0,2,1))
        gene.append([a,b])
    return gene

def get_connection_gene(number=5):
    chromosome = list()
    for i in range(5):
        gene_unit = np.random.randint(0,2,(CONFIGURATION['NUMBER_OF_INPUTS']))
        chromosome.append(gene_unit)
    return chromosome


if __name__=='__main__':
    a = get_activation_function_gene()
    b = get_connection_gene()
    with open("network_train_result.txt","a") as train_handler:
            train_handler.write("ANN model:")
            train_handler.write("\n")
            train_handler.write("active function: " + str(a))
            train_handler.write("\n")
            train_handler.write("connection:  " + str(b))
