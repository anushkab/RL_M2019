#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
from scipy.optimize import linprog


# In[33]:


#Initialsing the grid parameters:
size=4
threshold=4e-6
df=0.9 #The discount Factor
deterministic_policy=[0.25,0.25,0.25,0.25] #Equal for left , up, right and down
Actions=[np.array([1,0]),np.array([0, 1]),np.array([-1, 0]),np.array([0,-1 ])]


# In[34]:


def take_step(state, action):
    if (state[0]==0 and state[1]==0 )or(state[1]==4 and state[1]==4):
        return state,0
    else:
        next_state = state + action
        if next_state[0]>=size or next_state[0]<0 or next_state[1]>=size or next_state[1]<0:
            return state,-1
        else:
            return next_state, 0
value_map=np.zeros((size,size))
while True:
    delta=0
    for i in range(size):
        for j in range(size):
            awards={}
            curr_state=np.array([i,j])
            old_val_map=value_map.copy()
            n=0
            for a in Actions:
                next_state,reward=take_step(curr_state,a)
                var=reward + (df* value_map[next_state[0],next_state[1]])
                awards[n]=np.round(var,decimals=2)
                n+=1
            max_award=max(awards.values())
            diff=np.abs(old_val_map[i,j]-max_award)
            delta=max(delta,diff)
            value_map[i,j]=max_award
    if delta<threshold:
        break

optimal_policy_map = np.empty((size,size), object)
for i in range(size):
    for j in range(size):
        awards={}
        curr_state=np.array([i,j])
        n=0
        for a in Actions:
            next_state,reward=take_step(curr_state,a)
            var=reward + (df* value_map[next_state[0],next_state[1]])
            awards[n]=np.round(var,decimals=2)
            n+=1
        max_award = np.max(list(awards.values()))
        optimal_actions = []
        m=0
        for l in awards:
            if l==max_award:
                optimal_actions.append(m)
                m+=1
        optimal_policy_map[i, j]=optimal_actions


# In[9]:


print(value_map)


# In[ ]:





# In[41]:





# In[42]:


print(optimal_policy_map)
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




