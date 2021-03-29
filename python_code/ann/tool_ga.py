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
    print(get_activation_function_gene())
    print(get_connection_gene())
