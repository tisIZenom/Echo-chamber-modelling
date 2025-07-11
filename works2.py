import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

###############################################################

# The global variables 







# Parameters
n = 100        # number of agents
k = 5          # average number of connections
p = 0.1        # rewiring probability

# Time settings
dt = 0.01
T_max = 100
steps = int(T_max / dt)

# Initialize network
G = nx.watts_strogatz_graph(n, k, p)

# Initialize opinions as node attributes
for node in G:
    G.nodes[node]['opinion'] = np.random.uniform(-1, 1)

# For plotting
pos = nx.spring_layout(G)

# Influence function
def influence_kernel(r, tolerance=1.5):
    if abs(r) < tolerance:
        return np.exp(-2 * abs(r)) * r
    return 0


from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Extract initial opinions
initial_opinions = [G.nodes[i]['opinion'] for i in G.nodes]
norm = Normalize(vmin=-1, vmax=1)
cmap = plt.cm.coolwarm

# Create figure and axes for initial state
fig, ax = plt.subplots(figsize=(8, 6))

# Draw network edges and nodes with initial opinions
nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)
nx.draw_networkx_nodes(
    G, pos, node_color=initial_opinions,
    cmap=cmap, node_size=50, vmin=-1, vmax=1, ax=ax
)

# Add colorbar
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="Opinion")

ax.set_title("Initial Opinions on Network")
ax.axis('off')
plt.tight_layout()
plt.show()








# Simulation
history = []

for step in range(steps):
    current_opinions = np.array([G.nodes[i]['opinion'] for i in G.nodes])
    delta_opinions = np.zeros(n)

    for i in G.nodes:
        delta = 0
        for j in G.neighbors(i):
            r = current_opinions[j] - current_opinions[i]
            delta += influence_kernel(r)
        delta_opinions[i] = delta

    # Euler integration step
    new_opinions = current_opinions + dt * delta_opinions

    # Update opinions
    for i in G.nodes:
        G.nodes[i]['opinion'] = new_opinions[i]

    history.append(new_opinions.copy())

    # Stopping condition: max change < 0.01
    if step * dt >= 100:
        if np.max(np.abs(new_opinions - current_opinions)) < 0.01:
            print(f"Converged at time t = {step * dt:.2f}")
            break

# this is the final visualization part.
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

final_opinions = [G.nodes[i]['opinion'] for i in G.nodes]
norm = Normalize(vmin=-1, vmax=1)
cmap = plt.cm.coolwarm

# Create figure and axes explicitly
fig, ax = plt.subplots(figsize=(8, 6))

# Draw edges on the specified axes
nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)

# Draw nodes on the same axes
nodes = nx.draw_networkx_nodes(
    G, pos, node_color=final_opinions,
    cmap=cmap, node_size=50, vmin=-1, vmax=1, ax=ax
)

# Create a ScalarMappable and attach colorbar to the same axes
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="Opinion")

ax.set_title("Final Opinions on Network")
ax.axis('off')
plt.tight_layout()
plt.show()


################################################################################

# trying to visualize the distribution of opinions before and after. 




initial_opinions = history[0]
final_opinions = history[-1]

plt.figure(figsize=(10, 5))

# Initial distribution
plt.subplot(1, 2, 1)
plt.hist(initial_opinions, bins=20, range=(-1, 1), color='lightcoral', edgecolor='black')
plt.title("Initial Opinion Distribution")
plt.xlabel("Opinion")
plt.ylabel("Number of Agents")
plt.grid(True)

# Final distribution
plt.subplot(1, 2, 2)
plt.hist(final_opinions, bins=20, range=(-1, 1), color='skyblue', edgecolor='black')
plt.title("Final Opinion Distribution")
plt.xlabel("Opinion")
plt.ylabel("Number of Agents")
plt.grid(True)

plt.tight_layout()
plt.show()
