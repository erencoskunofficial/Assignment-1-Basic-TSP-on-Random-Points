import networkx as nx
import random
import math
import matplotlib.pyplot as plt



SEED = 22
N_POINTS = 20
COLOR_START = '#43A047'
COLOR_END = '#E53935'
COLOR_NODE = '#B0BEC5'
COLOR_ARROW = '#1A237E'



def generate_random_points(n_points, seed=42, xy_range=(0, 100)):
    """Generate n random (x, y) coordinates within the given range."""

    random.seed(seed)
    
    points = {}
    

    for i in range(n_points):
  
        x = random.uniform(xy_range[0], xy_range[1])

        y = random.uniform(xy_range[0], xy_range[1])
 
        points[i] = (x, y)
 
    return points


def build_graph(points):
    """Create a fully connected weighted graph from point coordinates."""
    G = nx.Graph()
    for i, pos in points.items():
        G.add_node(i, pos=pos)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = math.hypot(x1 - x2, y1 - y2)
            G.add_edge(i, j, weight=dist)
    return G



def nearest_neighbor_tsp(G, start=0):
    """Solve TSP approximately using the Nearest Neighbor heuristic."""
    # Başlangıç noktasını ziyaret edilenler listesine ekledim.
    visited = [start]

    total_distance = 0
 
    current = start


    while len(visited) < len(G.nodes):
        # Ziyaret edilmemiş noktaları ve mesafelerini buldum.
        unvisited = {}
        for n in G.nodes:
            if n not in visited:
                # Mevcut noktadan n numaralı noktaya olan mesafeyi aldım.
                distance = G[current][n]['weight']
                unvisited[n] = distance
        
        # En yakın noktayı buldum.
        next_node = None
        min_distance = float('inf')  # Sonsuz büyük sayı
        
        for node, distance in unvisited.items():
            if distance < min_distance:
                min_distance = distance
                next_node = node
        
        # Mesafeyi toplam mesafeye ekledim.
        total_distance += min_distance
        # Bir sonraki noktayı ziyaret edilenler listesine ekledim.
        visited.append(next_node)
        # Şu anki konumu güncelledim.
        current = next_node

    # Son noktadan başlangıç noktasına dönüş mesafesini ekledim.
    return_distance = G[current][start]['weight']
    total_distance += return_distance
    # Başlangıç noktasını tekrar ziyaret edilenler listesine ekledim.
    visited.append(start)
    
    # Sonuçları döndürdüm.
    return visited, total_distance


def plot_tour(G, tour, filename="tsp_result_final_v2.png"):
    """Plot the TSP route with numbered nodes and directional arrows."""
    pos = nx.get_node_attributes(G, 'pos')
    start, end = tour[0], tour[-1]

    # Node colors
    colors = [COLOR_START if n == start else COLOR_END if n == end else COLOR_NODE for n in G.nodes]

    plt.figure(figsize=(9, 7))
    plt.style.use('seaborn-v0_8-white')

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=280, node_color=colors, edgecolors='black')

    # Draw directional arrows
    edges = [(tour[i], tour[i + 1]) for i in range(len(tour) - 1)]
    for src, dst in edges:
        x1, y1 = pos[src]
        x2, y2 = pos[dst]
        dx, dy = (x2 - x1), (y2 - y1)
        plt.arrow(x1, y1, 0.9 * dx, 0.9 * dy,
                  length_includes_head=True,
                  head_width=2.0, head_length=3.0,
                  fc=COLOR_ARROW, ec=COLOR_ARROW,
                  lw=2.5, alpha=0.9)

    # Draw labels
    for idx, node in enumerate(tour[:-1]):
        x, y = pos[node]
        plt.text(x, y + 1.8, str(idx + 1),
                 fontsize=9, color='black', weight='bold',
                 ha='center', va='center',
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

    plt.title("Nearest Neighbor TSP Route", fontsize=13, pad=15)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


# ==========================================================
# MAIN
# ==========================================================
def main():
    points = generate_random_points(N_POINTS, seed=SEED)
    G = build_graph(points)
    tour, total_dist = nearest_neighbor_tsp(G)

    print(f"Toplam Mesafe: {total_dist:.2f}")
    print("Tur Sırası:", tour)
    plot_tour(G, tour)


if __name__ == "__main__":
    main()
