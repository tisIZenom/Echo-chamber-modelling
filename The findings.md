
___

This file reports what were the outcomes that came out of running the simulations with different parameters and comes up with hypotheses and conclusions regarding the same. 

___

We will be repeating the experiment for different values of each categories and analyse the simulations after they have been run. 

# The parameters

## The size 

We will have 4 categories of sizes to simulate what happens when we run the simulation. This parameter is represented by the variable n in the code. 

1. size 5 small
2. size 50 medium 
3. size 100 large 
4. size 1000 infinite

## Average connections 

This shows what are the number of connections a node is said to have averaged out throughout all the nodes. We will have networks with 2, 4, 6, 8, and 12 as the categories for this. 

## The Clustering coefficient

This number shows the probability of the two neighbours of a node being connected. 

shows how clustered and close knit a locality is. 

We will have values from 0.1 to 0.2. 

___

## Other parameters 

#### Randomness in the kernel 

- So far the kernel has usually never had an extra term that signifies the external randomness that influences an agent's opinion. 
- However in the code introducing just the randomness in the code does not change the consensus of a group 
	- This is only in the case of a non weighted or a weighted positive graph 
- ![[Pasted image 20250715112805.png]]

Here is an illustrated example of n = 100, p = 5 and k = 0.1
In this scenario we are using a positive weighted graph. 

In case 1 we have a positive weighted graph with randomness in the kernel. 

![[Pasted image 20250715113700.png]]

The group mostly converges except the two dots who are out of the tolerance limit for interacting. 

![[Pasted image 20250715113809.png]]

![[Pasted image 20250715113835.png]]

This is the standard deviation for the same. 

This is the kuramoto order parameter 
![[Pasted image 20250715113914.png]]

As we can see the graph is jagged and not smooth due to the randomness/noise perturbing it. Here are the opinions of the individuals. 

![[Pasted image 20250715114133.png]]





Now let us take a look at the same graph without randomness in the kernel.

The nodes converge nicely producing this distribution at time t = 96.00

![[Pasted image 20250715114745.png]]

This is the standard deviation and the kuromoto order parameter throughout the time. 

![[Pasted image 20250715114835.png]]

The final distribution of the opinions looks as follows. 

![[Pasted image 20250715114941.png]]

As we can observe adding randomness and positive weighted parameters usually gives rise to group consensus. The only way a group can be left out and form a chamber is when they have opinions out of tolerance with their neighbours. 

Let us now look at what happens when we have negative weights. 

![[Pasted image 20250715115611.png]]

This is with no randomness in the kernel. 

![[Pasted image 20250715115708.png]]

![[Pasted image 20250715115730.png]]

as we can see we have increase in std deviation. 

![[Pasted image 20250715115813.png]]

![[Pasted image 20250715115936.png]]

The group stay stagnant at these points at time t = 45.62. 
As we can see we have echo chambers that start forming. 

Let us look at the same graph with randomness included. 

![[Pasted image 20250715120539.png]]

![[Pasted image 20250715120557.png]]

![[Pasted image 20250715120722.png]]


The influence kernel was taken to be :

$$ \huge 
\phi(r) = e^{-6r}
$$
The total velocity function would be :
$$ \huge 
\frac{do_{i}}{dt} = \sum_{j} w_{ij} \phi(r) r + \sigma\beta
$$




Why choose this model over the others? 

They maybe dynamic however they usually produce consensus when time steps became large enough. And most models are not continous in time. 

Can this model also have consensus? yes. 

