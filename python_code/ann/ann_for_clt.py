import tensorflow as tf
import numpy as np
import yaml
import data

CONFIGURATION = None;
with open('configuration.yaml') as input_stream:
    CONFIGURATION = yaml.load(input_stream, Loader=yaml.FullLoader)

def layer(layer_name, data, output_channels):
    with tf.variable_scope(layer_name,reuse=tf.AUTO_REUSE):
        w = tf.get_variable(name="weight",shape=[data.shape[-1],output_channels])
        b = tf.get_variable(name="bias",shape=[output_channels])
        summary_bias = tf.summary.histogram("bias",b)
        y = tf.matmul(data,w)
        y = tf.add(y,b,name="bias")
        if layer_name == "last":
            y = tf.nn.relu(y,name="relu_function")
        else:
            y = tf.sigmoid(y,name="sigmoid_function")
    return y


# use NumPy to produce data
#x_data = np.float32(np.random.rand(100, 2))
#y_data = np.dot(x_data,[[0.1],[0.2]]) + 0.300


x = tf.placeholder("float", [None,CONFIGURATION['NUMBER_OF_INPUTS']],name="input_x")
y_ = tf.placeholder("float", [None,CONFIGURATION['NUMBER_OF_OUTPUTS']],name="input_y")

y=layer("first",x,9)
y=layer("second",y,3)
y=layer("last",y,CONFIGURATION['NUMBER_OF_OUTPUTS'])

# loss
loss = tf.reduce_mean(tf.square(y - y_))
summary_loss = tf.summary.scalar(name="loss",tensor=loss)
optimizer = tf.train.GradientDescentOptimizer(CONFIGURATION["LEARNING_RATE"])
train = optimizer.minimize(loss)

# init

#init = tf.initialize_all_variables()
init = tf.global_variables_initializer()
merged = tf.summary.merge_all()

saver = tf.train.Saver()

my_data = data.data(
        batch=CONFIGURATION["BATCH"],total_data_number=CONFIGURATION['TOTAL_DATA_NUMBER'],
        training_percent=CONFIGURATION["TRAINING_PERCENT"],
        file_path=CONFIGURATION["FILE_PATH"],file_name=CONFIGURATION["FILE_NAME"])

# run graph
with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter(CONFIGURATION["SAVING_PLACE_OF_TRAINING_PROCESS"],sess.graph)
    for step in range(0, CONFIGURATION['TRAINING_RUNTIMES']):
        train_data = my_data.get_batch_train_data()
        x_data = train_data[:,0:CONFIGURATION['NUMBER_OF_INPUTS']]
        y_data = \
        train_data[:,CONFIGURATION['NUMBER_OF_INPUTS']:CONFIGURATION['NUMBER_OF_INPUTS']
                + \
                CONFIGURATION['NUMBER_OF_OUTPUTS']].reshape(x_data.shape[0],CONFIGURATION['NUMBER_OF_OUTPUTS'])
        summary = sess.run(merged,feed_dict={x:x_data,y_:y_data})
        if step % 4000 == 0:
            writer.add_summary(summary, step)
            saver.save(sess, CONFIGURATION["SAVING_PLACE_OF_TRAINING_MODEL"])
            print(step,sess.run(loss,feed_dict={x:x_data,y_:y_data}))
        sess.run(train,feed_dict={x:x_data, y_:y_data})

