import random
from hfunctions import HelpfulFunctions

class NearestNeighbour:

    def generate_solution(cities, solution_heur):
        
        cities_copy = cities[:]
        solution = []
        random_index = random.randint(0, len(cities_copy) - 1)
        solution.append(cities_copy[random_index])
        cities_copy.pop(random_index)
    
        counter = 1        
        while counter < solution_heur:
            tmp = solution[-1]
            min_d = 1000000
            min_g = []
            min_i = 0
            for i in range(len(cities_copy)):
                d = HelpfulFunctions.distance(cities_copy[i][1], tmp[1], cities_copy[i][2], tmp[2])
                if d < min_d:
                    min_d = d
                    min_g = cities_copy[i]
                    min_i = i
            cities_copy.pop(min_i)
            solution.append(min_g)
            counter += 1
            
        while len(cities_copy) > 0:
            random_index = random.randint(0, len(cities_copy) - 1)
            solution.append(cities_copy[random_index])
            cities_copy.pop(random_index)
        return solution