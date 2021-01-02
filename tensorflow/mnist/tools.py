import tensorflow as tf

def conv(layer_name, x, out_channels,kernel_size=[3,3], stride=[1,1,1,1]):
    in_channels = x.get_shape()[-1]
    with tf.variable_scope(layer_name):
        w = tf.get_variable(name='weights',
                            shape=[kernel_size[0],kernel_size[1],in_channels, out_channels],
                            initializer=tf.contrib.layers.xavier_initializer())
        b = tf.get_variable(name="biases",
                            shape=[out_channels],
                            initializer=tf.constant_initializer(0.0))
        x = tf.nn.conv2d(x, w, stride, padding='SAME', name='conv')
        x = tf.nn.bias_add(x, b, name='bias_add')
        x = tf.nn.relu(x,name='relu')
        return x

def pool(layer_name, x, kernel=[1,2,2,1], stride=[1,2,2,1], is_max_pool=True):
    if is_max_pool:
        x=tf.nn.max_pool(x, kernel, strides=stride, padding='SAME', name=layer_name)
    else:
        x =tf.nn.avg_pool(x. kernel, strides=stride, padding='SAME', name=layer_name)
    return x

def fc_layer(layer_name, x, out_nodes):
    shape=x.get_shape()
    if len(shape) == 4:
        size = shape[1].value*shape[2].value*shape[3].value
    else:
        size = shape[-1].value

    with tf.variable_scope(layer_name):
        w = tf.get_variable('weights',
                            shape=[size, out_nodes],
                            initializer=tf.contrib.layers.xavier_initializer(0.0))
        b = tf.get_variable('biases',
                            shape=[out_nodes],
                            initializer=tf.constant_initializer(0.0))
        flat_x =tf.reshape(x, [-1, size])

        x = tf.nn.bias_add(tf.matmul(flat_x, w), b)
        x = tf.nn.relu(x)
        return x


