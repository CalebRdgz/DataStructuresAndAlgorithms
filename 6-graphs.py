#Vertex(Node), Between verticies, we have an Edge(connection)
#With graphs, can have weighted edges - some Edges have more
#weight than other edges(connections)
#ex.) Facebook connection between you and a friend
#you are firends with your friend, your friend is friends with you
#You follow a celebrity, they dont follow you back
#DIRECTIONAL or BI-DIRECTIONAL

#Adjacency Matrix
#Y-Axis: Actual Vertex
#X-Axis: Vertecies that may/not have an edge with those Actual Vertex
#Vertecies that have an edge with other vertecies are marked with "1"
#Vertecies that are not connected are "0"
#Graph is mirrored from a 45 degree angle with directional edges
#Graph is different when using bi-directional edges

#Adjacency List
#"A" Vertex has edges(connections) with "B" and "E":
# {
#     'A': ['B','E'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E'],
#     'E': ['A', 'D'],
# }

#Graph Big O
#Adding a Vertex(No edges) to Adjacency List:
# {
#     'A': ['B','E'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E'],
#     'E': ['A', 'D'],
#     'F': [],
# }
#Add an edge between B and F (O(1)):
# {
#     'A': ['B','E'],
#     'B': ['A', 'C','F'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E'],
#     'E': ['A', 'D'],
#     'F': ['B'],
# }
#Remove an edge between B and F (O(1)):
#Go to B, look for all edges in B, and remove F
#Go to F, look for all edges in F, and remove B
#O(1) in Adjacency Matrix, O(|E|) in Adjacency List
#Need to touch everything in the dictionary (adjacency list) to remove a Vertex
# {
#     'A': ['B','E'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E'],
#     'E': ['A', 'D'],
#     'F': [],
# }
#Adjacency Matrix - Storing 1s and 0s for edges, incredibly inefficient with larger data points
#Adjacency Lists better for larger data like social media apps

class Graph:
    def __init__(self):
        #This creates an empty dictionary:
        #{
        #
        # }
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    #Add Vertex (No edge for now)
    #Looks like this:
    # {
    #     'A': []
    # }
    def add_vertex(self, vertex):
        #Check for duplicates in the adjacency list:
        if vertex not in self.adj_list.keys():
            #If no duplicates, add the vertex to the empty list:
            #{
                # 'A': []
            # }
            self.adj_list[vertex] = []
            return True
        #If duplicate in the adjacency list, return False
        return False
    
    #Add Edge between Verticies
    #Looks like this:
    # {
    #     1: [2]
    #     2: [1]
    # }
    def add_edge(self, v1, v2):
        #If vertex1 and vertex2 both exist, we can create an edge between them:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            #{
                # 1: [2],
                # 2: [1]
            #}
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    #Remove Edge between Verticies
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try: #try these lines of code in case of an Error:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass #pass = ignore this error and move on to the next line, (return True)
            return True
        return False
    
    #Remove a Vertex from the Adjacency List:
    #Loop through the list, looking for edges to remove between Verticies and remove the Node
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            #other vertex is the main Node(Vertex) we are currently in in the loop
            for other_vertex in self.adj_list[vertex]:
                #remove the vertex that is found in that other_vertex when we loop to it
                self.adj_list[other_vertex].remove(vertex)
            #remove the Vertex itself entirely from the adjacency list:
            del self.adj_list[vertex]
            return True
        return False

#Add Vertex
# my_graph = Graph()

# my_graph.add_vertex('A')
# my_graph.print_graph()

#Add Edge
# my_graph = Graph()

# my_graph.add_vertex(1)
# my_graph.add_vertex(2)
# print("BEFORE ADDING EDGE:")
# my_graph.print_graph()

# my_graph.add_edge(1, 2)
# print("AFTER ADDING EDGE:")
# my_graph.print_graph()

#Remove Edge between Verticies:
# my_graph = Graph()

# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')

# my_graph.add_edge('A', 'B')
# my_graph.add_edge('B', 'C')
# my_graph.add_edge('C', 'A')
# print("BEGORE REMOVING A AND B EDGE:")
# my_graph.print_graph()

# my_graph.remove_edge('A', 'B')
# my_graph.remove_edge('A', 'D') #D is not connected(no edge) to A (ValueError)
# print("AFTER:")
# my_graph.print_graph()

#Remove Vertex from adjacency list:
my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')
print("BEGORE REMOVING D VERTEX:")
my_graph.print_graph()

my_graph.remove_vertex('D')
print("AFTER:")
my_graph.print_graph()