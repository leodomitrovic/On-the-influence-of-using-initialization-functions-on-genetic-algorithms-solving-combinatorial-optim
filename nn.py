import numpy as np
import urllib
import matplotlib.pyplot as plt
import random

class NearestNeighbour:
    def __init__(
            self,
            population_size,
            randomness,
            url
    ):
        self.population_size = population_size
        self.randomness = randomness
        self.url = url
     
    def udaljenost(self, x1, y1, x2, y2):
        return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 
    
    def sort(self, population, population_fitness):
        merged_list = list(zip(population, population_fitness))
        merged_list.sort(key=lambda merged_list_member: merged_list_member[1], reverse=True)
        population, population_fitness = zip(*merged_list)
        population_fitness = [score**(-1) for score in population_fitness]
        
    def generate_solution(self, gradovi):
        solution_heur = 0
        if self.randomness == 1:
            solution_heur = 52
        elif self.randomness == 0.5:
            solution_heur = 26
        elif self.randomness == 0.1:
            solution_heur = 5
        else: 
            solution_heur = 0
        
        gradovi_copy = gradovi[:]
        solution = []
        slucajniIndeks = random.randint(0, len(gradovi_copy)-1)
        solution.append(gradovi_copy[slucajniIndeks])
        gradovi_copy.pop(slucajniIndeks)
        
        br = 1
        
        while br < solution_heur:
            tmp = solution[-1]
            min_d = 10000
            min_g = []
            min_i = 0
            for i in range(len(gradovi_copy)):
                d = np.sqrt(pow(gradovi_copy[i][1] - tmp[1], 2) + pow(gradovi_copy[i][2] - tmp[2], 2))
                if d < min_d:
                    min_d = d
                    min_g = gradovi_copy[i]
                    min_i = i
            gradovi_copy.pop(min_i)
            solution.append(min_g)
            br += 1
            
        while br < len(gradovi_copy):
            slucajniIndeks = random.randint(0, len(gradovi_copy)-1)
            solution.append(gradovi_copy[slucajniIndeks])
            gradovi_copy.pop(slucajniIndeks)
            br += 1
        return solution
        
    def TwoOpt(self, solution):
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
        
                    d1 = self.udaljenost(solution[u1][1], solution[u1][2], solution[u2][1], solution[u2][2])
                    d2 = self.udaljenost(solution[v1][1], solution[v1][2], solution[v2][1], solution[v2][2])
                    
                    d1_new = self.udaljenost(solution[u1][1], solution[u1][2], solution[v1][1], solution[v1][2])
                    d2_new = self.udaljenost(solution[u2][1], solution[u2][2], solution[v2][1], solution[v2][2])
                    
                    old = d1 + d2
                    new = d1_new + d2_new
                    
                    if new < old:
                        br += 1
                        improved = True
                        
                        if debugging:
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
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()
                        break
                
                if improved:
                    break
        return solution
    
    def evaluate(self, solution):
        dist = 0
        for i in range(0, len(solution) - 1):
            dist += self.udaljenost(solution[i][1], solution[i][2], solution[i + 1][1], solution[i + 1][2])
        return dist
    
    def algorithm(self):
        gradovi = []
        if isinstance(self.url, list):
            gradovi = self.url
        else:
            file1 = urllib.request.urlopen(self.url)
            file = []
            i = 0
            for line in file1: 
                i += 1
                l = line.decode("utf-8").split()
                file.append(l)
                if i >= 7 and i <= 58:
                    tmp = []
                    for k in l:
                        tmp.append(float(k))
                    gradovi.append(tmp)
        
        # Inicijalizacija            
        population_size = 48
        population = []
        population_fitness = []
        for i in range(1, population_size + 1):
            solution = self.generate_solution(gradovi)
            population.append(solution)
            population_fitness.append(self.evaluate(solution))
       
        iteration = 0
        while True:
            if (iteration == 100):
                break
            
            # odabir roditelja
            
            # križanje
            
            
            # 2-opt
            for i in range(0, population_size):
                if (np.random.rand() < 0.1):
                    population[i] = self.TwoOpt(population[i])
            
            # elitizam
            self.sort(population, population_fitness)
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
            iteration += 1
            population = pom_populacija
        return population[0]