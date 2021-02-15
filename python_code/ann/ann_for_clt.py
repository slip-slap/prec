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
x_data = np.float32(np.random.rand(100, 2))
y_data = np.dot(x_data,[[0.1],[0.2]]) + 0.300


x = tf.placeholder("float", [None,16],name="input_x")
y_ = tf.placeholder("float", [None,2],name="input_y")

y=layer("first",x,9)
y=layer("second",y,3)
y=layer("last",y,2)

# loss
loss = tf.reduce_mean(tf.square(y - y_))
summary_loss = tf.summary.scalar(name="loss",tensor=loss)
optimizer = tf.train.GradientDescentOptimizer(0.002)
train = optimizer.minimize(loss)

# init

init = tf.initialize_all_variables()
merged = tf.summary.merge_all()

saver = tf.train.Saver()

my_data = data.data(
        batch=CONFIGURATION["BATCH"],total_data_number=CONFIGURATION['TOTAL_DATA_NUMBER'],
        training_percent=CONFIGURATION["TRAINING_PERCENT"],
        file_path=CONFIGURATION["FILE_PATH"],file_name=CONFIGURATION["FILE_NAME"])

# run graph
with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter("./ann",sess.graph)
    for step in range(0, 40000):
        if(step%2000 == 0):
            saver.save(sess, "./train_model/model.ckpt")
        train_data = my_data.get_batch_train_data()
        train_data_input = train_data[:,0:CONFIGURATION['NUMBER_OF_INPUTS']]
        train_data_output = \
        train_data[:,CONFIGURATION['NUMBER_OF_INPUTS']:CONFIGURATION['NUMBER_OF_INPUTS']
                + \
                CONFIGURATION['NUMBER_OF_OUTPUTS']].reshape(train_data_input.shape[0],CONFIGURATION['NUMBER_OF_OUTPUTS'])
        sess.run(train,feed_dict={x:x_data, y_:y_data})
        summary = sess.run(merged,feed_dict={x:x_data,y_:y_data})
        writer.add_summary(summary, step)
        if step % 1000 == 0:
            print(step,sess.run(loss,feed_dict={x:x_data,y_:y_data}))

