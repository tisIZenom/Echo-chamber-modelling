# networkx creates network that helps in visualization
# matplotlib just for viewing purposes. 

import networkx as nx
import matplotlib.pyplot as plt
import random 
import time 


# These are the parameters that control how the network forms (refer to documentation)

n = 30     # shows the number of agents in the network 
k = 4      # Each node, how many neighbours does it connect to 
p = 0.2    # the randomness and rewiring that occurs in the network


# generating a network (in out case it is a small world network - watts-strogatz style)

Good = nx.watts_strogatz_graph(n, k, p)


# trying to visualize the network

nx.draw(Good, with_labels=True, node_color= 'blue', node_size = 420)
plt.title("Your watts-strogatz small world network")

plt.show()


# We shall have two opinions 
# 1 for closeminded and likes windows 
# 0 for openminded and likes linux 

for node in Good.nodes():
    Good.nodes[node]['Opinion'] = random.choice([0,1])

# let us have a simple update sysmtem for the opinions 
#Defining a function would be better 


"""



def update_opinion(Good, conformity_strenght=0.5):
    new_opinion = {}
    neighbor_opinion = [Good.nodes[neighbor]['opinion'] for neighbor in Good.neighbors(node)]
    if neighbor_opinion:
        majority = round(sum(neighbor_opinion) / len(neighbor_opinion))
        # the agent likes the new opinion now due to bias 
        new_opinion[node] = (
            majority if random.random() < conformity_strenght else opinion 
        )
    for node, opinion in new_opinion.items():
        Good.nodes[node]['opinion'] = opinion

#####################################################################


import time

for t in range(10):  # 10 rounds of updates
    update_opinion(Good)
    opinion = [Good.nodes[n]['opinion'] for n in Goof.nodes()]
    print(f"Round {t+1}: {sum(opinion)} accept, {len(opinion) - sum(opinion)} reject")
    time.sleep(0.5)

"""



import networkx as nx
import matplotlib.pyplot as plt
import random

# --- Step 1: Create the Network ---
n = 30      # number of agents
k = 4       # each node connected to k nearest neighbors
p = 0.1     # rewiring probability for small-world network

G = nx.watts_strogatz_graph(n, k, p)

# --- Step 2: Initialize Beliefs ---
# 0 = rejects theory, 1 = accepts theory
for node in G.nodes():
    G.nodes[node]['belief'] = random.choice([0, 1])
    G.nodes[node]['confidence'] = 1  # number of evidential updates (for Bayesian-style weight)

# --- Step 3: Define Belief Update Rule ---
def update_beliefs(G, conformity_strength=0.5, evidence_weight=0.4):
    new_beliefs = {}
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if not neighbors:
            continue

        neighbor_beliefs = [G.nodes[n]['belief'] for n in neighbors]
        majority_belief = round(sum(neighbor_beliefs) / len(neighbor_beliefs))

        current_belief = G.nodes[node]['belief']
        confidence = G.nodes[node]['confidence']

        # Evidence update (e.g., new data supports truth = 1 with probability 0.6)
        evidence = 1 if random.random() < 0.6 else 0

        # Bayesian-style belief shift based on new evidence
        if evidence != current_belief:
            confidence -= 1
        else:
            confidence += 1

        # Compute final belief based on both evidence and conformity
        if random.random() < conformity_strength:
            final_belief = majority_belief
        else:
            final_belief = evidence

        new_beliefs[node] = (final_belief, max(1, confidence))

    for node, (b, c) in new_beliefs.items():
        G.nodes[node]['belief'] = b
        G.nodes[node]['confidence'] = c

# --- Step 4: Run Simulation ---
def run_simulation(G, rounds=20):
    history = []
    for t in range(rounds):
        update_beliefs(G)
        beliefs = [G.nodes[n]['belief'] for n in G.nodes()]
        history.append(sum(beliefs) / len(beliefs))
        print(f"Round {t+1}: {sum(beliefs)} accept, {len(beliefs) - sum(beliefs)} reject")
    return history

# --- Step 5: Visualize Consensus Trend ---
history = run_simulation(G)

plt.plot(history, marker='o')
plt.title("Proportion of Agents Accepting Theory Over Time")
plt.xlabel("Round")
plt.ylabel("Proportion Accepting")
plt.ylim(0, 1)
plt.grid(True)
plt.show()









