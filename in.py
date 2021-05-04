import numpy as np
import urllib
import matplotlib.pyplot as plt
import random

# TODO: ispraviti logičku grešku, algoritam mi se ne čini ispravnim jer skače ko lud kad bi očito mogao pronaći bolje bliže točke

debugging = False

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
    
    if debugging:
        for i in populacija:
            x.append(i[1])
            y.append(i[2])
        x.append(populacija[0][1])
        y.append(populacija[0][2])
        plt.plot(x, y)
        plt.plot(x, y, 'ro')
        plt.show()
        x = []
        y = []

d_sum = 0
    
for i in range(len(populacija)):
    d_sum = d_sum + udaljenost(populacija[i][1], populacija[i-1][1], populacija[i][2], populacija[i-1][2])
    x.append(populacija[i][1])
    y.append(populacija[i][2])

x.append(populacija[0][1])
y.append(populacija[0][2])
    
plt.plot(x, y)
plt.plot(x, y, 'ro')
plt.show()

print("Ukupna udaljenost: " + str(d_sum))