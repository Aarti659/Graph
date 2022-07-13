
def add_vertex(V):
  global graph
  global vertices_no
  if V in graph:
    print("Vertex ", V, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[V] = []


def add_edge(v1, v2, E):
  global graph

  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")

  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    temp = [v2, E]
    graph[v1].append(temp)


def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


graph = {}

vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()

print ("Internal representation: ", graph)


