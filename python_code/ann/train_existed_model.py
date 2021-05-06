import tensorflow as tf
import tool
import data
import yaml

CONFIGURATION = None;
with open('configuration.yaml') as input_stream:
    CONFIGURATION = yaml.load(input_stream, Loader=yaml.FullLoader)
my_data = data.data(
            batch=CONFIGURATION["BATCH"],total_data_number=CONFIGURATION['TOTAL_DATA_NUMBER'],
            training_percent=CONFIGURATION["TRAINING_PERCENT"],
            file_path=CONFIGURATION["FILE_PATH"],file_name=CONFIGURATION["FILE_NAME"])

def coninue_training(graph_dir):
    print("train an existed neural network")
    return_value_loss = 0
    g1 = tf.Graph()
    with g1.as_default() as g:
        saver = tf.train.import_meta_graph(graph_dir+"/model.meta")
        input_x = g.get_tensor_by_name("input_x:0")
        input_y = g.get_tensor_by_name("input_y:0")
        loss  = g.get_tensor_by_name("loss:0")
        train = g.get_operation_by_name("train")
        output  = g.get_tensor_by_name("last_layer/result:0")

        with tf.Session() as sess:
            saver.restore(sess, tf.train.latest_checkpoint(graph_dir+"/"))
            for step in range(CONFIGURATION['TRAINING_RUNTIMES']):
                # get data
                train_data = my_data.get_batch_train_data()
                train_data_input = train_data[:,0:CONFIGURATION['NUMBER_OF_INPUTS']]
                train_data_output = \
                train_data[:,CONFIGURATION['NUMBER_OF_INPUTS']:CONFIGURATION['NUMBER_OF_INPUTS']
                        + \
                        CONFIGURATION['NUMBER_OF_OUTPUTS']].reshape(train_data_input.shape[0],CONFIGURATION['NUMBER_OF_OUTPUTS'])
                sess.run(train,feed_dict={input_x:train_data_input, input_y:train_data_output})
                if step % CONFIGURATION['NUMBER_OF_TRAINING_SAVE_STATE'] == 0:
                    saver.save(sess, graph_dir + "/model")
                    # can't name this variable loss, it will overwrite the tensor in the 
                    # graph
                    return_value_loss = sess.run(loss,feed_dict={input_x:train_data_input,input_y:train_data_output})
                    print("step="+str(step)+" "+str(return_value_loss))
    return return_value_loss

if __name__=="__main__":
    print(coninue_training("./train_model/model1"))
