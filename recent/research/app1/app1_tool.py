import numpy as np
import ga_constant_variable as GCV
import collections

def counter_item(a):
    if(isinstance(a,list)==False):
        print("input argument is not a list")
        return
    if(len(a)==0):
        print("element length is zero")
        return
    return  dict(collections.Counter(a))

def list_cross_over(a, b, random_number):
    if isinstance(a, list) != True:
        print("the first element is not a list")
    if isinstance(b, list) != True:
        print("the second element is not a list")
    if len(a) == 0:
        print("the first element is empty")
    if len(b) == 0:
        print("the second element is empty")
    
    a_half_pos = int(len(a)/2)
    b_half_pos = int(len(b)/2)
    
    if(random_number == 0):
        result = a[0:a_half_pos] + b[0:b_half_pos]
    if(random_number == 1):
        result = a[0:a_half_pos] + b[b_half_pos:]
    if(random_number == 2):
        result = a[a_half_pos:] + b[0:b_half_pos]
    if(random_number == 3):
        result = a[a_half_pos:] + b[b_half_pos:]
    return result

def reduce_list_length(a, number):
    #print('a: ' + str(a))
    #print('number: ' + str(number))
    if isinstance(a,list) == False:
        print("reduce list length")
        print("the first argument is not a list")
        return
    if number == 0:
        return a
    if number < 1:
        print("reduce list length")
        print("illegal argument")
        return
    if len(a) < number:
        print("reduce list length")
        print("list is too short")
        return
    for i in range(number):
        del a[-1]
    return a

def increase_list_length(a, number):
    if isinstance(a, list)==False:
        print("increase list length")
        print("the first argument is not a list")
        return
    if number < 0:
        print("increase list length")
        print("the second argument is not a list")
        return
    for i in range(number):
        random_angle_pos = int(np.random.randint(low=0,high=len(GCV.ANGLE),size=1))
        a.append(GCV.ANGLE[random_angle_pos])
    return a

def random_change_list_content(a):
    if isinstance(a, list)==False:
        print("the first argument is not a list")
        return
    for i in range(len(a)):
        if(np.random.random() > 0.4):
            a[i] = GCV.ANGLE[0] - a[i]
    return a

def modify_one_element_list(a):
    random_pos = np.random.randint(0, len(a)) 
    a[random_pos] = GCV.ANGLE[0] - a[random_pos]
    return a

def get_specified_value_pos(a, value, population):
    a_ = np.subtract(a, value).tolist()
    if max(a_) < 0:
        return a_.index(max(a_))
    if max(a_) >= 0:
        #sub_a_= [x for x in a_ if x > 0]
        #min_ele = min(sub_a_)
        sub_a = [x for x in population if x.strength_raito > value]
        min_mass = 1000
        identity = 0
        for i in range(len(sub_a)):
            if(sub_a[i].mass < min_mass):
                min_mass = sub_a[i].mass
                identity = id(sub_a[i])
        for i in range(len(population)):
            if id(population[i]) == identity:
                return i


def save_individual(ind):
    with open("temp.py","a") as result_handler:
        result_handler.write("##########begin########################")
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_layup= "+ str(counter_item(ind.angle_list)))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_strength_raito= "+ str(ind.strength_raito))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_mass= "+ str(ind.mass))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_cost= "+ str(ind.cost))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_number_of_layer= "+ str(len(ind.material_list)))
        result_handler.write("\n")
        result_handler.write("##########end########################")
        result_handler.write("\n")

def save_average_result(result_fitness, result_strength_ratio,total_sr,total_mass, total_cost, total_layer, RUN_BATCH):
    with open("result_ind.py","a") as result_handler:
        result_handler.write("##########average########################") 
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_fitness= "+ str(np.divide(result_fitness,1).tolist()))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_fitness= "+ str(np.divide(result_fitness,RUN_BATCH).tolist()))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_strength_ratio= "+ str(np.divide(result_strength_ratio,RUN_BATCH).tolist()))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_average_strength_ratio= "+ str(np.divide(total_sr,RUN_BATCH)))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_average_mass= "+ str(np.divide(total_mass,RUN_BATCH)))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_average_cost= "+ str(np.divide(total_cost,RUN_BATCH)))
        result_handler.write("\n")
        result_handler.write("coeff_"+ str(GCV.MUTATION_EFFICIENT_TYPE) +"_average_layer= "+ str(np.divide(total_layer,RUN_BATCH)))
        result_handler.write("\n")

if __name__ == '__main__':
    #a = list_cross_over([1,2,3,2,5],[89,120,340],3)
    #a = reduce_list_length([1,2,3,4,2],0)
    #a = increase_list_length([1,2],3)
    #print(a)
    #print(get_specified_value_pos([0.999,1.2323,2], 2.15))
    with open("temp.py","a") as result_handler:
        result_handler.write("##########average########################")
        result_handler.write(str([1,2,4]))


