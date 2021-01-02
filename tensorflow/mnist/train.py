import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#testlabel = mnist.test.labels
#print(testlabel)

import tensorflow as tf
import net




x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", [None,10])


x_image = tf.reshape(x, [-1, 28, 28, 1])

h_fc1 = net.net(x_image,10)

y_conv = tf.nn.softmax(h_fc1)


cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))

tf.summary.scalar('loss',cross_entropy)

train_step = tf.train.GradientDescentOptimizer(1e-4).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

tf.summary.scalar('accuracy',accuracy)
merge_summary = tf.summary.merge_all()
sess = tf.Session()
train_writer=tf.summary.FileWriter('/Users/kismet/Desktop',sess.graph)



saver = tf.train.Saver()
sess.run(tf.global_variables_initializer())


for i in range(20000):
    batch = mnist.train.next_batch(50)
    sess.run(train_step, feed_dict={x: batch[0], y_: batch[1] })
    loss=sess.run(cross_entropy, feed_dict={x: batch[0], y_: batch[1]})
    if i%100 == 0:
        train_summary=sess.run(merge_summary, feed_dict={x: batch[0], y_: batch[1] })
        train_writer.add_summary(train_summary,i)
        saver.save(sess,"/Users/kismet/Desktop/tensorflow/mnist/log/model.ckpt")
        train_accuracy = accuracy.eval(session=sess,
                feed_dict={x:batch[0], y_: batch[1]}
                )
        print("step %d,training accuracy %g"%(i, train_accuracy))


print("test accuracy %g"% accuracy.eval(session=sess, feed_dict={x: mnist.test.images, y_: mnist.test.labels0}))
