from hfunctions import HelpfulFunctions
import time
from nn import NearestNeighbour
from cities import cities
    
tsp_index = 7

def TwoOpt(solution, withwhile=True):
    debugging = False
    
    best_distance = HelpfulFunctions.evaluate(solution)
    improvement_threshold=0.001
    improvement_factor = 1
    
    print("twoopt start")
    
    execution_times = []
    start_time = time.time()*1000
    
    counter = 0
    improved = True
    while withwhile or counter < 1:
        
        previous_best = best_distance
        improved = False
        for i in range(0, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                if j - i == 1:
                    continue
                u1 = i
                u2 = i + 1
                v1 = j
                v2 = j + 1
    
                d1 = HelpfulFunctions.distance(solution[u1][1], solution[u1][2], solution[u2][1], solution[u2][2])
                d2 = HelpfulFunctions.distance(solution[v1][1], solution[v1][2], solution[v2][1], solution[v2][2])
                
                d1_new = HelpfulFunctions.distance(solution[u1][1], solution[u1][2], solution[v1][1], solution[v1][2])
                d2_new = HelpfulFunctions.distance(solution[u2][1], solution[u2][2], solution[v2][1], solution[v2][2])

                old = d1 + d2
                new = d1_new + d2_new
                
                if new < old:
                    counter += 1

                    reversed_solution = solution[u2:v1+1]
                    reversed_solution.reverse()
                    solution[u2:v1+1] = reversed_solution

                    improved = True
                    break
            if improved and withwhile:
                break
        if not improved:
            break
    
    print("time: " + str(time.time()*1000-start_time) + ", # of changes: " + str(counter))
    return solution

solution = [[1, 0, 0], [2, 300, 0], [3, 310, 30], [4, 270, 30], [5, 80, 30], [6, 15, 30], [7, 15, 40], [8, 80, 40], [9, 270, 40], [10, 310, 40], [11, 300, 70], [12, 0, 70], [13, 0, 0]]

HelpfulFunctions.draw(solution, "before 2-opt")

solution = TwoOpt(solution)
HelpfulFunctions.draw(solution, "after 2-opt")

"""first = NearestNeighbour.generate_solution(cities.cities[tsp_index], len(cities.cities[tsp_index]))
second = NearestNeighbour.generate_solution(cities.cities[tsp_index], len(cities.cities[tsp_index]))

while True:

    solution1 = HelpfulFunctions.OrderCrossover(first, second)
    solution2 = HelpfulFunctions.OrderCrossover(second, first)
        
    solution1 = TwoOpt(solution1)
    solution2 = TwoOpt(solution2)
    
    first = solution1
    second = solution2"""