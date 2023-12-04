import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read data from CSV into a pandas DataFrame
data = pd.read_csv('players.csv')

# Create an empty graph
G = nx.Graph()

# Iterate through each row in the DataFrame and add nodes and edges to the graph
for index, row in data.iterrows():
    player = row['Player']
    opponent = row['Opponent']
    games = row['Games']
    
    G.add_node(player)
    G.add_node(opponent)
    G.add_edge(player, opponent, games=games, weight=games)

# Draw the graph
pos = nx.spring_layout(G)


# Example: Setting edge width based on weight attribute
#edge_widths = [float(d) * 0.1 for _, _, d in G.edges(data=True)]
# Add edge labels (win rates) to the graph
pos = nx.spring_layout(G, k=1, iterations=50)
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, pos, with_labels=True, node_size=500, font_weight='bold')
plt.title('Win Rates between Players and Opponents')
plt.show()
