#!/usr/bin/env python
# coding: utf-8

# In[133]:


import numpy as np


# In[134]:


#Initialsing the grid parameters:
size=5
df=1 #The discount Factor
deterministic_policy=[0.25,0.25,0.25,0.25] #Equal for left , up, right and down
Actions=[np.array([0, -1]),np.array([0, 1]),np.array([1, 0]),np.array([-1,0 ])]


# In[137]:


val_map=np.zeros((self.size,self.size))
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

matrix_A,matrix_B=np.identity(states_count),np.zeros((states_count))
for i in range(size):
    for j in range(size):
        curr_state=np.array([i,j])
        index_state_1D=get_1D_index(curr_state)
        for a in Actions:
            next_state,reward=take_step(curr_state,a)
            index_new_state_1D=get_1D_index(next_state)
            matrix_B[index_state_1D]+=0.25*reward # since policy is 0.25 for all actions
            matrix_A[index_state_1D,index_new_state_1D]-=0.25*df
X=np.linalg.solve(matrix_A, matrix_B)
value_map=np.round(X.reshape((size,size)),decimals=1)


# In[138]:


print(value_map)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




