import numpy as np
import tensorflow as tf
import data
import tool
import yaml

CONFIGURATION = None;
with open('configuration.yaml') as input_stream:
    CONFIGURATION = yaml.load(input_stream, Loader=yaml.FullLoader)

my_data = data.data(
        batch=CONFIGURATION["BATCH"],total_data_number=CONFIGURATION['TOTAL_DATA_NUMBER'],
        training_percent=CONFIGURATION["TRAINING_PERCENT"],
        file_path=CONFIGURATION["FILE_PATH"],file_name=CONFIGURATION["FILE_NAME"])

test_data= my_data.get_test_data()
test_data_input = test_data[:,0:16]
test_data_output = test_data[:,16:CONFIGURATION['NUMBER_OF_INPUTS']+ CONFIGURATION['NUMBER_OF_OUTPUTS']
                             ].reshape(test_data_input.shape[0],CONFIGURATION['NUMBER_OF_OUTPUTS'])

def get_cell_result(train_data_input, train_data_output, \
        meta_graph="", checkpoint=""):
    g1 = tf.Graph()
    with g1.as_default() as g:
        saver = tf.train.import_meta_graph(meta_graph)
        input_x = g.get_tensor_by_name("input_x:0")
        input_y = g.get_tensor_by_name("input_y:0")
        output  = g.get_tensor_by_name("last/relu_function:0")
        with tf.Session() as sess:
            saver.restore(sess, tf.train.latest_checkpoint(checkpoint))

            my_output = sess.run(output, \
                    feed_dict={input_x:train_data_input,input_y:train_data_output})

            print(" simulation result\n"+  str(my_output))
            print(" practical result\n"+   str(train_data_output))
    return my_output; 

if __name__=='__main__':
    print(test_data_input.shape)
    test_data_input = test_data_input[20:26,:]
    test_data_output = test_data_output[20:26,:]
    accurate = get_cell_result(test_data_input, test_data_output, \
            meta_graph="./train_model/model.meta",\
            checkpoint='./train_model')
"""
    feature_result2 = get_cell_result(test_data_input, test_data_output, \
            meta_graph="./trained_model/feature2_cell/model.meta",\
            checkpoint='./trained_model/feature2_cell')
    feature_result3 = get_cell_result(test_data_input, test_data_output, \
            meta_graph="./trained_model/feature3_cell/model.meta",\
            checkpoint='./trained_model/feature3_cell')
    feature_result4 = get_cell_result(test_data_input, test_data_output, \
            meta_graph="./trained_model/feature4_cell/model.meta",\
            checkpoint='./trained_model/feature4_cell')



# combniationg model
    test_data_input = np.concatenate((feature_result2, \
        feature_result1,feature_result3,feature_result4), 1)
    normal_result = get_cell_result(test_data_input, test_data_output, \
            meta_graph="./trained_model/combination/model.meta",\
            checkpoint='./trained_model/combination')
"""

