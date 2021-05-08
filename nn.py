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
        
    def udaljenost(self, x1, x2, y1, y2):
        return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        
    def calculate(self):
        population_heur = 0
        if self.randomness == 1:
            population_heur = 48
        elif self.randomness == 0.5:
            population_heur = 24
        elif self.randomness == 0.1:
            population_heur = 5
        else: 
            population_heur = 0
        
        gradovi = []
        debugging = True
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
        
        populacija = []
        slucajniIndeks = random.randint(0, len(gradovi)-1)
        populacija.append(gradovi[slucajniIndeks])
        gradovi.pop(slucajniIndeks)
        x = []
        y = []
        ukupno = 0
        br = 1
        if len(gradovi) < population_heur:
            population_heur = len(gradovi)
            self.population_size = len(gradovi) + 1
        
        while br < population_heur + 1:
            tmp = populacija[-1]
            min_d = 10000
            min_g = []
            min_i = 0
            for i in range(len(gradovi)):
                d = np.sqrt(pow(gradovi[i][1] - tmp[1], 2) + pow(gradovi[i][2] - tmp[2], 2))
                if d < min_d:
                    min_d = d
                    min_g = gradovi[i]
                    min_i = i
            gradovi.pop(min_i)
            populacija.append(min_g)
            x.append(min_g[1])
            y.append(min_g[2])
            ukupno += min_d
            br += 1
            
        while br < self.population_size:
            slucajniIndeks = random.randint(0, len(gradovi)-1)
            populacija.append(gradovi[slucajniIndeks])
            x.append(gradovi[slucajniIndeks][1])
            y.append(gradovi[slucajniIndeks][2])
            gradovi.pop(slucajniIndeks)
            br += 1
        
        print (ukupno)
        
        improved = True
        br = 0
        while improved:
            improved = False
            for i in range(0, self.population_size - 2):
                for j in range(i + 2, self.population_size):
                    if j - i == 1:
                        continue
                    u1 = i
                    u2 = i + 1
                    v1 = j
                    v2 = j + 1
                    
                    d1 = self.udaljenost(populacija[u1][1], populacija[u1][2], populacija[u2][1], populacija[u2][2])
                    d2 = self.udaljenost(populacija[v1][1], populacija[v1][2], populacija[v2][1], populacija[v2][2])
                    
                    d1_new = self.udaljenost(populacija[u1][1], populacija[u1][2], populacija[v1][1], populacija[v1][2])
                    d2_new = self.udaljenost(populacija[u2][1], populacija[u2][2], populacija[v2][1], populacija[v2][2])
                    
                    old = d1 + d2
                    new = d1_new + d2_new
                    
                    if new < old:
                        br += 1
                        improved = True
                        pom = []
                        for i in range(u2, v1 + 1):
                            pom.append(populacija[i])
                        pom.reverse()
                        
                        j = 0
                        for i in range(u2, v1 + 1):
                            populacija[i] = pom[j]
                            x[i] = pom[j][1]
                            y[i] = pom[j][2]
                            j += 1
                        ukupno -= old - new
                        break
                
                if improved:
                    break
        
        plt.plot(x, y)
        plt.plot(x, y, 'ro')
        plt.show()
        print (br)
        return ukupno