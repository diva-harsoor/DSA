"""
Takes a coordinate and count (representing which number "move" this will be)
Returns a list of all valid moves (valid being on the game board)
"""
def graph_moves(coordinate, count):

    
    
    graph = []
    new_x = coordinate[0] + 1
    if new_x >= 1 and new_x <= 8:
        new_y = coordinate[1] + 2
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])
        new_y = coordinate[1] - 2
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])
    
    new_x = coordinate[0] + 2
    if new_x >= 1 and new_x <= 8:
        new_y = coordinate[1] + 1
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])
        new_y = coordinate[1] - 1
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])

    new_x = coordinate[0] - 1
    if new_x >= 1 and new_x <= 8:
        new_y = coordinate[1] + 2
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])
        new_y = coordinate[1] - 2
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])

    new_x = coordinate[0] - 2
    if new_x >= 1 and new_x <= 8:
        new_y = coordinate[1] + 1
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])
        new_y = coordinate[1] - 1
        if new_y >= 1 and new_y <= 8:
            graph.append([(new_x, new_y), count])

    return graph

"""
Implements breadth-first search of a target coordinate from an initial coordinate,
according to a knight's ability to move (2 blocks on one axis, 1 block on the other)
"""
def search_graph(initial, target):
    count = 0
    visited = set()
    queue = []

    queue.append([initial, count])
    if (initial == target):
        return count
    visited.add(initial)

    while queue != set(): # check that the queue is not empty
        coordinate_and_count = queue.pop(0)
        print(coordinate_and_count)
        if coordinate_and_count[0] == target:
            return coordinate_and_count[1]
        neighbors = graph_moves(coordinate_and_count[0], coordinate_and_count[1] + 1)
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                queue.append(neighbor)
                visited.add(neighbor[0])



"""
Taking input from stdin - assumes integer input
"""
print("Enter x-value of initial coordinate (must be >= 1 and <= 8): ")
x = input()
if (int(x) < 1 or int(x) > 8):
    print("Invalid value. Exiting program.")
    quit();

print("Enter y-value of initial coordinate: (must be >= 1 and <= 8)")
y = input()
if (int(y) < 1 or int(y) > 8):
    print("Invalid value. Exiting program.")
    quit();

initial = (int(x), int(y))

print("Enter x-value of target coordinate (must be >= 1 and <= 8): ")
x = input()
if (int(x) < 1 or int(x) > 8):
    print("Invalid value. Exiting program.")
    quit();

print("Enter y-value of target coordinate: (must be >= 1 and <= 8)")
y = input()
if (int(y) < 1 or int(y) > 8):
    print("Invalid value. Exiting program.")
    quit();

target = (int(x), int(y))


"""
Running program and returning results
"""
result = search_graph(initial, target)
output_string = "The shortest path is " + str(result) + " move(s) long."
print(output_string)