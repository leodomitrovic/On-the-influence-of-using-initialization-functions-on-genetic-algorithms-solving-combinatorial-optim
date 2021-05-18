import numpy as np
import matplotlib.pyplot as plt
import random

class PomocneFunkcije:
    
    def nacrtaj(population, title):
        x = [item[1] for item in population]
        y = [item[2] for item in population]
        plt.plot(x, y)
        plt.plot(x, y, 'ro')
        plt.title(title)
        plt.show()
    
    def algorithm(population, population_fitness, population_size):
        brojac = 0
        while True:
            brojac += 1
            if brojac == 100:
                break
            
            # 2-opt
            for i in range(0, len(population)):
                if (np.random.rand() < 0.1):
                    population[i] = PomocneFunkcije.TwoOpt(population[i])
                    population_fitness[i] = PomocneFunkcije.evaluate(population[i])
            
            # elitizam
            population, population_fitness = PomocneFunkcije.Elitizam(population, population_fitness, population_size)
        return population[0]
    
    def udaljenost(x1, y1, x2, y2):
        return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 
    
    def sort(population, population_fitness):
        merged_list = list(zip(population, population_fitness))
        merged_list.sort(key=lambda merged_list_member: merged_list_member[1], reverse=True)
        population, population_fitness = zip(*merged_list)
        population_fitness = [score**(-1) for score in population_fitness]
        return population, population_fitness
    
    def evaluate(solution):
        dist = 0
        for i in range(0, len(solution) - 1):
            dist += PomocneFunkcije.udaljenost(solution[i][1], solution[i][2], solution[i + 1][1], solution[i + 1][2])
        return dist
    
    def Elitizam(population, population_fitness, population_size):
        population, population_fitness = PomocneFunkcije.sort(population, population_fitness)
        population = list(population)
        
        half = int(population_size / 2)
        pom_populacija = []
        for i in range(0, half):
            pom_populacija.append(population[0])
            population.pop(0)
        
        br = half
        while br < population_size:
            slucajniIndeks = random.randint(0, len(population) - 1)
            pom_populacija.append(population[slucajniIndeks])
            population.pop(slucajniIndeks)
            br += 1
        population = pom_populacija
        for i in range(0, len(population)):
                population_fitness[i] = PomocneFunkcije.evaluate(population[i])
                
        return population, population_fitness
    
    def TwoOpt(solution):
        improved = True
        debugging = False
        
        br = 0
        while improved:
            if br > 30:
                break
            
            improved = False
            for i in range(0, len(solution) - 2):
                for j in range(i + 2, len(solution) - 1):
                    if j - i == 1:
                        continue
                    u1 = i
                    u2 = i + 1
                    v1 = j
                    v2 = j + 1
        
                    d1 = PomocneFunkcije.udaljenost(solution[u1][1], solution[u1][2], solution[u2][1], solution[u2][2])
                    d2 = PomocneFunkcije.udaljenost(solution[v1][1], solution[v1][2], solution[v2][1], solution[v2][2])
                    
                    d1_new = PomocneFunkcije.udaljenost(solution[u1][1], solution[u1][2], solution[v1][1], solution[v1][2])
                    d2_new = PomocneFunkcije.udaljenost(solution[u2][1], solution[u2][2], solution[v2][1], solution[v2][2])
    
                    old = d1 + d2
                    new = d1_new + d2_new
                    
                    if new < old:
                        br += 1
                        improved = True
                        
                        if debugging:
                            x = [item[1] for item in solution]
                            y = [item[2] for item in solution]
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()
                        
                        pom = []
                        for k in range(u2, v1 + 1):
                            pom.append(solution[k])
                        pom.reverse()
                        
                        l = 0
                        for k in range(u2, v1 + 1):
                            solution[k] = pom[l]
                            l += 1
        
                        if debugging:
                            x = [item[1] for item in solution]
                            y = [item[2] for item in solution]
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()
                        break
                
                if improved:
                    break
        return solution