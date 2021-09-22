import numpy as np
import matplotlib.pyplot as plt
import random
import time


class HelpfulFunctions:
    
    def makePopulation(heuristic, population_size, cities, randomness):
        
        # initialization      
        population = []
        population_fitness = []
        
        if randomness == 1:
            solution_heur = len(cities)
        elif randomness == 0.5:
            solution_heur = int(len(cities) / 2)
        elif randomness == 0.1:
            solution_heur = int(len(cities) * 0.1)
        else: 
            solution_heur = 0
        
        for i in range(population_size):
            cities_copy = cities[:]
            solution = heuristic.generate_solution(cities_copy, solution_heur)
            population.append(solution)
            population_fitness.append(HelpfulFunctions.evaluate(solution))
        
        return population, population_fitness
    
    def OrderCrossover(first, second):
        first_crossover = random.randint(0, len(first)-1)
        
        while True:
            second_crossover = random.randint(0, len(first)-1)
            if first_crossover != second_crossover:
                break
            
        tmp1 = first_crossover
        tmp2 = second_crossover
        first_crossover = min(tmp1, tmp2)
        second_crossover = max(tmp1, tmp2)
        
        child = first[first_crossover:second_crossover]
        
        for i in range(second_crossover, second_crossover + len(second)):
            index = i % len(second)
            if second[index] not in child:
                child.append(second[index])

        return child
    
    def draw(population, title):
        x = [item[1] for item in population]
        y = [item[2] for item in population]
        plt.plot(x, y)
        plt.plot(x, y, 'ro')
        plt.title(title)
        plt.show()
    
    def algorithm(population, population_fitness, population_size, tsp_name):
        counter = 0
        min_res = []
        min_fitness = 100000
        
        best_fitnesses = []
        
        while True:
            if counter == 100:
                break
            
            ELITIST_SIZE = int(population_size/2)
            elitists = population[:ELITIST_SIZE]
            elitists_fitness = population_fitness[:ELITIST_SIZE]
            
            offspring, offspring_fitness = HelpfulFunctions.generate_offspring(population)
                        
            population += offspring
            population_fitness += offspring_fitness
                
            for i in reversed(range(len(population))):
                if population[i] in elitists:
                    del population[i]
                    del population_fitness[i]
            
            # Sort
            for _ in range(len(population)):
                for j in range(len(population) - 1):
                    if population_fitness[j] > population_fitness[j+1]:
                        population[j], population[j+1] = population[j+1], population[j]
                        population_fitness[j], population_fitness[j+1] = population_fitness[j+1], population_fitness[j]
                        
            
            #roulette wheel
            rws = population_fitness[:]
            rws = [k ** (-1) for k in rws]
            rws = rws  / np.sum(rws)
            rws = np.cumsum(rws)
            
            #elitism
            half = int(population_size / 2)
            counter = 0
            while counter < half:
                random_num = np.random.rand()
                
                for i in range(len(population)):
                    if random_num <= rws[i]:
                        elitists.append(population[i])
                        population.pop(i)
                        population_fitness.pop(i)
                        rws = population_fitness[:]
                        rws = [k ** (-1) for k in rws]
                        rws = rws  / np.sum(rws)
                        rws = np.cumsum(rws)
                        counter += 1
                        break
                
            population = []
            population_fitness = []
            population = elitists[:]
            for i in range(0, len(population)):
                population_fitness.append(HelpfulFunctions.evaluate(population[i]))
            
            #sort
            for _ in range(len(population)):
                for j in range(len(population) - 1):
                    if population_fitness[j] > population_fitness[j+1]:
                        population[j], population[j+1] = population[j+1], population[j]
                        population_fitness[j], population_fitness[j+1] = population_fitness[j+1], population_fitness[j]

            if population_fitness[0] < min_fitness - 15:
                min_res = population[0]
                min_fitness = population_fitness[0]
                counter = 0
            else:
                counter += 1
            
            best_fitnesses.append(population_fitness[0])
        
        x = np.arange(len(best_fitnesses))
        #y = 
        #x = [item[1] for item in population]
        #y = [item[2] for item in population]
        plt.plot(x, best_fitnesses)
        #plt.plot(x, y, 'ro')
        #plt.title(title)
        plt.show()
        
        
        return population[0]
    
    def distance(x1, y1, x2, y2):
        return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 
    
    def generate_offspring(population):
        offspring = []
        offspring_fitness = []
        
        max_number_of_offsprings = 20
        if len(population[0]) >= 50 and len(population[0]) < 100:
            max_number_of_offsprings = 30
        elif len(population[0]) >= 100:
            max_number_of_offsprings = 40
            
        for i in range(len(population)):
            if (np.random.rand() < 0.9):
                first = i
                second = -1
                while True:
                    second = np.random.randint(len(population))
                    if first != second:
                        break    
                first_child = HelpfulFunctions.OrderCrossover(population[first], population[second])
                second_child = HelpfulFunctions.OrderCrossover(population[second], population[first])                
                
                if np.random.rand() < 0.1:
                    first_child = HelpfulFunctions.TwoOpt(first_child)
                    
                if np.random.rand() < 0.1:
                    second_child = HelpfulFunctions.TwoOpt(second_child)
                
                offspring.append(first_child)
                offspring.append(second_child)
                offspring_fitness.append(HelpfulFunctions.evaluate(first_child))
                offspring_fitness.append(HelpfulFunctions.evaluate(second_child))
                if len(offspring) >= max_number_of_offsprings:
                    break
        return offspring, offspring_fitness
    
    def calculate_end(n):
        end = n
        
        for i in range(1, n + 1):
            end += i
        
        return end
    
    def evaluate(solution):
        dist = 0

        for i in range(0, len(solution) - 1):
            dist += HelpfulFunctions.distance(solution[i][1], solution[i][2], solution[i + 1][1], solution[i + 1][2])
        dist += HelpfulFunctions.distance(solution[-1][1], solution[-1][2], solution[0][1], solution[0][2])
        return dist
    
    def TwoOpt(solution):
  
        improved = True
        while improved:
            
            improved = False
            for i in range(0, len(solution) - 2):
                for j in range(i + 2, len(solution) - 1):
                    if j - i == 1:
                        continue
                    u1 = i
                    u2 = i + 1
                    v1 = j
                    v2 = j + 1
        
                    d1 = HelpfulFunctions.distance(solution[u1][1], solution[u1][2], solution[u2][1], solution[u2][2])
                    d2 = HelpfulFunctions.distance(solution[v1][1], solution[v1][2], solution[v2][1], solution[v2][2])
                    
                    d1_new = HelpfulFunctions.distance(solution[u1][1], solution[u1][2], solution[v1][1], solution[v1][2])
                    d2_new = HelpfulFunctions.distance(solution[u2][1], solution[u2][2], solution[v2][1], solution[v2][2])
    
                    old = d1 + d2
                    new = d1_new + d2_new
                    
                    if new < old:
                        reversed_solution = solution[u2:v1+1]
                        reversed_solution.reverse()
                        solution[u2:v1+1] = reversed_solution

                        improved = True
                        break
                if improved:
                    break

        return solution