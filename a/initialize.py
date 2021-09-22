from nn import NearestNeighbour
from insertion import Insertion
from i1 import I1
from hfunctions import HelpfulFunctions
from cities import cities
import numpy as np
from tabulate import tabulate
import time
from os import path
import ray

# TODO: friedman's test, kod uspoređivanja različitih genetskih algoritama usporediti city po city, znači usporediti  prosjek od rješenje[heur=0,rand,city] sa rješenje[heur=1,rand,city]

cities = cities.cities
city_names = cities.city_names
heuristic_names = ["Nearest Neighbour", "Insertion", "Solomon I1"]

population_size = 48
nr_of_experiments = 10 # potrebno za pravi experiment staviti na 50, zbog bržeg izračuna sada je 2

heuristics = [NearestNeighbour, Insertion, I1]
randomnesses = [1, 0.5, 0.1, 0]

#if path.exists('data.npy'):
#    results = np.load('data.npy')
#else:
results = np.empty((len(heuristics), len(randomnesses), len(cities), nr_of_experiments), dtype=np.float64)

#if path.exists('times.npy'):
#    times_of_execution = np.load('times.npy')
#else:
times_of_execution = np.empty((len(heuristics), len(randomnesses), len(cities), nr_of_experiments))

average_fitness_arr = np.empty((len(heuristics), len(randomnesses), len(cities)), dtype=np.float64)
stdev_arr = np.empty((len(heuristics), len(randomnesses), len(cities)), dtype=np.float64)
average_times = np.empty((len(heuristics), len(randomnesses), len(cities)), dtype=np.float64)

ray.init(num_cpus=2)

for h, heur in enumerate(heuristics):
    print("Heuristic: " + heuristic_names[h])
    for r, randomness in enumerate(randomnesses):
        print("Randomness: " + str(randomness*100) + "%")
        for g, city in enumerate(cities):
            print("City: " + city_names[g] + " (" + str(g) + ")")
            for i in range(nr_of_experiments):
                print("Experiment: " + str(i))
                if abs(results[h,r,g,i]) < 0.001:
                    #print("experiment: " + str(i))
                    time_at_start = time.time()
                    population, population_fitness = HelpfulFunctions.makePopulation(heur, population_size, city, randomness)
                    best_solution = HelpfulFunctions.algorithm(population, population_fitness, population_size, len(city))
                    times_of_execution[h,r,g,i] = time.time() - time_at_start
                    results[h,r,g,i] = int(HelpfulFunctions.evaluate(best_solution))
                    np.save('data', results)
                    np.save('times', times_of_execution)
            break
        break
    break

ray.shutdown()

def showResults():
    for h, heur in enumerate(heuristics):
        print("Heuristic: " + heuristic_names[h])
        for r, randomness in enumerate(randomnesses):
            for g, city in enumerate(cities):
                average_fitness = 0
                average_time = 0
                for i in range(nr_of_experiments):
                    average_fitness += results[h,r,g,i]
                    average_time += times_of_execution[h,r,g,i]
                    
                average_fitness /= nr_of_experiments
                average_fitness_arr[h,r,g] = average_fitness
                
                average_time /= nr_of_experiments
                average_times[h,r,g] = average_time
                
                stdev_arr[h,r,g] = np.std(results[h,r,g])
            info = {'city': city_names, 'Avg.': average_fitness_arr[h,r], 'St. dev.': stdev_arr[h,r], 'Avg. time': average_times[h,r]}
            print("Randomness: " + str(randomness*100) + "%")
            print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

showResults()