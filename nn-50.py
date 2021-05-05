import numpy as np
import urllib
import matplotlib.pyplot as plt
import random

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
x = []
y = []
br = 1
populacija_heur = 24

while br < populacija_heur:
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
    br += 1
    
while br < velicina_populacije:
    slucajniIndeks = random.randint(0, len(gradovi)-1)
    populacija.append(gradovi[slucajniIndeks])
    x.append(gradovi[slucajniIndeks][1])
    y.append(gradovi[slucajniIndeks][2])
    gradovi.pop(slucajniIndeks)
    br += 1

plt.plot(x, y)
plt.plot(x, y, 'ro')
plt.show()