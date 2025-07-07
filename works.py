''' This is the model two of the networks program that we are going to write.
    The networks that are simulated here are purely based on theoretical work and 
    currently do not try to model/simulate real data. 


    The idea is as follows 
        - Initialize a random small world network using the watts-strogatz network (most accurate depiction of the real world networks)
        - Generate a random distibution of opinions (1 dimensional)
        - Import the interaction kernel that is time dependent and run the simulation for an ample amount of time. 
        - Generate graphical view of the changes in opinions over time and terminate when the opinions do not have a change greater than 0.01 in time t = 10 units.

'''

############################################################################################################

# Part 0.5 importing the required libraries 

import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np

###########################################################################################################


# Part 1 Initializing the graph 

# we are using parameters that best suit real world networks so that our model somewhat mimics the real network properties.

# Parameters 

n = 100        # shows the number of agents in the model 
k = 5          # shows the average number of connections per node 
p = 0.1        # shows the rewiring possibility associated with the connections of a node 

network1 = nx.watts_strogatz_graph(n, k, p)

# Checking if the graph has been initialized (This part can be commented out later)

nx.draw(network1, node_size = 42, with_labels = True)

plt.title("The network (watts_strogatz_graph)")

plt.show()


############################################################################################################

# Part 2 Initializing the opinions of the nodes/agents

# I have decided to set the opinions of the nodes as a node attribute 
for node in network1:
    network1.nodes[node]['opinion'] = np.random.uniform(-1,1)

# to simulate different types of soceities change the random uniform to something else here 
# Let us also make the graph easy to visualize 



############################################################################################################ 

# now comes the hard part. Defining an influence kernel and sticking to it 
# I am thinking of having two types one deterministic and one with a random variable 
# there is also another problem of having a continous time 


# Part 3 defining the function. 

def velocity_opinion(network1,opinions,):
    velocity{}
    for i in network1.nodes:
        delta = 0 
        tolerence = 1.5
        for j in network1.neighbors(i):
            w_ij = 1 # the edge weight and the function
            r = (opinions[i] - opinions[j])
            if r < tolerence:
                delta += e^(float(-6))(r )
        velocity[i]
    return velocity 





print("hello world")
