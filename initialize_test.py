from nn import NearestNeighbour
from insertion import Insertion
from i1 import I1
from hfunctions import HelpfulFunctions
from cities import cities
import numpy as np
from tabulate import tabulate
import time
import ray

HelpfulFunctions.ucitajUdaljenosti()

nn = NearestNeighbour(0)
nn.generate_solution(52)

# i sad bi htio NOVU instancu ali kad napišem nn = NearestNeighbour(0), nn referencira na ovaj stari
nn = NearestNeighbour(0)
print(nn.solution)