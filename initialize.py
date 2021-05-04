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

NN = NearestNeighbour(
    population_size = 48,
    randomness = 1,
    url = url1
)

res = NN.calculate()
print (res)