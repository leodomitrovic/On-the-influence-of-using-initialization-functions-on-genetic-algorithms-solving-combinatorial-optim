# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:43:54 2021

@author: Krepana Krava
"""

import numpy as np
import urllib
import matplotlib.pyplot as plt
import random



urls = ["http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/berlin52.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/st70.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/eil76.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/kroA100.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/kroB100.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/kroC100.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/eil101.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr107.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr124.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr136.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr144.tsp",
"http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr152.tsp"]

for url in urls:
    file1 = urllib.request.urlopen(url)
    #file = []
    cities = []
    i = 0
    for line in file1: 
        i += 1
        l = line.decode("utf-8")
        #print(l)
        if(l != "EOF\n"):
            #file.append(l)
            if i >= 7:
                l = l.split()
                
                tmp = []
                for k in l:
                    tmp.append(int(k))
                cities.append(tmp)
    print(cities)