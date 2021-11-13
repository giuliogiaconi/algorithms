import random

def min_cut_graph(adjacency_matrix):
    """Function that computes the minimum cut for a graph represented by the adjacency matrix.

    Args:
        adjacency_matrix (list): adjacency matrix made up of a list of lists. Each list contains a row of the adjacency matrix 

    Returns:
        int: minimum cut for the adjacency matrix
    """

    if len(adjacency_matrix)==2:

        # print('base case')
        
        for i in adjacency_matrix[0][1:]:
            
            assert i == adjacency_matrix[1][0]
           
        for i in adjacency_matrix[1][1:]:
            
            assert i == adjacency_matrix[0][0]
        
        
        assert len(adjacency_matrix[0][1:]) == len(adjacency_matrix[1][1:])
        
        min_cut = len(adjacency_matrix[0][1:])
        # print(min_cut)
        return min_cut

    else:

        # print('recursive step')
        # print(adjacency_matrix)

        # choose two vertices at random
        index_first_vertex = random.randint(0,len(adjacency_matrix)-1) #0
        first_vertex = adjacency_matrix[index_first_vertex][0]
        second_vertex = random.choice(adjacency_matrix[index_first_vertex][1:]) #5
        # print(f"merging vertices {first_vertex} and {second_vertex}")

        # create new "contracted" row
        new_row = []
        new_row.append(first_vertex) #1
        new_row.extend(adjacency_matrix[index_first_vertex][1:])
        for index_second_vertex, row in enumerate(adjacency_matrix):
            if row[0] == second_vertex:
                new_row.extend(row[1:])
                break
        # print('new element', new_row)

        # delete self loops
        new_new_row = [new_row[0]]
        new_new_row.extend([i for i in new_row[1:] if ((i != first_vertex) and (i !=second_vertex))])
        # print('new element without self loops', new_new_row)

        # remove old elements and add new one
        if index_first_vertex < index_second_vertex:
            del adjacency_matrix[index_first_vertex]
            del adjacency_matrix[index_second_vertex-1]
        else: 
            del adjacency_matrix[index_second_vertex]
            del adjacency_matrix[index_first_vertex-1]
        adjacency_matrix.append(new_new_row)

        # rename one of the contracted vertices in adjacency matrix with the other
        for row in adjacency_matrix:
            for index, item in enumerate(row):
                if row[index] == second_vertex:
                    row[index] = first_vertex

        # print('new adjacency matrix', adjacency_matrix)
        min_cut = min_cut_graph(adjacency_matrix) 
        return min_cut


adjacency_matrix = [['1', '2', '3', '4'], ['2', '1', '5', '6'], ['3', '1', '4'], ['4', '3', '1'], ['5', '2', '6'], ['6', '5', '2']]

# compute the minimum cut for a number of times
min_cut = 1000
for i in range(100):
    # print(i)
    adjacency_matrix = [['1', '2', '3', '4'], ['2', '1', '5', '6'], ['3', '1', '4'], ['4', '3', '1'], ['5', '2', '6'], ['6', '5', '2']]

    res = min_cut_graph(adjacency_matrix)
    # print('current min cut:', res)
    min_cut = min(min_cut, res)
    print(min_cut)

print('min_cut: ', min_cut)