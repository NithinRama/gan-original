from collections import OrderedDict
import configparser
import pdb
from layers import *

class multidict(OrderedDict):
    _unique = 0   # class variable

    def __setitem__(self, key, val):
        if isinstance(val, dict):
            self._unique += 1
            key += str(self._unique)
        OrderedDict.__setitem__(self, key, val)
#TODO :add leakyrelu
nets = ['fullyConnectedlayer', 'ConvulationLayer', 'DeConvulationLayer']
activ = ['sigmoid', 'tanh', 'elu', 'selu', 'softplus', 'softsign', 'relu', 'tanh']
layers_list = []
Config = configparser.ConfigParser(defaults=None, dict_type=multidict, strict=False)
Config.read('network.cfg')
a = Config._sections
print(a)
for i in a:
    net_name = i
    net_name = ''.join(i for i in net_name if not i.isdigit())
    if net_name in nets:
        layers_list.append(net_name)
        idx = nets.index(net_name)
        if idx == 0:
            
            
            
            
            

        #self.g_fc1_W = tf.Variable(xavier_init([100, 128]))
        #self.g_fc1_b = tf.Variable(tf.zeros(128))