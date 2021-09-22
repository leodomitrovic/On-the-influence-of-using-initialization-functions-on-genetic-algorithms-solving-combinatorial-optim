import random
from hfunctions import HelpfulFunctions

class Insertion:
    
    def generate_solution(cities, solution_heur):
    
        cities_copy = cities[:]
        solution = []

        random_index = random.randint(0, len(cities_copy)-1)
        solution.append(cities_copy[random_index])
        cities_copy.pop(random_index)
        
        random_index = random.randint(0, len(cities_copy)-1)
        solution.append(cities_copy[random_index])
        cities_copy.pop(random_index)

        counter2 = 2
        while counter2 < solution_heur:
            
            min_g_d = 10000000
            min_g = []
            min_i = 0
            for j in range(len(solution)):
                tmp = solution[j]
                for i in range(len(cities_copy)):
                    d = HelpfulFunctions.distance(cities_copy[i][1], tmp[1], cities_copy[i][2], tmp[2])
                    if d < min_g_d:
                        min_g_d = d
                        min_g = cities_copy[i]
                        min_i = i
            
            min_p_d = 10000000
            min_p_i = -1
            for i in range(len(solution)):
                d = HelpfulFunctions.distance(solution[i][1], min_g[1], solution[i][2], min_g[2]) + HelpfulFunctions.distance(solution[i-1][1], min_g[1], solution[i-1][2], min_g[2])
                if d < min_p_d:
                    min_p_d = d
                    min_p_i = i
            solution.insert(min_p_i, min_g)
            cities_copy.pop(min_i)
            counter2 += 1
        
        while len(cities_copy) > 0:
            random_index = random.randint(0, len(cities_copy) - 1)
            solution.append(cities_copy[random_index])
            cities_copy.pop(random_index)
        return solution
