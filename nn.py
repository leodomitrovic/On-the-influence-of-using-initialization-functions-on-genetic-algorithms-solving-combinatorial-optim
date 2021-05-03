import numpy as np
import urllib
import matplotlib.pyplot as plt

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
populacija.append(gradovi[0])
gradovi.pop(0)
x = []
y = []

while len(gradovi) > 0:
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
    
plt.plot(x, y)
plt.show()