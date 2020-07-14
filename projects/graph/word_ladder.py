from util import Queue

class Graph:
    pass

def word_ladders(start_word, end_word):
    q = Queue()

    visited = set()

    q.enqueue([start_word])

    while q.size() > 0:

        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)

            nbs = get_neighbors(current_word)

            for n in nbs:
                new_path = current_path + [n]
                q.enqueue(new_path)