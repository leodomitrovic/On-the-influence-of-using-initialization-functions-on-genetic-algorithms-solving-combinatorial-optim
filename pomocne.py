import numpy as np
import matplotlib.pyplot as plt
import random

class PomocneFunkcije:

    # vraća novo dijete
    def OrderCrossoverStari(first, second):
        
        # moguće da prvi crossover bude na većem indeksu od drugog!
        first_crossover = random.randint(0, len(first) - 3)
        while True:
            second_crossover = random.randint(0, len(first) - 3)
            if first_crossover != second_crossover:
                break
            
        tmp1 = first_crossover
        tmp2 = second_crossover
        first_crossover = min(tmp1, tmp2)
        second_crossover = max(tmp1, tmp2)
        
        child = first[first_crossover:second_crossover]
        #print(str(first_crossover) + ", " + str(second_crossover) + ", " + str(len(child)))
        
        sec_par_counter = -1
        # sad moramo pronaći grad first[second_crossover] u drugom roditelju
        for i, grad in enumerate(second):
            if grad == first[second_crossover]:
                sec_par_counter = i
                break
        
        if sec_par_counter == -1:
            print("greskaaaa")
            sec_par_counter = second_crossover
        
        while len(child) < len(second):
            #if child_counter > len(second)-first_crossover:
            #    child_counter = 0
            #if sec_par_counter > len(second) - 1:
            #    sec_par_counter = 0
            if sec_par_counter < 0:
                sec_par_counter = len(second) - 1
            # provjeri ako čvor puta iz second već je u child
            if second[sec_par_counter] not in child:
                #if child_counter < second_crossover-first_crossover+1:   
                child.append(second[sec_par_counter])
                #child.insert(child_counter, second[sec_par_counter])
                #else:
                #    child.append(second[sec_par_counter])
            
            sec_par_counter -= 1

        return child
    
    # vraća novo dijete
    def OrderCrossover(first, second):
        
        # moguće da prvi crossover bude na većem indeksu od drugog!
        first_crossover = random.randint(0, len(first) - 3)
        while True:
            second_crossover = random.randint(0, len(first) - 3)
            if first_crossover != second_crossover:
                break
            
        tmp1 = first_crossover
        tmp2 = second_crossover
        first_crossover = min(tmp1, tmp2)
        second_crossover = max(tmp1, tmp2)
        
        child = [None] * len(first)
        child[first_crossover:second_crossover] = first[first_crossover:second_crossover]
        
        remaining = []
        for i in range(second_crossover, second_crossover + len(second)):
            index = i % len(second)
            if second[index] not in child:
                remaining.append(second[index])
                
        for i in range(second_crossover, len(first)):
            child[i] = remaining[0]
            del remaining[0]
            
        for i in range(0, first_crossover):
            child[i] = remaining[0]
            del remaining[0]
        
        if len(remaining) > 0:
            print("WOOOPPAA")
        return child
    
    def nacrtaj(population, title):
        x = [item[1] for item in population]
        y = [item[2] for item in population]
        plt.plot(x, y)
        plt.plot(x, y, 'ro')
        plt.title(title)
        plt.show()
    
    def algorithm(population, population_fitness, population_size, new_crossover=True):
        brojac = 0
        while True:
            brojac += 1
            if brojac == 100:
                break
            
            # odabir roditelja
            # rekao bih da se roditelj bira sad u sljedećem koraku haha
            
            # križanje
            # uzeti čvor kao roditelja s vj 90%, drugog uzeti random i dobiti dvoje djece iz toga, ponavljati postupak
            ELITIST_SIZE = 12
            elitists = population[:ELITIST_SIZE]
            elitists_fitness = population_fitness[:ELITIST_SIZE]
            
            velicina_pop_prije_crossover = len(population)
            for first in range(0, velicina_pop_prije_crossover, 2):
                if (np.random.rand() < 0.8):
                    second = first + 1
                    
                    if new_crossover:
                        first_child = PomocneFunkcije.OrderCrossover(population[first], population[second])
                        second_child = PomocneFunkcije.OrderCrossover(population[second], population[first])
                    else:
                        first_child = PomocneFunkcije.OrderCrossoverStari(population[first], population[second])
                        second_child = PomocneFunkcije.OrderCrossoverStari(population[second], population[first])
                        
                    population[first] = first_child
                    population[second] = second_child
                    population_fitness[first] = PomocneFunkcije.evaluate(population[first])
                    population_fitness[second] = PomocneFunkcije.evaluate(population[second])
                    
            # 2-opt
            for i in range(0, len(population)):
                if (np.random.rand() < 0.1):
                    population[i] = PomocneFunkcije.TwoOpt(population[i])
                    population_fitness[i] = PomocneFunkcije.evaluate(population[i])
            
            # Sort
            for _ in range(len(population)):
                for j in range(len(population) - 1):
                    if population_fitness[j] > population_fitness[j+1]:
                        population[j], population[j+1] = population[j+1], population[j]
                        population_fitness[j], population_fitness[j+1] = population_fitness[j+1], population_fitness[j]
            
            # Elitizam
            half = int(population_size / 2)
            br = 0
            while br < half:
                slucajniIndeks = random.randint(0, len(population) - 1)
                elitists.append(population[slucajniIndeks])
                population.pop(slucajniIndeks)
                br += 1
            population.clear
            population_fitness.clear
            population = elitists
            for i in range(0, len(population)):
                    population_fitness[i] = PomocneFunkcije.evaluate(population[i])
                        
            # Sort
            for _ in range(len(population)):
                for j in range(len(population) - 1):
                    if population_fitness[j] > population_fitness[j+1]:
                        population[j], population[j+1] = population[j+1], population[j]
                        population_fitness[j], population_fitness[j+1] = population_fitness[j+1], population_fitness[j]
                        
            print("Min: {:.2f}\tMean: {:.2f}\tMax: {:.2f}".format(np.min(population_fitness), np.mean(population_fitness), np.max(population_fitness)))
            
        return population[0]
    
    def udaljenost(x1, y1, x2, y2):
        return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 

    def evaluate(solution):
        dist = 0

        for i in range(0, len(solution) - 1):
            dist += PomocneFunkcije.udaljenost(solution[i][1], solution[i][2], solution[i + 1][1], solution[i + 1][2])
        dist += PomocneFunkcije.udaljenost(solution[-1][1], solution[-1][2], solution[0][1], solution[0][2])
        return dist    
    
    def TwoOpt(solution):
        improved = True
        debugging = False
        
        br = 0
        while improved:
            if br > 30:
                break
            
            improved = False
            for i in range(0, len(solution) - 2):
                for j in range(i + 2, len(solution) - 1):
                    if j - i == 1:
                        continue
                    u1 = i
                    u2 = i + 1
                    v1 = j
                    v2 = j + 1
        
                    d1 = PomocneFunkcije.udaljenost(solution[u1][1], solution[u1][2], solution[u2][1], solution[u2][2])
                    d2 = PomocneFunkcije.udaljenost(solution[v1][1], solution[v1][2], solution[v2][1], solution[v2][2])
                    
                    d1_new = PomocneFunkcije.udaljenost(solution[u1][1], solution[u1][2], solution[v1][1], solution[v1][2])
                    d2_new = PomocneFunkcije.udaljenost(solution[u2][1], solution[u2][2], solution[v2][1], solution[v2][2])
    
                    old = d1 + d2
                    new = d1_new + d2_new
                    
                    if new < old:
                        br += 1
                        improved = True
                        
                        if debugging:
                            x = [item[1] for item in solution]
                            y = [item[2] for item in solution]
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()
                        
                        pom = []
                        for k in range(u2, v1 + 1):
                            pom.append(solution[k])
                        pom.reverse()
                        
                        l = 0
                        for k in range(u2, v1 + 1):
                            solution[k] = pom[l]
                            l += 1
        
                        if debugging:
                            x = [item[1] for item in solution]
                            y = [item[2] for item in solution]
                            plt.plot(x, y)
                            plt.plot(x, y, 'bo')
                            plt.plot([solution[u1][1], solution[u2][1]], [solution[u1][2], solution[u2][2]], color='g', lw=2)
                            plt.plot([solution[v1][1], solution[v2][1]], [solution[v1][2], solution[v2][2]], color='r', lw=2)
                            plt.show()
                        break
                
                if improved:
                    break
        return solution
