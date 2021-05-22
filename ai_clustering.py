import random

def objective_func(state,marks):
        tot=0
        for i in range(0, len(marks)):
            diff = []
            for j in range(0, len(state)):

                d=abs(state[j]-marks[i])
                diff.append(d)
            p = diff.index(min(diff))
            tot += pow(diff[p], 2)

        return tot

def difference(state,n):
    diff = []
    for j in range(0, len(state)):
            d = abs(state[j] - n)
            diff.append(d)
    p = diff.index(min(diff))

    return p

def swarm_optimization(marks,k):
    particles = 3
    iterations = 0
    generate=0
    expand=0
    position=[]
    for i in range(0,particles):
        iposition=[]
        for j in range(0,k):
            p=marks[random.randrange(0,len(marks))]
            iposition.append(p)
        position.append(iposition)
    print("Intialization: ")
    print("Positions: ")
    print(position)
    velocity=[]
    for i in range(0,particles):
          ivelocity=[]
          for j in range(0,k):
            p=0
            ivelocity.append(p)
          velocity.append(ivelocity)
    print("Velocities: ")
    print(velocity)
    objective=[]
    for i in range(0,len(position)):
        o=objective_func(position[i],marks)
        objective.append(o)

    pbest_pos = position.copy()
    print("Pbest positions: ")
    print(pbest_pos)
    gbest_pos = position[objective.index(min(objective))]
    print("Pbest values: ")
    print(objective)
    print("Gbest position: ")
    print(gbest_pos)
    print("Gbest value: ")
    print(objective[objective.index(min(objective))])
    print()
    c1=2
    c2=2
    generate+=3
    expand+=3
    while iterations<6:
      v_new = []
      p_new=[]
      for i in range(0,particles):
            v=velocity[i].copy()
            p=pbest_pos[i].copy()
            s=position[i].copy()
            g=gbest_pos.copy()

            for j in range(0,len(velocity[i])):
                v[j]=v[j]+ c1*random.randint(0,1)*(p[j]-s[j])+ c2*random.randint(0,1)*(g[j]-s[j])

            v_new.append(v)
            for j in range(0, len(position[i])):
                s[j] = s[j] + v[j]
            p_new.append(s)

      velocity=v_new.copy()
      position=p_new.copy()

      for i in range(0,len(position)):
            if objective_func(pbest_pos[i],marks)>objective_func(position[i],marks):
                pbest_pos[i]=position[i].copy()
                objective[i]=objective_func(pbest_pos[i],marks)
      print("Next Iteration: ")
      print("New position: ")
      print(position)
      print("New velocities: ")
      print(velocity)
      print("Pbest positions: ")
      print(pbest_pos)
      print("Pbest values: ")
      print(objective)
      gbest_pos = pbest_pos[objective.index(min(objective))]
      print("Gbest position: ")
      print(gbest_pos)
      print("Gbest value: ")
      print(objective[objective.index(min(objective))])
      print()
      iterations+=1
      generate+=3
      expand+=3

    group_rep=gbest_pos
    print("Group representatives: ")
    print(group_rep)
    print("Groups:")
    for i in range(0,len(group_rep)):
        group=[]
        for j in range(0,len(marks)):
            index=difference(group_rep,marks[j])
            if index==i:
                group.append(marks[j])
        print(group)
    print("No of nodes generated: ")
    print(generate)
    print("Nof of nodes expanded: ")
    print(expand)

def main():
     n=int(input("Enter number of students: "))
     k=int(input("Enter number of groups: "))
     marks=[]
     print("Enter the marks: ")
     for i in range(0,n):
         m=int(input())
         marks.append(m)

     swarm_optimization(marks,k)
if __name__ == "__main__":
        main()