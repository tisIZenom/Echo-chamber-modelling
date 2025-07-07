

# Here is some anitmation for the 06/07/2025 13:46 defaunt - weishbauch model 


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Build the WS network
n, k, p = 100, 6, 0.1
G = nx.watts_strogatz_graph(n, k, p)
# initialize opinions uniformly in [-1,1]
for i in G:
    G.nodes[i]['opinion'] = np.random.uniform(-1, 1)

pos = nx.spring_layout(G, seed=42) # thank you ces and hitchhikers book 
fig, ax = plt.subplots(figsize=(6,6))

# 2. Deffuant parameters
mu = 0.7          # convergence parameter (how much they adjust)
eps = 1.5        # confidence bound: only interact if |o_i - o_j| < eps
steps = 2000       # number of update steps

# 3. Draw initial frame
nodes = nx.draw_networkx_nodes(
    G, pos,
    node_color=[G.nodes[i]['opinion'] for i in G],
    cmap=plt.cm.coolwarm,
    vmin=-1, vmax=1,
    node_size=50,
    ax=ax
)
edges = nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)
cbar = plt.colorbar(nodes, ax=ax)
cbar.set_label("Opinion")
ax.set_title("Opinion Dynamics (t = 0)")
ax.axis("off")

# 4. Update function for animation
def update(frame):
    # pick a random edge (i,j)
    i, j = np.random.choice(n, 2, replace=False)
    if G.has_edge(i, j):
        oi, oj = G.nodes[i]['opinion'], G.nodes[j]['opinion']
        if abs(oi - oj) < eps:
            # both shift halfway (mu=0.5) toward each other
            G.nodes[i]['opinion'] += mu * (oj - oi)
            G.nodes[j]['opinion'] += mu * (oi - oj)
    # redraw node colors
    colors = [G.nodes[i]['opinion'] for i in G]
    nodes.set_array(np.array(colors))
    ax.set_title(f"Opinion Dynamics (t = {frame+1})")
    return nodes,

# 5. Create animation
anim = FuncAnimation(
    fig, update,
    frames=steps,
    interval=100,     # ms between frames
    blit=True
)


plt.show()



from matplotlib.animation import FuncAnimation, FFMpegWriter


# Save to mp4
writer = FFMpegWriter(fps=10, metadata=dict(artist='Ani'), bitrate=1800)
anim.save("opinion_dynamics.mp4", writer=writer)

