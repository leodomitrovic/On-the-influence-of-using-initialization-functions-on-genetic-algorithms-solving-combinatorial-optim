# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:03:48 2021

@author: Krepana Krava
"""

import numpy as np

from hfunctions import HelpfulFunctions
from cities import cities

from tabulate import tabulate
import pandas as pd


results = np.load('data.npy')
times = np.load('times.npy')

heuristics = 3

done_counter = 0



city_names = cities.city_names
heuristic_names = ["NN", "In", "I1"]
population_size = 48
nr_of_experiments = 5 # potrebno za pravi experiment staviti na 50, zbog bržeg izračuna sada je 2

randomnesses = [1, 0.5, 0.1, 0]


cities = []
average_fitness_arr = []
fitstdev_arr = []
timestdev_arr = []
average_times = []
heurs = []

extra_array = np.zeros((len(city_names), 4*4), dtype=float)

#for i in range(10):
#    print(results[0,0,11,i])

#print(np.std(results[0,0,11, 0:10]))
#print(np.std([74629.0,74079.0,74235.0,74309.0,75141.0,74455.0,73843.0,74376.0,74729.0,74113.0]))

for h in range(heuristics):
    for r in range(len(randomnesses)):
        
        for g in range(15):
            not_empty = False
            average_fitness = 0
            average_time = 0
            for i in range(nr_of_experiments):
                if abs(results[h,r,g,i]) > 0.1:
                    not_empty = True
                    done_counter += 1
                average_fitness += results[h,r,g,i]
                #average_time += times[h,r,g,i]
                
            average_fitness /= nr_of_experiments
            #average_fitness_arr[h,r,g] = average_fitness
            
            average_time /= nr_of_experiments
           # average_times[h,r,g] = average_time
            if not_empty:
               print("{0},{1},{2}".format(h,r,g))
print(done_counter)

def showResults():
    h = 2
    #print("heuristic: " + heuristic_names[h])
    for r, randomness in enumerate(randomnesses):
        not_empty = False
        for g in range(15):
            average_fitness = 0
            average_time = 0
            for i in range(nr_of_experiments):
                if abs(results[h,r,g,i]) > 0.1:
                    not_empty = True
                average_fitness += results[h,r,g,i]
                average_time += times[h,r,g,i]
                
            average_fitness /= nr_of_experiments
            average_fitness_arr.append(average_fitness)
            
            average_time /= nr_of_experiments
            average_times.append(average_time)
            
            fitstdev = np.std(results[h,r,g,0:nr_of_experiments])
            timestdev = np.std(times[h,r,g,0:nr_of_experiments])
            
            fitstdev_arr.append(fitstdev)
            timestdev_arr.append(timestdev)
            heurs.append(h)
            cities.append(g)
            

            
            extra_array[g][(4*r)] = average_fitness
            extra_array[g][(4*r)+1] = fitstdev
            extra_array[g][(4*r)+2] = average_time
            extra_array[g][(4*r)+3] = timestdev
            print(results[h,r,g,0])
                
            #if not_empty:
                #info = {'city': city_names, 'Avg.': average_fitness_arr[h,r], 'St. dev.': fitstdev_arr[h,r], 'Avg. time': average_times[h,r]}
                #print("Randomness: " + str(randomness*100) + "%")
                #print(tabulate(info, headers='keys', tablefmt='fancy_grid'))
            #break # da se ne računa previše, točnije samo jedan randomness
  # također da se ne računa previše, točnije samo jedna heuristic
        
showResults()

data = {
        'City': cities,
        'Average fitness': average_fitness_arr,
        'Fitness st. dev.': fitstdev_arr,
        'Average time': average_times,
        'Time st. dev.': timestdev_arr,
        'Heur': heurs,
        }

#df = pd.DataFrame(data)
#lala = df.groupby(['Heur'])['City'].count()
#print (lala)
#np.savetxt('krava.txt', extra_array, delimiter=',', dtype=int) 

arrays = [
    np.array(["1", "1", "1", "1", "0.5", "0.5", "0.5", "0.5", "0.1", "0.1", "0.1", "0.1", "0", "0", "0", "0"]), #randomness
    np.array(["fitness", "fit.st.dev.", "time", "time st.dev.","fitness", "fit.st.dev.", "time", "time st.dev.","fitness", "fit.st.dev.", "time", "time st.dev.","fitness", "fit.st.dev.", "time", "time st.dev."]), #stupci koje trebamo
]

city_names = ["berlin52", "st70", "eil76", "kroA100", "kroB100", "kroC100", "eil101", "pr107", "pr124", "pr136", "pr144", "pr152", "oliver30","eilon50","eilon75"]


df = pd.DataFrame(extra_array)
#lol = df.transpose
print(df)
df.to_csv('out.csv')