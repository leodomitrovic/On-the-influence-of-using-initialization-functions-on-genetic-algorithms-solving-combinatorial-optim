import random
from hfunctions import HelpfulFunctions

class I1:

    def generate_solution(cities, solution_heur):
            
        cities_copy = cities[:]
        solution = []
        
        random_index = random.randint(0, len(cities_copy)-1)
        solution.append(cities_copy[random_index])
        cities_copy.pop(random_index)
        
        random_index = random.randint(0, len(cities_copy)-1)
        solution.append(cities_copy[random_index])
        cities_copy.pop(random_index)

        counter = 2        
        while counter < solution_heur:
            
            min_p_d = 100000
            min_p_i = -1
            min_p_g = -1
            for i in range(len(solution)):
                for j in range(len(cities_copy)):
                    d = HelpfulFunctions.distance(solution[i][1], cities_copy[j][1], solution[i][2], cities_copy[j][2]) + HelpfulFunctions.distance(solution[i-1][1], cities_copy[j][1], solution[i-1][2], cities_copy[j][2])
                    if d < min_p_d:
                        min_p_d = d
                        min_p_i = i
                        min_p_g = j
            solution.insert(min_p_i, cities_copy[min_p_g])
            cities_copy.pop(min_p_g)
            counter += 1

        while len(cities_copy) > 0:
            random_index = random.randint(0, len(cities_copy) - 1)
            solution.append(cities_copy[random_index])
            cities_copy.pop(random_index)
        return solution