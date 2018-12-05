from pulp import*

p = [0,10,10,13,4,9,4,8,15,7,1,9,3,15,9,11,6,5,14,18,3]  #process
d = [0,50,38,49,12,20,105,73,45,6,64,15,6,92,43,78,21,15,50,150,99]    #due date
w = [0,10,5,1,5,10,1,5,10,5,1,5,10,10,5,1,10,5,5,1,5]  #weight

T = [2,1,4,3,5,6,7,8,9,10,11,12,13,16,15,14,17,18,19,20]       #Task 
#initialize templist
temp = [0 for i in range(20)]   
#initialize choicelist, each iteration of best sol
choice = [0 for i in range(200)] 
#initialize tabulist
tabu =[[0  for i in range(2)]  for j in range(2)]
count = 0



for j in range(200):
    #initialize sol
    buf = p[T[0]]
    temp[0] = 0    
    for num in range(20):
        temp[0] = temp[0] + w[T[num]]*max(buf-d[T[num]],0)
        if num == 19:
            break
        buf = p[T[num+1]] + buf

    # temp[0] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)
    print(temp[0],"best now")
    for i in range(1,20):
        T[i-1],T[i] = T[i],T[i-1]   #swap 2 number
        if (T[i-1] == tabu[0][0] and T[i] == tabu[0][1]) or (T[i-1] == tabu[1][0] and T[i] == tabu[1][1]):
            # temp[i] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)
            # print(temp[i],"tabu!")
            temp[i] = 10000000  #if tabu, set value extremly high
            
        else:    
            buf = p[T[0]]
            temp[i] = 0    
            for num in range(20):
                temp[i] = temp[i] + w[T[num]]*max(buf-d[T[num]],0)
                if num == 19:
                    break
                buf = p[T[num+1]] + buf


            # temp[i] = w[T[0]]*max(p[T[0]]-d[T[0]],0) + w[T[1]]*max(p[T[0]]+p[T[1]]-d[T[1]],0) + w[T[2]]*max(p[T[0]]+p[T[1]]+p[T[2]]-d[T[2]],0) + w[T[3]]*max(p[T[0]]+p[T[1]]+p[T[2]]+p[T[3]]-d[T[3]],0)
            
        T[i-1],T[i] = T[i],T[i-1]   #swap 2 number again
    
    
    
    if j >= 1:
        tcmp = temp[1]
        mark = 0
        for k in range(1,19):
            sol = min(tcmp,temp[k+1])
            if sol < tcmp:
                mark = k    #check if sol change
            tcmp = sol
               
    else:
        tcmp = temp[0]
        mark = 0
        for k in range(19):
            sol = min(tcmp,temp[k+1])
            if sol < tcmp:
                mark = k    
            tcmp = sol
   

    
    choice[j] = sol

    tabu[count][0] = T[mark]
    tabu[count][1] = T[mark+1]
    
    # print(tabu)
    count = count+1
    if count>1:
        count = 0
        
    T[mark],T[mark+1] = T[mark+1],T[mark]
    # print(T)
    


