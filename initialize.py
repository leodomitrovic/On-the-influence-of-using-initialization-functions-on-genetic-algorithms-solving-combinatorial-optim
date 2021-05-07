from nn import NearestNeighbour

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
         [18, 58, 35], [19, 62, 32], [20, 82,  7], [21, 91, 38], [22,  83, 46], [23, 71, 44], [24, 64, 60], [25, 68, 58],
         [26, 83, 69], [27, 87, 76], [28, 74, 78], [29, 71, 71], [30, 58, 69]]

NN = NearestNeighbour(
    population_size = 48,
    randomness = 1,
    url = url1
)

res = NN.calculate()
print (res)