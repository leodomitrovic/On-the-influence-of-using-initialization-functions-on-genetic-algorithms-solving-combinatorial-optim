import random
from cities import cities

class Solution:
    
    def __init__(self, tsp_index, nodes=[]):
        self.tsp_index = tsp_index
        self.nodes = nodes[:]
        self.fitness = 0
        #print("This is Constructor")

    def add(self, node_index):
        if node_index in self.nodes:
            print("index {0} already in".format(node_index))
        else:
            self.nodes.append(node_index)
        
    def get(self, array_index):
        return self.nodes[array_index]
    
    def __contains__(self, key):
        return key in self.nodes
    
    def __len__(self):
        return len(self.nodes)
    
    def __str__(self):
        return "Tsp-index: {0}\nNodes: {1}".format(self.tsp_index,self.nodes)
