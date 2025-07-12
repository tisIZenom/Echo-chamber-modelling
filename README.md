
___

This is the Readme file for the echo chambers modelling.
# The environment 

  - Language - Python - version 3.13.5 
  - OS - Arch linux 
  - Libraries used - networkx (please refer to the documentation for more details)
	  - matplotlib
	  - numpy
	  - networkx
	  - pickle

  - the code was run in the system terminal with no extra wrappers. 
  - Please use the latest versions of python and networkx since the code uses some new features that are provided by both. 
  
___

# Some more information on the code. 

### Echo_chambers_sim.py 

- The time taken and the approximation for continous time is done through Euler integration. 
- The opinions that are initialized in the graph initially are uniform on [-1, 1 ]
- The edge weights however are initialized using a gaussian function using both a positive only and a negative edge weights to see if there is a difference in the consensus of the network.
- There are two order parameters that are measured here. 
	- One is the kuramoto parameter which measures the polarization of the group. 
	- The other is just the standard deviation of the opinions. 
- We have only one kernel to measure at the moment and it would be nice to have multiple kernels to see what would happen in each case. 
- There might be a possible echo chamber formation. There is a code that measures the possible echo-chamber formation in the main loop and stops the iteration to visualize the graph. 
- The influence kernel uses a Normal distribution randomness in each step as well. 
- you can also load a saved graph and change the influence kernel and it's randomness. 

___

# Questions to understand  
try to make an animation for the change in opinions. 



try to track what happens if we have the same graph going through different possibilities

visual tracking over time. of the kuramoto factor 

there is something called greedy modularity communities in networkx look into more details in that part . 

modularity of opinion aligned communities 

Try to make a distribution of opinions over time.  break if

Make a grand table to see how the factors affect the convergence


------------------------------------------------------------------------ 

Some important/ interesting insights in this 

- Even with random noise there are no echo chambers that form(sometimes when convergence occurs)


___

# Some FAQs in the code

1. Do all dynamical systems converge? 
	1. Yes nonlinear systems can converge needn't be a chaotic system just because you have a nonlinear system
2. Can you know a priory if your system converges given a type of function? 
	1. Yes there is a lemma that shows that this is always true 
	2. refer to the document for more information. 
	3. Mainly this is true if you have a non-negative influence kernel.
3. Can you find the convergence of the group a priory?
	1. It is dependent upon many factors such as what do you classify the group of functions that allow the network to converge to a certain point.  as Linear averaging models or nonlinear averaging models
	2. Also depends upon the distribution of the initial distribution and the connectivity of the group. 
	3. The bounded nature of the kernel also contributes to this highly. 
4. What are some synchrony factors you can use to measure in the network?
	1. There are many parameters that can be evaluated to check the synchrony of the group.
	2. The ones I am interested in measuring are parameters like kuramoto order parameter, and also the clustering coefficient vs local alignment. 
5. Can these synchrony factors predict the formation of the echo chambers?
	1. Technically directly referring to a parameter that expresses if an echo chamber is possible it does not directly imply it. 



___
