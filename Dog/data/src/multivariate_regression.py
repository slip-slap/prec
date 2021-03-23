import numpy as np

NUMBER_OF_VARIATES = 4
NUMBER_OF_DATA     = 100


#  y = 3x1 + -2x2 + x3
input_data = [
        [0,1],
        [1,0],
        [4,0],
        [6,5],
        [9,3],
        [5,2],
        [13,7]
        ]
output_data = [-2, 3, 12,  8, 21, 11, 25]


def mutivars_regress_model(inputs, outputs):
    inputs_transpose = np.transpose(inputs)
    normal_matrix = np.matmul(inputs_transpose, np.array(inputs))
    moment_matrix = np.matmul(inputs_transpose, outputs)
    beta = np.matmul(np.linalg.inv(normal_matrix), moment_matrix)
    return beta 

outputs = np.array(output_data).transpose()
result = mutivars_regress_model(input_data, outputs)

print(result)



