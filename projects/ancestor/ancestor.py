from util import Queue

anc = {}

def earliest_ancestor(ancestors, starting_node):

    q = Queue()
    visited = set()
    path = []

    for a in ancestors:
        if a[1] not in anc:
            anc[a[1]] = [a[0]]
        else:
            anc[a[1]].append(a[0])

    q.enqueue(starting_node)

    while q.size():
        current_node = q.dequeue()

        if current_node not in visited:
            visited.add(current_node)

            if current_node in anc:
                parents = anc[current_node]
                curr = []
                for p in parents:
                    curr.append(p)
                    q.enqueue(p)
                curr.sort(reverse=True)
                path = path + curr

    if len(path) > 1:
        return path[-1]
    else:
        return -1

# def get_parents(node):
#     parents = 

#     return parents


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1)) #should equal 10

