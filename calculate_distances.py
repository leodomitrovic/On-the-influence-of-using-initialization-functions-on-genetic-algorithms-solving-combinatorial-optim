# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:32:45 2021

@author: Krepana Krava
"""

from hfunctions import HelpfulFunctions
from cities import cities
import numpy as np

cities = cities.cities

nr_of_cities = len(cities)

cities_with_distances = []
itera = 0
for i, city in enumerate(cities):
    nr_of_individual_distances = len(city)
    individual_distances = np.zeros(( nr_of_individual_distances, nr_of_individual_distances ), dtype=float)

    for j in range(nr_of_individual_distances):
        for k in range(j+1, nr_of_individual_distances):
            
            individual_distances[j, k] = float(HelpfulFunctions.distance(cities[i][j][1], cities[i][j][2], cities[i][k][1], cities[i][k][2]))
            
    cities_with_distances.append(individual_distances)

np.save('distances', cities_with_distances)