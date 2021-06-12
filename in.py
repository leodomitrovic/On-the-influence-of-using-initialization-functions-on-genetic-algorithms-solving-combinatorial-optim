import numpy as np
import urllib
import matplotlib.pyplot as plt
import random
from pomocne import PomocneFunkcije

<<<<<<< Updated upstream
debugging = False
randomness = 0

url = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/berlin52.tsp"
file1 = urllib.request.urlopen(url)
file = []
gradovi = []
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

populacija = []
velicina_populacije = 48

slucajniIndeks = random.randint(0, len(gradovi)-1)
populacija.append(gradovi[slucajniIndeks])
gradovi.pop(slucajniIndeks)

slucajniIndeks = random.randint(0, len(gradovi)-1)
populacija.append(gradovi[slucajniIndeks])
gradovi.pop(slucajniIndeks)

x = []
y = []
br = 2

def udaljenost(x1, x2, y1, y2):
    return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

while br < velicina_populacije:
    
    rand_num = random.randint(0, 100)
    if randomness < rand_num:
        min_g_d = 10000
        min_g = []
        min_i = 0
        for j in range(len(populacija)):
            tmp = populacija[j]
            for i in range(len(gradovi)):
                d = udaljenost(gradovi[i][1], tmp[1], gradovi[i][2], tmp[2])
                if d < min_g_d:
                    min_g_d = d
                    min_g = gradovi[i]
                    min_i = i
    else:
        min_i = random.randint(0, len(gradovi)-1)
        min_g = gradovi[min_i]
        
    min_p_d = 100000
    min_p = []
    min_p_i = -1
    for i in range(len(populacija)):
        d = udaljenost(populacija[i][1], min_g[1], populacija[i][2], min_g[2]) + udaljenost(populacija[i-1][1], min_g[1], populacija[i-1][2], min_g[2])
        if d < min_p_d:
            min_p_d = d
            min_p_i = i
    populacija.insert(min_p_i, min_g)
    gradovi.pop(min_i)

    br += 1
=======
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
    
>>>>>>> Stashed changes
    
        solution = []
        gradovi_copy = gradovi[:]

        slucajniIndeks = random.randint(0, len(gradovi)-1)
        solution.append(gradovi[slucajniIndeks])
        gradovi_copy.pop(slucajniIndeks)
        
        slucajniIndeks = random.randint(0, len(gradovi)-1)
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
            min_p = []
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