import numpy as np

actions = np.array(list(range(-5,6)))

max_requests = 10

def poisson_val(n, lambd):
    return np.exp(-lambd) * np.power(lambd,n) / np.math.factorial(n)

def exp_return(state, action, state_value):
    returns = 0.0
    
    #employee moves car from 1st location to second
    if action > 0:
        action -= 1
        
    #base return for moving car
    returns -= 2 * abs(action)

    for request_first_loc in range(0, max_requests + 1):
        for request_second_loc in range(0, max_requests + 1):
          
            num_first = int(min(state[0] - action, 20))
            num_sec = int(min(state[1] + action, 20))

            real_first = min(num_first, request_first_loc)
            real_second = min(num_sec, request_second_loc)

            reward = (real_first + real_second) * 10
            
            num_first -= real_first
            num_sec -= real_second

            prob_first = poisson_val(request_first_loc, 3) 
            prob_second = poisson_val(request_second_loc, 4)
            prob = prob_first * prob_second
            
            returned_first = 3
            returned_second = 2
            num_first = min(num_first + returned_first, 20)
            num_sec = min(num_sec + returned_second, 20)
            
            #extra constraint: more than 10 will need extra parking
            above_10 = 0
            if num_first > 10:
                above_10 += num_first - 10
            if num_sec > 10:
                above_10 += num_sec - 10
            reward -= above_10*4
            
            returns += prob * (reward + 0.9 * state_value[num_first, num_sec])
            
    return returns


def policy_eval(value,policy):
    new_value = np.copy(value)
    for i in range(20 + 1):
        for j in range(20 + 1):
            new_value[i, j] = exp_return([i, j], policy[i, j], new_value)
    value_change = np.abs((new_value - value)).sum()
    value = new_value
    return policy, value_change, new_value

def policy_improvement(policy,value, actions):
    new_policy = np.copy(policy)
    for i in range(20 + 1):
        for j in range(20 + 1):
            action_returns = []
            for a in actions:
                if (a >= 0 and i >= a):
                    action_returns.append(exp_return([i, j], a, value))
                elif (a < 0 and j >= abs(a)):
                	action_returns.append(exp_return([i, j], a, value))
                else:
                    action_returns.append(-10000000000.0)
            new_policy[i, j] = actions[np.argmax(action_returns)]

    policy_change = (new_policy != policy).sum()
    policy = new_policy
    return policy , policy_change


value = np.zeros((20 + 1, 20 + 1))
policy = np.zeros((20 + 1, 20 + 1))

#large change to start 
policy_change = 100
value_change = 100
while True:
    # policy evaluation
    while True:
    	#print("entered")
    	policy, value_change, value = policy_eval(value, policy)
    	if value_change < 0.0001:
        	break
    print(policy)
    # policy improvement
    policy, policy_change = policy_improvement(policy,value, actions)
    if policy_change == 0:
        print("Optimal policy", policy)
        break

print(policy)