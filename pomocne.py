import numpy as np
import urllib
import matplotlib.pyplot as plt
import random
class PomocneFunkcije:
    
    def nacrtaj(population, title):
        x = [item[1] for item in population]
        y = [item[2] for item in population]
        plt.plot(x, y)
        plt.plot(x, y, 'ro')
        plt.title(title)
        plt.show()
    
    def algorithm(population, population_fitness, population_size):
        iteration = 0
        while True:
            if (iteration == 100):
                break
            
            # odabir roditelja
            # rekao bih da se roditelj bira sad u sljedećem koraku haha
            
            # križanje
            # uzeti čvor kao roditelja s vj 90%, drugog uzeti random i dobiti dvoje djece iz toga, ponavljati postupak
            velicina_pop_prije_crossover = len(population)
            for first in range(0, velicina_pop_prije_crossover-1):
                if (np.random.rand() < 0.9):
                    #uzimanje drugog čvora randomly
                    while True:
                        second = random.randint(0, velicina_pop_prije_crossover-1)
                        if first != second:
                            break
                        
                    first_child = PomocneFunkcije.OrderCrossover(population[first], population[second])
                    second_child = PomocneFunkcije.OrderCrossover(population[second], population[first])
                    
                    population[first] = first_child
                    population[second] = second_child
                    population_fitness[first] = PomocneFunkcije.evaluate(population[first])
                    population_fitness[second] = PomocneFunkcije.evaluate(population[second])
            
            # 2-opt
            for i in range(0, len(population)):
                if (np.random.rand() < 0.1):
                    population[i] = PomocneFunkcije.TwoOpt(population[i])
                    population_fitness[i] = PomocneFunkcije.evaluate(population[i])
            
            # elitizam
            population, population_fitness = PomocneFunkcije.sort(population, population_fitness)
            population = list(population)
            
            half = int(len(population) / 2)
            pom_populacija = []
            for i in range(0, half):
                pom_populacija.append(population[0])
                population.pop(0)
            
            br = half
            while br < population_size:
                slucajniIndeks = random.randint(0, len(population) - 1)
                pom_populacija.append(population[slucajniIndeks])
                population.pop(slucajniIndeks)
                br += 1
            population = pom_populacija
            
            iteration += 1
        return population[0]
    
    def udaljenost(x1, y1, x2, y2):
        return np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 
    
    def sort(population, population_fitness):
        merged_list = list(zip(population, population_fitness))
        merged_list.sort(key=lambda merged_list_member: merged_list_member[1], reverse=True)
        population, population_fitness = zip(*merged_list)
        population_fitness = [score**(-1) for score in population_fitness]
        return population, population_fitness
    
    def evaluate(solution):
        dist = 0
        for i in range(0, len(solution) - 1):
            dist += PomocneFunkcije.udaljenost(solution[i][1], solution[i][2], solution[i + 1][1], solution[i + 1][2])
        return dist
    
    # vraća novo dijete
    def OrderCrossover(first, second):
        debugging = False
        
        first_crossover = random.randint(0, len(first) - 3)
        while True:
            second_crossover = random.randint(first_crossover+1, len(first) - 1)
            if first_crossover != second_crossover:
                break
        child = first[first_crossover:second_crossover]
        #print(str(first_crossover) + ", " + str(second_crossover) + ", " + str(len(child)))
        child_counter = second_crossover-first_crossover+1
        
        
        sec_par_counter = -1
        # sad moramo pronaći grad first[second_crossover] u second
        for i, grad in enumerate(second):
            if grad == first[second_crossover]:
                sec_par_counter = i
                break
        
        if debugging:
            x = [item[1] for item in first]
            y = [item[2] for item in first]
            plt.plot(x, y)
            plt.plot(x, y, 'bo')
            x = [item[1] for item in first[first_crossover:second_crossover]]
            y = [item[2] for item in first[first_crossover:second_crossover]]
            #plt.plot(x, y, color='g', lw=2)
            plt.plot(x, y, color='r', lw=2)
            plt.title("first parent")
            plt.show()
            
            x = [item[1] for item in second]
            y = [item[2] for item in second]
            plt.plot(x, y)
            plt.plot(x, y, 'bo')
            x = [second[sec_par_counter][1]]
            y = [second[sec_par_counter][2]]
            plt.plot(x, y, 'mo', markersize=5)
            #plt.plot(x, y, color='ro', lw=2)
            plt.title("second parent")
            plt.show()
        
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
                child_counter += 1
                #else:
                #    child.append(second[sec_par_counter])
            if debugging: 
            
                x = [item[1] for item in child]
                y = [item[2] for item in child]
                plt.plot(x, y, 'bo')
                plt.plot(x, y)
                x = [item[1] for item in second]
                y = [item[2] for item in second]
                plt.plot(x, y, 'y')
                x = [second[sec_par_counter][1]]
                y = [second[sec_par_counter][2]]
                plt.plot(x, y, color='c')
                plt.title("child")
                plt.show()
            
            sec_par_counter -= 1

        return child
    
    def Elitizam(population, population_fitness, population_size):
        population, population_fitness = PomocneFunkcije.sort(population, population_fitness)
        population = list(population)
        
        half = int(population_size / 2)
        pom_populacija = []
        for i in range(0, half):
            pom_populacija.append(population[0])
            population.pop(0)
        
        br = half
        while br < population_size:
            slucajniIndeks = random.randint(0, len(population) - 1)
            pom_populacija.append(population[slucajniIndeks])
            population.pop(slucajniIndeks)
            br += 1
        population = pom_populacija
    
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