from pulp import*

p = [0,10,10,13,4]  #process
d = [0,4,2,1,12]    #due date
w = [0,14,12,1,12]  #weight

T = [2,1,4,3]       #Task 
#initialize templist
temp = [0 for i in range(20)]   
#initialize choicelist
choice = [1000 for i in range(20)] 
#initialize tabulist
tabu =[[0  for i in range(2)]  for j in range(2)]
count = 0


#initialize sol
# temp[0] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)

for j in range(5):
    #initialize sol
    temp[0] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)
    print(temp[0],"best now")
    for i in range(1,4):
        T[i-1],T[i] = T[i],T[i-1]   #swap 2 number
        if (T[i-1] == tabu[0][0] and T[i] == tabu[0][1]) or (T[i-1] == tabu[1][0] and T[i] == tabu[1][1]):
            #temp[i] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)
            temp[i] = 10000000  #if tabu, set value extremly high
            print(temp[i],"tabu!")
        else:    
            # T[i-1],T[i] = T[i],T[i-1]
            temp[i] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)
            # T[i-1],T[i] = T[i],T[i-1]
            print(temp[i])
        T[i-1],T[i] = T[i],T[i-1]   #swap 2 number again
    
    
    
    if j >= 1:
        tcmp = temp[1]
        mark = 0
        for k in range(1,3):
            sol = min(tcmp,temp[k+1])
            if sol < tcmp:
                mark = k    #check if sol change
            tcmp = sol
            # else:
            #     mark = 0    
    else:
        tcmp = temp[0]
        mark = 0
        for k in range(3):
            sol = min(tcmp,temp[k+1])
            if sol < tcmp:
                mark = k    #check if sol change
            tcmp = sol
    #         temp[0] = sol

    
    choice[j] = sol

    tabu[count][0] = T[mark]
    tabu[count][1] = T[mark+1]
    
    print(tabu)
    count = count+1
    if count>1:
        count = 0
        
    T[mark],T[mark+1] = T[mark+1],T[mark]
    print(T)
    

# print (choice)
