import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import time

# Cidades e distâncias (como no seu código)
cidades = ['Volta Redonda', 'Barra Mansa', 'Pinheiral', 'Quatis', 'Piraí', 'Valença']
distancias = {
    ('Volta Redonda', 'Barra Mansa'): 12.7,
    ('Volta Redonda', 'Pinheiral'): 13.3,
    ('Volta Redonda', 'Quatis'): 42.2,
    ('Volta Redonda', 'Piraí'): 34.1,
    ('Volta Redonda', 'Valença'): 64.1,
    ('Barra Mansa', 'Pinheiral'): 32.5,
    ('Barra Mansa', 'Quatis'): 26.5,
    ('Barra Mansa', 'Piraí'): 39.7,
    ('Barra Mansa', 'Valença'): 75,
    ('Pinheiral', 'Quatis'): 54.4,
    ('Pinheiral', 'Piraí'): 26.5,
    ('Pinheiral', 'Valença'): 59.4,
    ('Quatis', 'Piraí'): 54.4,
    ('Quatis', 'Valença'): 105,
    ('Piraí', 'Valença'): 60.8
}

# Criar grafo
G = nx.Graph()
for cidade in cidades:
    G.add_node(cidade)
for (cidade1, cidade2), dist in distancias.items():
    G.add_edge(cidade1, cidade2, weight=dist)

# Função para calcular distância total de um caminho
def caminho_distancia(caminho, G):
    distancia = 0
    for i in range(len(caminho)-1):
        distancia += G[caminho[i]][caminho[i+1]]['weight']
    # Retornar ao ponto de partida
    distancia += G[caminho[-1]][caminho[0]]['weight']
    return distancia

# Calcular todas as permutações (menos a cidade de partida fixa)
start_time = time.time()
cidade_inicial = 'Volta Redonda'
outras_cidades = [c for c in cidades if c != cidade_inicial]

menor_distancia = float('inf')
melhor_caminho = None

for perm in permutations(outras_cidades):
    caminho = [cidade_inicial] + list(perm)
    dist = caminho_distancia(caminho, G)
    if dist < menor_distancia:
        menor_distancia = dist
        melhor_caminho = caminho
end_time = time.time()

# Exibir resultados
print("Melhor caminho (ciclo Hamiltoniano):", melhor_caminho + [cidade_inicial])
print("Menor distância total (km):", menor_distancia)
print("Tempo de cálculo (s):", end_time - start_time)

# Mostrar grafo com melhor caminho destacado
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
nx.draw_networkx_nodes(G, pos, nodelist=[cidade_inicial], node_color='red', node_size=900)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.4)  # todas as arestas

# Destacar melhor caminho
caminho_arestas = [(melhor_caminho[i], melhor_caminho[i+1]) for i in range(len(melhor_caminho)-1)]
caminho_arestas.append((melhor_caminho[-1], melhor_caminho[0]))  # retorno ao início
nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, width=3, edge_color='green')

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title(f"Melhor ciclo Hamiltoniano - Distância: {menor_distancia:.1f} km", fontsize=12)
plt.axis('off')
plt.show()
