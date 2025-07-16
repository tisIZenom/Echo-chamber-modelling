
___

We started off with a model that could be continous in time, consider multiple factors and have both deterministic and random contributors to the velocity. We have accomplished in converting this idea into code in python. 

There were many things that one could vary to model real world data and hopefully predict if there would be changes. 

- The function that was used was an exponential decay function which includes a bounded confidence. 
- The randomness was calculated through a truncated gaussian distribution and a uniform distribution. 
- The factors that can be varied in the code are as follows. 
	1. size of the network
	2. average connection 
	3. rewiring probability 
	4. edge weights
		1. negative edge weights 
		2. positive edge weights 
		3. no edge weights (ie, 1)
	5. randomness/ non-deterministic part in the kernel

These factors greatly change the outcome of the experiment and determine whether we will have a stable convergence/steady state. 

The formation of an echo chamber can either occur as a dynamic state for an appreciable amount of time and then disappear or form as a stable state of the system. 

We know that the ones that do form as a stable state happen due to two reasons. 

1. The topology of the system 
2. The way the velocity is defined

Using the topology of the system we can predict whether the system will have echo chambers forming as a stable state. 

It is a necessary condition to have convergence that the system be well connected and connected in a manner that favours individuals being equally connected. 

Measure called modularity depicts how well the network is divided into communities and this is solely based upon the topology of the network. The higher this is the more likely that the network has echo chambers that form. 

Based on the way velocity is defined these temporary communities may form due to the bounded confidence and thus increasing the modularity of the network. 

How does the non-deterministic addition to the kernel affect the convergence of the network?

Having randomness with mean at zero does not change the convergence of the network. (In the case of weighted positive and non weighted graphs.)

Show the findings and run the code in the terminal. 

In the mean time any questions so far? 



Finally the most amount of echo chambers are formed when you establish negative weights in the network and have bounded confidence as well - need to do more work in this aspect. 

