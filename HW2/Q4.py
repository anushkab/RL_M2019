#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
from scipy.optimize import linprog


# In[51]:


#Initialsing the grid parameters:
size=5
A,A_prime=np.array([0,1]),np.array([4,1])
B,B_prime=np.array([0,3]),np.array([2,3])
df=0.9 #The discount Factor
deterministic_policy=[0.25,0.25,0.25,0.25] #Equal for left , up, right and down
Actions=[np.array([1,0]),np.array([0, 1]),np.array([-1, 0]),np.array([0,-1 ])]


# In[60]:


states_count=size*size
def take_step(state, action):
    if (state==A).all():
        return A_prime,10
    elif (state==B).all():
        return B_prime,5
    else:
        next_state = state + action
        if next_state[0]>=size or next_state[0]<0 or next_state[1]>=size or next_state[1]<0:
            return state,-1
        else:
            return next_state, 0
def get_1D_index(state):
    return state[1]+(size*state[0])

matrix_A,matrix_B= np.zeros((states_count*4, states_count)),np.zeros((states_count*4))
for i in range(size):
    for j in range(size):
        n=0
        curr_state=np.array([i,j])
        for a in Actions:
            index_state_1D=4*get_1D_index(curr_state)+n
            next_state,reward=take_step(curr_state,a)
            index_new_state_1D=get_1D_index(next_state)
            matrix_B[index_state_1D]-=reward 
            matrix_A[index_state_1D,index_new_state_1D]+=df
            n+=1
print(matrix_B)
print(matrix_A)
for p in range(states_count* 4):
    matrix_A[p,p//4]-=1 

solution=linprog(np.ones(states_count),A_ub=matrix_A,b_ub=matrix_B)
solution_x=solution['x']
A_into_X=matrix_A * np.round(solution_x,decimals=1)
x = (np.sum(A_into_X, axis=1)+ matrix_B)
x=x.reshape(-1,4)
x_max=np.amax(x,axis=1)

def get_where_arg_max(a,b,c):
    return np.ravel(np.argwhere(a[c]==b[c]))

optimal_policy_map=np.empty(states_count,'object')
for index in range(states_count):
    y=get_where_arg_max(x,x_max,index)
    for each_action in y:
        if optimal_policy_map[index] is not None:
            optimal_policy_map[index].append(each_action)
            continue
        optimal_policy_map[index]=[each_action]
        
optimal_policy_map = optimal_policy_map.reshape((size, size))
optimal_value_map = np.round(np.reshape(solution_x,(size,size)),decimals=1)

print(optimal_value_map)
for i in range(size):
    for j in range(size):
        P=[]
        l=optimal_policy_map[i][j]
        for k in l:
            if k==0:
                P.append("left")
            if k==1:
                P.append("right")
            if k==2:
                P.append("up")
            if k==3:
                P.append("down")
        print(P)
    print()


# In[ ]:





# In[ ]:





# In[ ]:




