import numpy as np
import ga_constant_variable as GCV

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
        result = a[0:a_half_pos] + b[b_half_pos:-1]
    if(random_number == 2):
        result = a[a_half_pos:-1] + b[0:b_half_pos]
    if(random_number == 3):
        result = a[a_half_pos:-1] + b[b_half_pos:-1]
    return result

def reduce_list_length(a, number):
    if isinstance(a,list) == False:
        print("the first argument is not a list")
        return
    if number < 1:
        print("illegal argument")
        return
    if len(a) < number:
        print("list is too short")
        return

    for i in range(number):
        del a[-1]
    return a

def increase_list_length(a, number):
    if isinstance(a, list)==False:
        print("the first argument is not a list")
        return
    if number < 0:
        print("the second argument is not a list")
        return
    for i in range(number):
        random_angle_pos = int(np.random.randint(low=0,high=len(GCV.ANGLE),size=1))
        a.append(GCV.ANGLE[random_angle_pos])
    return a


if __name__ == '__main__':
    #a = list_cross_over([1,2,3,2,5],[89,120,340],3)
    #a = reduce_list_length([1,2,3,4,2],-1)
    a = increase_list_length([1,2],3)
    print(a)



