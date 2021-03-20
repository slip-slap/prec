import constant_variable as cv
import numpy as np
import tool

def get_random_value(code):
    if(code==cv.ANGLE_CODE):
        random_angle_pos = int(np.random.randint(low=0,high=len(cv.ANGLE),size=1))
        return cv.ANGLE[random_angle_pos]
    if(code==cv.MATERIAL_CODE):
        random_material_pos = int(np.random.randint(low=0,high=len(cv.MATERIAL),size=1))
        return cv.MATERIAL[random_material_pos]

def add_block(half_chromosome, half_number,code):
    for i in range(half_number):
        half_chromosome.append(get_random_value(code));
    return half_chromosome
def remove_block(half_chromosome, half_number):
    for i in range(half_number):
        del half_chromosome[-1];
    return half_chromosome

def append_chromsome_is_even(chromosome, number,code):
    full_chromosome = [];
    chromosome_len = len(chromosome)
    half_chromosome = chromosome[0:int(chromosome_len/2)]
    if(number%2==0):
        half_chromosome = add_block(half_chromosome, int(number/2),code);
        full_chromosome = tool.get_symmetry_list(half_chromosome);
    if(number%2==1):
        half_chromosome = add_block(half_chromosome, int(number/2),code);
        full_chromosome = tool.get_symmetry_list(half_chromosome);
        full_chromosome_len = len(full_chromosome)
        full_chromosome.insert(int(full_chromosome_len/2),get_random_value(code))
    return full_chromosome;

def append_(chromosome, number,code):
    full_chromosome = [];
    chromosome_len = len(chromosome)
    if(chromosome_len%2==0):
        full_chromosome = append_chromsome_is_even(chromosome,number,code);
    if(chromosome_len%2==1):
        del chromosome[int(chromosome_len/2)]
        full_chromosome = append_chromsome_is_even(chromosome,number,code);
        mid_pos = int(len(full_chromosome)/2)
    return full_chromosome

def remove_chromsome_is_even(chromosome, number):
    full_chromosome = [];
    chromosome_len = len(chromosome)
    half_chromosome = chromosome[0:int(chromosome_len/2)]
    if(number%2==0):
        half_chromosome = remove_block(half_chromosome, int(number/2),code);
        full_chromosome = tool.get_symmetry_list(half_chromosome);
    if(number%2==1):
        half_chromosome = remove_block(half_chromosome, int(number/2),code);
        full_chromosome = tool.get_symmetry_list(half_chromosome);
        del full_chromosome[int(len(full_chromosome)/2)]
    return full_chromosome;

def remove_(chromosome, number):
    chromosome_len = len(chromosome)
    full_chromosome = [];
    if(chromosome_len%2==0):
        full_chromosome = remove_chromsome_is_even(chromosome, number);
    if(chromosome_len%2==1):
        mid_element = chromosome[int(chromosome_len/2)];
        del chromosome[int(chromosome_len/2)];
        full_chromosome = remove_chromsome_is_even(chromosome, number);
    return full_chromosome;


def get_chromosome_mutation_(chromosome, constraint, code):
    chromosome_after_muation = [];
    if(cv.SAFETY_FACTOR > constraint):
        number = int(cv.MUTATION_EFFICIENT * (cv.SAFETY_FACTOR - constraint))
        chromosome_after_muation = append_(chromosome, number,code);
    if(cv.SAFETY_FACTOR < constraint):
        number = int(cv.MUTATION_EFFICIENT * (constraint - cv.SAFETY_FACTOR))
        chromosome_after_muation = remove_(chromosome, number);
    return chromosome_after_muation;

if __name__ == "__main__":
    chromosome = [2,1,8,9,9,8,1,2]
    print("safety factor: "+ str(cv.SAFETY_FACTOR))
    print("mutation efficient: "+str(cv.MUTATION_EFFICIENT))
    print(get_chromosome_mutation_(chromosome, 0.3,"100"))
