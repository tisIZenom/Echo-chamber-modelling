========================================== README ====================================================

This is the Readme file for the modelling of echo chambers:


  - There are a lot of definitions and important facts in the code that i have written 
  I hope to have a little more detail on the places where you can refer to in order to better understand the code.
  When I set that up I will make sure to index it here. 


> The environment 

  - Language - Python - version 3.13.5 
  - OS - Arch linux 
  - Libraries used - networkx (please refer to the documentation for more details)
                   - matplotlib
                   - numpy 

  - the code was run in the system terminal with no extra wrappers. 

# Questions to understand  

what are some synchrony parameters that you can measure in the end. 
  - And also see whether if you can measure an echo chamber using this fact 



also ask for an option to include randomness or not. 
try to make an animation for the change in opinions. 

Let us also try to add negative trust weights 

Adding edge weights will also prove interesting. 

also try to analytically prove that we can use just one type of influence kernel

also change the random values to real values as in the values should be a gaussian not a uniform distribution.
- Having a truncated normal function. 
try to have a consensus score for before and after for the function. 

visual tracking over time. of the kuramoto factor 

there is something called greedy modularity communities in networkx look into more details in that part . 

modularity of opinion aligned communities 

Make a grand table to see how the factors affect the convergence


------------------------------------------------------------------------ 

Some important/ interesting insights in this 

- Even with random noise there are no echo chambers that form(sometimes when convergence occurs)


___

# Some fixes in the code

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
5. 



___

numerator = 0
denominator = 0

for i in G.nodes:
    for j in G.neighbors(i):
        weight = G[i][j].get('weight', 1.0)
        numerator += weight * G.nodes[j]['opinion']
        denominator += weight

weighted_estimate = numerator / denominator if denominator > 0 else 0
___

we can also see std deviation using 

consensus_score = np.std([G.nodes[i]['opinion'] for i in G.nodes])

___

you can also have visual tracking of the opinions over time 