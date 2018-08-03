import tensorflow as tf

def xavier_init(size):
    '''

    :param size:
    :return:
    '''
    in_dim = size[0]
    xavier_stddev = 1. / tf.sqrt(in_dim / 2.)
    return tf.random_normal(shape=size, stddev=xavier_stddev)


class layers:
    
    def fullyConnectedLayer(self, x, input_size, output_size, activation_func, name='fullyConnectedLayer'):
        with tf.variable_scope(name):
            w = tf.Variable(xavier_init([input_size,output_size]))
            b = tf.Variable(tf.zeros(output_size))
            layer = tf.nn.relu(tf.matmul(x, w) + b)
            return layer
    
