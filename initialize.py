from nn import NearestNeighbour
from insertion import Insertion
from i1 import I1
from hfunctions import HelpfulFunctions
from cities import cities
import numpy as np
from tabulate import tabulate
import time
import ray
import winsound

ray.shutdown()
ray.init()

cities = cities.cities
city_names = cities.city_names
heuristic_names = ["NN", "In", "I1"]
population_size = 48
nr_of_experiments = 5

heuristics = [NearestNeighbour, Insertion, I1]
randomnesses = [1, 0.5, 0.1, 0]

results = np.load('data.npy')
times_of_execution = np.load('times.npy')

if len(results) == 0:
    results = np.zeros((len(heuristics), len(randomnesses), len(cities), 50))
    times_of_execution = np.zeros((len(heuristics), len(randomnesses), len(cities), 50))

average_fitness_arr = np.zeros((len(heuristics), len(randomnesses), len(cities)), dtype=float)
fitnessstdev_arr = np.zeros((len(heuristics), len(randomnesses), len(cities)), dtype=float)
timestdev_arr = np.zeros((len(heuristics), len(randomnesses), len(cities)), dtype=float)
average_times = np.zeros((len(heuristics), len(randomnesses), len(cities)), dtype=float)

def reset_saved_data():
    results = np.zeros((len(heuristics), len(randomnesses), len(cities), 50))
    times_of_execution = np.zeros((len(heuristics), len(randomnesses), len(cities), 50))
    np.save('data', results)
    np.save('times', times_of_execution)

@ray.remote
def itera(h, population_size, city, randomness, indeks_grada, broj_eksperimenta, counter):
    time_at_start = time.time()
    population, population_fitness = HelpfulFunctions.makePopulation(heuristics[h], population_size, city, randomness)
    best_solution = HelpfulFunctions.algorithm(population, population_fitness, population_size, city_names[indeks_grada] + ":" + str(randomness) + ":" + heuristic_names[h])
    time_of_execution = time.time() - time_at_start
    rjesenje = int(HelpfulFunctions.evaluate(best_solution))
    print("Tsp problem: " + heuristic_names[h] + ":" + str(randomness*100) + "%:" + city_names[indeks_grada] + ":" + str(broj_eksperimenta) + " (" + str(counter) + "/50)")
    print("Time: {0:.0f} seconds".format(time_of_execution))
    print("Fitness: " + str(rjesenje))
    return (time_of_execution, rjesenje)

while True:
    
    counter = 0
    max_counter = 50
    
    tasks = []
    task_settings = []

    for h, heur in enumerate(heuristics):
        for r, randomness in enumerate(randomnesses):
            if r == 3 and h != 0:
                continue
            for g, city in enumerate(cities):
                for i in range(nr_of_experiments):
                    if abs(results[h,r,g,i]) < 0.1:
                                                
                        if counter >= max_counter:
                            break
                        
                        tasks.append(itera.remote(h, population_size, city, randomness, g, i, counter))
                        task_settings.append((h,r,g,i))
                        counter += 1
                                                
                        print("Added to execution queue: " + heuristic_names[h] + ":" + str(randomness*100) + "%:" + city_names[g] + ":" + str(i) + " (" + str(counter) + "/50)")

                if counter >= max_counter:
                    break
            if counter >= max_counter:
                break
        if counter >= max_counter:
            break
    
    if counter > 0:
    
        ray_results = ray.get(tasks)
        
        for i, p in enumerate(task_settings):
            
            results[p[0],p[1],p[2],p[3]] = float(ray_results[i][1])
            times_of_execution[p[0],p[1],p[2],p[3]] = float(ray_results[i][0])
        
        print("Saving results...")
        
        np.save('data', results)
        np.save('data_backup', results)
        np.save('times', times_of_execution)
        np.save('times_backup', times_of_execution)
        
        print("Results saved!")
        
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    else:
        break

def showResults():
    for h, heur in enumerate(heuristics):
        print("Heuristic: " + heuristic_names[h])
        for r, randomness in enumerate(randomnesses):
            not_empty = False
            for g, city in enumerate(cities):
                average_fitness = 0
                average_time = 0
                for i in range(nr_of_experiments):
                    if abs(results[h,r,g,i]) > 0.1:
                        not_empty = True
                    average_fitness += results[h,r,g,i]
                    average_time += times_of_execution[h,r,g,i]
                    
                average_fitness /= nr_of_experiments
                average_fitness_arr[h,r,g] = average_fitness
                
                average_time /= nr_of_experiments
                average_times[h,r,g] = average_time
                
                fitnessstdev_arr[h,r,g] = np.std(results[h,r,g,0:nr_of_experiments])
                timestdev_arr[h,r,g] = np.std(times_of_execution[h,r,g,0:nr_of_experiments])
            if not_empty:
                info = {'city': city_names, 'Avg. fitness': average_fitness_arr[h,r], 'St. dev. of fitness': fitnessstdev_arr[h,r], 'Avg. time': average_times[h,r], 'St. dev. of time': timestdev_arr[h,r]}
                print("Randomness: " + str(randomness*100) + "%")
                print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

showResults()
