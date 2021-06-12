from nn import NearestNeighbour
from insertion import Insertion
from pomocne import PomocneFunkcije

url1 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/berlin52.tsp"
url2 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/st70.tsp"
url3 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/eil76.tsp"
url4 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/kroA100.tsp"
url5 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/kroB100.tsp"
url6 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/kroC100.tsp"
url7 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/eil101.tsp"
url8 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr107.tsp"
url9 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr124.tsp"
url10 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr136.tsp"
url11 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr144.tsp"
url12 = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/pr152.tsp"
url13 = [[1, 54, 67], [2, 54, 62], [3, 37, 84], [4, 41, 94], [5, 2, 99], [6, 7, 64], [7, 25, 62], [8, 22, 60], [9, 18, 4],
         [10, 4, 50], [11, 13, 40], [12, 18, 40], [13, 24, 42], [14, 25, 38], [15, 44, 35], [16, 41, 26], [17, 45, 21],
         [18, 58, 35], [19, 62, 32], [20, 82, 7], [21, 91, 38], [22,  83, 46], [23, 71, 44], [24, 64, 60], [25, 68, 58],
         [26, 83, 69], [27, 87, 76], [28, 74, 78], [29, 71, 71], [30, 58, 69]]
url14 = [[1, 32, 22], [2, 27, 23], [3, 20, 26], [4, 17, 33], [5, 25, 32], [6, 31, 32], [7, 32, 39], [8, 30, 48], [9, 21, 47], 
         [10, 25, 55], [11, 16, 57], [12, 17, 63], [13, 5, 64], [14, 8, 52], [15, 12, 42], [16, 7, 38], [17, 5, 25], [18, 10, 17], 
         [19, 5, 6], [20, 13, 13], [21, 21, 10], [22, 30, 15], [23, 36, 16], [24, 39, 10], [25, 46, 10], [26, 59, 15], 
         [27, 51, 21], [28, 48, 28], [29, 52, 33], [30, 58, 27], [31, 61, 33], [32, 56, 37], [33, 52, 41], [34, 62, 42], 
         [35, 58, 48], [36, 49, 49], [37, 57, 58], [38, 62, 63], [39, 63, 69], [40, 52, 64], [41, 43, 67], [42, 37, 69], 
         [43, 27, 68], [44, 31, 62], [45, 42, 57], [46, 37, 52], [47, 38, 46], [48, 42, 41], [49, 45, 35], [50, 40, 30]]
url15 = [[1, 30, 20], [2, 27, 24], [3, 22, 22], [4, 26, 29], [5, 20, 30], [6, 21, 36], [7, 21, 45], [8, 21, 48], [9, 22, 53], 
         [10, 26, 59], [11, 30, 60], [12, 35, 60], [13, 40, 60], [14, 35, 51], [15, 30, 50], [16, 33, 44], [17, 29, 39], 
         [18, 33, 34], [19, 38, 33], [20, 40, 37], [21, 45, 35], [22, 45, 42], [23, 41, 46], [24, 50, 50], [25, 55, 50], 
         [26, 55, 57], [27, 62, 57], [28, 70, 64], [29, 57, 72], [30, 55, 65], [31, 50, 70], [32, 47, 66], [33, 40, 66], 
         [34, 31, 76], [35, 10, 70], [36, 17, 64], [37, 15, 56], [38, 9, 56], [39, 7, 43], [40, 12, 38], [41, 11, 28], [42, 6, 25], 
         [43, 12, 17], [44, 16, 19], [45, 15, 14], [46, 15, 5], [47, 26, 13], [48, 36, 6], [49, 44, 13], [50, 50, 15], [51, 54, 10], 
         [52, 50, 4], [53, 59, 5], [54, 64, 4], [55, 66, 8], [56, 66, 14], [57, 60, 15], [58, 55, 20], [59, 62, 24], [60, 65, 27], 
         [61, 62, 35], [62, 67, 41], [63, 62, 48], [64, 55, 45], [65, 51, 42], [66, 50, 40], [67, 54, 38], [68, 55, 34], 
         [69, 50, 30], [70, 52, 26], [71, 48, 21], [72, 43, 26], [73, 36, 26], [74, 40, 20], [75, 35, 16]]

population_size = 48

NN = NearestNeighbour(
    population_size = population_size,
    randomness = 1,
    url = url14,
)

population, population_fitness = NN.makePopulation()
najboljiNNnew = PomocneFunkcije.algorithm(population, population_fitness, population_size, new_crossover=True)
najboljiNNold = PomocneFunkcije.algorithm(population, population_fitness, population_size, new_crossover=False)
#PomocneFunkcije.nacrtaj(najboljiNN, "NN algoritam")
print(PomocneFunkcije.evaluate(najboljiNNnew))
print(PomocneFunkcije.evaluate(najboljiNNold))

"""
insertion = Insertion(
    population_size = population_size,
    randomness = 1,
    url = url1
)

population, population_fitness = insertion.makePopulation()
najboljiIn = PomocneFunkcije.algorithm(population, population_fitness, population_size)
PomocneFunkcije.nacrtaj(najboljiIn, "In algoritam")
print(PomocneFunkcije.evaluate(najboljiIn))
"""
