import random
import itertools

def crossover(parents):

     child1 = parents[0]
     child2 = parents[1]
     child1_list = list(child1)
     child2_list = list(child2)

     if(random.random()<cross_prob):
         crossover_point=random.randrange(0,3)
         for i in range(crossover_point,3):
            temp=child1_list[i]
            child1_list[i]=child2_list[i]
            child2_list[i]=temp

     child1=''.join(child1_list)
     child2=''.join(child2_list)

     return child1,child2

def mutation(children):
    child1 = children[0]
    child2 = children[1]
    child1_list = list(child1)
    child2_list = list(child2)
    if (random.random() < mut_prob):

        for i in range(0,3):
            if random.randint(0,1)==1:
               if child1_list[i]=='0':
                    child1_list[i]='1'

               else:
                    child1_list[i]='0'

               if child2_list[i] =='0':
                   child2_list[i] = '1'

               else:
                   child2_list[i] ='0'

    child1 =''.join(child1_list)
    child2 =''.join(child2_list)

    return child1,child2


def tournament_selection(population,r):

     select=[]
     for i in range(0,r):
         select.append(population[random.randrange(0,len(population))])
     f1= fitness_value(select)
     j=f1.index(max(f1))
     parent1=select[j]
     select = []
     for i in range(0, r):
         select.append(population[random.randrange(0, len(population))])
     f2 = fitness_value(select)
     j = f2.index(max(f2))
     parent2 = select[j]

     return parent1,parent2

def fitness_value(population):
     fitness=[]
     for i in range(0,len(population)):
        t=2*pow(int((population[i]),2),2)+1
        fitness.append(t)

     return fitness


def generate_population(k):
    population=[]
    for i in range(0,k):
        population.append("{:03b}".format(random.randint(0,6)))

    return population

def main():
    global generate
    global expand
    generate = 0
    expand = 0
    max=0
    k = int(input("Enter population:"))
    global cross_prob
    r = int(input("Enter k for tournament selection: "))
    cross_prob = float(input("Enter crossover probability: "))
    global mut_prob
    mut_prob = float(input("Enter mutation probability: "))
    gen = []
    s = generate_population(k)
    generate+=k
    print("Initial generation: ")
    print(s)
    j=0
    sol=0
    while generate<500:
        max=0
        flag=0
        gen=s.copy()
        f = fitness_value(gen)
        for i in range(0,len(f)):
            if max<f[i] and int((gen[i]),2)<=6:
                max=f[i]
                j=i
        sol= int((gen[j]),2)
        gen=[]
        for i in range(0, int(k / 2)):
            t = tournament_selection(s,r)
            expand+=2
            c = crossover(t)
            m = mutation(c)
            gen.append(m)

        s = list(itertools.chain(*gen))
        generate+=k
        print("Next generation: ")
        print(s)

    print("Solution- x is :")
    print(sol)
    print("No of nodes generated:")
    print(generate)
    print("No of nodes expanded:")
    print(expand)

if __name__ == "__main__":
    main()