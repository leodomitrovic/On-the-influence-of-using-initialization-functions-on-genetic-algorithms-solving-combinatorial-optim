import numpy as np
import matplotlib.pyplot as plt
import random

class HelpfulFunctions:
    
    
    def makePopulation(heuristic, population_size, cities, randomness):
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
            solution = heuristic.generate_solution(cities.copy(), solution_heur)
            #random.shuffle(solution)
            population.append(solution)
            population_fitness.append(HelpfulFunctions.evaluate(solution))
            
        #print("population made")
        return population, population_fitness
    
    def OrderCrossover(first, second):
        first_crossover = random.randint(0, len(first) - 3)
        
        while True:
            second_crossover = random.randint(0, len(first) - 3)
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
    
    def algorithm(population, population_fitness, population_size, city_size):
        counter = 0
        total = 0
        end = HelpfulFunctions.calculate_end(city_size)
        #min_res = []
        #min_fitness = 100000
        while True:
            if counter == end:
                break
            
            # Sort
            for _ in range(len(population)):
                for j in range(len(population) - 1):
                    if population_fitness[j] > population_fitness[j+1]:
                        population[j], population[j+1] = population[j+1], population[j]
                        population_fitness[j], population_fitness[j+1] = population_fitness[j+1], population_fitness[j]
            
            ELITIST_SIZE = int(population_size/2)
            elitists = population[:ELITIST_SIZE]
            elitists_fitness = population_fitness[:ELITIST_SIZE]
            
            # crossover
            size_of_pop_before_crossover = len(population)
            for first in range(0, size_of_pop_before_crossover, 2):
                if (np.random.rand() < 0.8):
                    second = first + 1
                        
                    first_child = HelpfulFunctions.OrderCrossover(population[first], population[second])
                    second_child = HelpfulFunctions.OrderCrossover(population[second], population[first])
                    
                    population[first] = first_child
                    population[second] = second_child
                    population_fitness[first] = HelpfulFunctions.evaluate(population[first])
                    population_fitness[second] = HelpfulFunctions.evaluate(population[second])
                    
            # 2-opt
            for i in range(0, len(population)):
                if (np.random.rand() < 0.1):
                    population[i] = HelpfulFunctions.TwoOpt(population[i])
                    population_fitness[i] = HelpfulFunctions.evaluate(population[i])
            
            # postoji šansa 18% da jedinka nije prošla kroz križanje i mutaciju pa ju izbacujemo iz populacije budući da je već u elists
            for i in reversed(range(len(population))):
                if population_fitness[i] in elitists_fitness:
                    del population[i]
                    del population_fitness[i]
            
            # Sort
            for _ in range(len(population)):
                for j in range(len(population) - 1):
                    if population_fitness[j] > population_fitness[j+1]:
                        population[j], population[j+1] = population[j+1], population[j]
                        population_fitness[j], population_fitness[j+1] = population_fitness[j+1], population_fitness[j]
            
            # Elitizam
            half = int(population_size / 2)
            counter = 0
            while counter < half:
                random_index = random.randint(0, len(population) - 1)
                elitists.append(population[random_index])
                population.pop(random_index)
                counter += 1
            population.clear
            population_fitness = []
            population = elitists
            for i in range(0, len(population)):
                population_fitness.append(HelpfulFunctions.evaluate(population[i]))
            
            #print("Min: {:.2f}\tMean: {:.2f}\tMax: {:.2f}".format(np.min(population_fitness), np.mean(population_fitness), np.max(population_fitness)))
            """if population_fitness[0] < min_fitness + 5:
                min_res = population[0]
                min_fitness = population_fitness[0]
                counter = 0
            else:
                counter += 1"""
            counter += 1
            total += 1
            if counter % 10 == 0:
                print(counter)
        
        print (total)
        return population[0]
    
    def distance(x1, y1, x2, y2):
        manhattan_distance = True
        
        if manhattan_distance:
            return abs(x1 - x2) + abs(y1 - y2) 
        else:
            return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 
    
    def calculate_end(n):
        end = n
        
        for i in range(1, n + 1):
            end += i
        
        return end
        
    def sort(population, population_fitness):
        merged_list = list(zip(population, population_fitness))
        merged_list.sort(key=lambda merged_list_member: merged_list_member[1], reverse=True)
        population, population_fitness = zip(*merged_list)
        population_fitness = [score**(-1) for score in population_fitness]
        return population, population_fitness
    
    def evaluate(solution):
        dist = 0

        for i in range(0, len(solution) - 1):
            dist += HelpfulFunctions.distance(solution[i][1], solution[i][2], solution[i + 1][1], solution[i + 1][2])
        dist += HelpfulFunctions.distance(solution[-1][1], solution[-1][2], solution[0][1], solution[0][2])
        return dist
    
    def Elitizam(population, population_fitness, population_size):
        population, population_fitness = HelpfulFunctions.sort(population, population_fitness)
        population = list(population)
        
        half = int(population_size / 2)
        tmp_population = []
        for i in range(0, half):
            tmp_population.append(population[0])
            population.pop(0)
        
        counter = half
        while counter < population_size:
            random_index = random.randint(0, len(population) - 1)
            tmp_population.append(population[random_index])
            population.pop(random_index)
            counter += 1
        population = tmp_population
        for i in range(0, len(population)):
                population_fitness[i] = HelpfulFunctions.evaluate(population[i])
                
        return population, population_fitness
    
    def TwoOpt(solution):
        debugging = False
        
        best_distance = HelpfulFunctions.evaluate(solution)
        improvement_threshold=0.01
        improvement_factor = 1
        
        counter = 0
        while improvement_factor > improvement_threshold:
            
            previous_best  = best_distance

            if counter > 30:
                break
            
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
                        counter += 1
                        
                        if debugging:
                            x = [item[1] for item in solution]
                            y = [item[2] for item in solution]
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()
                        
                        reversed_solution = solution[u2:v1+1]
                        reversed_solution.reverse()
                        solution[u2:v1+1] = reversed_solution
                        
                        # stari reverse
                        """pom = []
                        for k in range(u2, v1 + 1):
                            pom.append(solution[k])
                        pom.reverse()
                        
                        l = 0
                        for k in range(u2, v1 + 1):
                            solution[k] = pom[l]
                            l += 1
                        """
                        
                        if debugging:
                            x = [item[1] for item in solution]
                            y = [item[2] for item in solution]
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()

            improvement_factor = 1 - best_distance/previous_best
            break
        return solution
