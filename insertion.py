import urllib
import random
from pomocne import PomocneFunkcije

class Insertion:
    def __init__(
            self,
            population_size,
            randomness,
            url
    ):
        self.population_size = population_size
        self.randomness = randomness
        self.url = url
    
    def generate_solution(self, gradovi):
        solution_heur = 0 
        if self.randomness == 1:
            solution_heur = len(gradovi)
        elif self.randomness == 0.5:
            solution_heur = int(len(gradovi) / 2)
        elif self.randomness == 0.1:
            solution_heur = int(len(gradovi) * 0.1)
        else: 
            solution_heur = 0
    
        solution = []
        gradovi_copy = gradovi[:]

        slucajniIndeks = random.randint(0, len(gradovi_copy)-1)
        solution.append(gradovi[slucajniIndeks])
        gradovi_copy.pop(slucajniIndeks)
        
        slucajniIndeks = random.randint(0, len(gradovi_copy)-1)
        solution.append(gradovi[slucajniIndeks])
        gradovi_copy.pop(slucajniIndeks)

        br = 2
        while br < solution_heur:
            
            min_g_d = 10000
            min_g = []
            min_i = 0
            for j in range(len(solution)):
                tmp = solution[j]
                for i in range(len(gradovi)):
                    d = PomocneFunkcije.udaljenost(gradovi[i][1], tmp[1], gradovi[i][2], tmp[2])
                    if d < min_g_d:
                        min_g_d = d
                        min_g = gradovi[i]
                        min_i = i
            
            min_p_d = 100000
            min_p_i = -1
            for i in range(len(solution)):
                d = PomocneFunkcije.udaljenost(solution[i][1], min_g[1], solution[i][2], min_g[2]) + PomocneFunkcije.udaljenost(solution[i-1][1], min_g[1], solution[i-1][2], min_g[2])
                if d < min_p_d:
                    min_p_d = d
                    min_p_i = i
            solution.insert(min_p_i, min_g)
            gradovi.pop(min_i)
            br += 1
        
        while br < len(gradovi_copy):
            slucajniIndeks = random.randint(0, len(gradovi_copy)-1)
            solution.append(gradovi_copy[slucajniIndeks])
            gradovi_copy.pop(slucajniIndeks)
            br += 1
        return solution
    
    
    def makePopulation(self):
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
            population_fitness.append(PomocneFunkcije.evaluate(solution))
        return population, population_fitness