import time

counter = input("Enter Iteration times:")    #set iteration times
tabu_size = input("Enter tabu size:")       #set tabu size
start = time.time()                         #set timer start

p = [0,10,10,13,4,9,4,8,15,7,1,9,3,15,9,11,6,5,14,18,3]  #process
d = [0,50,38,49,12,20,105,73,45,6,64,15,6,92,43,78,21,15,50,150,99]   #due date
w = [0,10,5,1,5,10,1,5,10,5,1,5,10,10,5,1,10,5,5,1,5]       #weight
# T = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]    #Task
T = [12,13,5,16,8,1,2,3,4,6,7,9,10,11,14,15,17,18,19,20]    #high priority first serve Task

#initialize templist
temp = [0 for i in range(len(T))]   
#initialize choicelist, each iteration of best sol
choice = [0 for i in range(int(counter))] 
#initialize tabulist
tabu =[[0  for i in range(2)]  for j in range(int(tabu_size))]
#initialize count as counting tabu list
count = 0

for j in range(int(counter)):
    #1st initial sol, after 1st becomes each iteration best sol
    buf = p[T[0]]
    temp[0] = 0    
    for num in range(len(T)):
        temp[0] = temp[0] + w[T[num]]*max(buf-d[T[num]],0)
        if num == len(T)-1:
            break
        buf = p[T[num+1]] + buf

    # print(temp[0],"best now") #each iteration's best value
    for i in range(1,len(T)):
        T[i-1],T[i] = T[i],T[i-1]   #swap 2 number
        
        #check tabu list every element 
        for num2 in range(int(tabu_size)):
            if (T[i-1] == tabu[num2][0] and T[i] == tabu[num2][1]):
                judge_tabu = 1   #if tabu, set judge =1 which means true, and leave loop
                break
            else:
                judge_tabu = 0   #if not, set judge = 0 which means false 

        #check whether tabu or not
        if judge_tabu == 1:      
            temp[i] = 1000000   #if tabu, set value extremly high, so it cannot be considered as best sol
                
        else:    
            buf = p[T[0]]
            temp[i] = 0    
            for num in range(len(T)):
                temp[i] = temp[i] + w[T[num]]*max(buf-d[T[num]],0)
                if num == len(T)-1:
                    break
                buf = p[T[num+1]] + buf
            
        T[i-1],T[i] = T[i],T[i-1]   #swap 2 number again
    
    # Compare every change(two job ), which is a best solution, and find which two number add to tabu list   
    if j >= 1:
        tcmp = temp[1]
        mark = 0
        for k in range(1,len(T)-1):
            sol = min(tcmp,temp[k+1])
            if sol < tcmp:
                mark = k    #check if sol becomes better
            tcmp = sol
               
    else:
        tcmp = temp[0]
        mark = 0
        for k in range(len(T)-1):
            sol = min(tcmp,temp[k+1])
            if sol < tcmp:
                mark = k    
            tcmp = sol
  
    #add each iteraion's best sol into choiceList
    choice[j] = sol     

    #add T(a,b) to tabu list
    tabu[count][0] = T[mark]    
    tabu[count][1] = T[mark+1]
    
    count = count+1                    #tabu list element plus 1
    if count>int(tabu_size)-1:         #if tabu list full, restart from first one 
        count = 0
        
    T[mark],T[mark+1] = T[mark+1],T[mark]   #change T to currently best sol
    
# Compare iteration's better choice, and choose optimal solution 
cmpmin = choice[0]    
for j in range(int(counter)-1):
    optsol = min(cmpmin,choice[j+1])
    cmpmin = optsol

#print problem answer 
print()
print("Approximate optimal solution:",T)
print("Objective function value:",optsol) 
print("Tabu:",tabu)

#print program execution time
stop = time.time()
print("Runtime:",stop-start,"(s)")
