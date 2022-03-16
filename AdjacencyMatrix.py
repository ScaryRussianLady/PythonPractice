'''
https://www.geeksforgeeks.org/add-and-remove-edge-in-adjacency-matrix-representation-of-a-graph/

Author: Annija Balode
Algorithm: Adjacency Matrix

Above link used as a reference for adding and removing an edge.
'''

# A class for the Graph.
class Graph(object):
    
    def __init__(self, size):
        # An empty array for the Adjacency Matrix
        self.adjMatrix = []
        # Add 0's to the array until edges are added.
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        # Set size to size given by user.
        self.size = size

    #A function for adding a vertex.
    def add_vertex(self, size):
        # For each position in 'size'..
        for j in range(size):
            # And for each position in the range of the length of the Adjacency Matrix..
            for l in range(len(self.adjMatrix)):
                # append 0 to the Adjacency Matrix.
                self.adjMatrix[l].append(0)
                
        for k in range(size):
            # Avoids the new elements from displaying in the same line and being stored as one sub-array. 
            self.adjMatrix.append([])
            # For the new range of the size of the graph..
            for i in range(self.size + size):
                # Initialise the new elements to 0 until an edge is added.
                self.adjMatrix[-1].append(0)
        
        # Add the number of vertices provided to the old number to update the size of the graph.
        self.size = self.size + size

    # A function for adding an edge.
    def add_edge(self, vertex1, vertex2):
        # Updated the graph: switching 0 to 1 at the appropriate vertices.
        # At points: (vertex1, vertex2) and (vertex2, vertex1).
        self.adjMatrix[vertex1-1][vertex2-1] = 1
        self.adjMatrix[vertex2-1][vertex1-1] = 1

        # If the first and second vertex is the same value.
        if vertex1-1 == vertex2-1:
            # Let the user know that both vertices are the same.
            print("The vertices are the same.")

    # A function for removing an edge.
    def remove_edge(self, vertex1, vertex2):
        # Change the 1 to 0: removing the edge between both vertices.
        self.adjMatrix[vertex1-1][vertex2-1] = 0
        self.adjMatrix[vertex2-1][vertex1-1] = 0
        
        # If there is a value of 0 at the point (vertex1, vertex2) then..
        if self.adjMatrix[vertex1-1][vertex2-1] == 0:
            # Let the user know that there is no edge.
            print("No edge.")

    # A function for printing the matrix.
    def print_matrix(self):
        print("    ", end="")
        
        # Print the number of vertices there are across the top.
        for vertex in range(self.size):
            print(" ",vertex+1, end="")
        print("\n")
        print("    ", end="")
        
        # Prints a line to divide the vertices and the edges.
        for vertex_line in range(self.size):
            print("---",end="")
        print()
        vertex_row = 0
        
        #Prints the number vertex for each row.
        for i in self.adjMatrix:
            vertex_row += 1
            print(vertex_row, end=" | ")
            
            # And for each value in the row of the Adjacency Matrix, print either 0 or 1 (edge or not).
            for j in i:
                print(" ",j,end="")
            print("\n")
     
def main():
    g = Graph(6)

    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(3,4)

    g.print_matrix()
    g.remove_edge(1,2)
    g.print_matrix()
    print("\n")
    g.add_vertex(1)

    g.print_matrix()
   
if __name__ == '__main__':
   main()
