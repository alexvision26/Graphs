from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def traverse_rooms(graph, starting_node):
    s = Stack()

    s.push(starting_node)

    travel_path = []

    visited = set()

    while len(visited) < len(graph):
        next_move = Stack()
        current = s.stack[-1]
        visited.add(current)

        poss_dir = graph[current][1]
        # print(poss_dir)

        for direction, next_room in poss_dir.items():
            # print(direction, next_room)
            if next_room not in visited:
                next_move.push(next_room)

        if next_move.size() > 0:
            room = next_move.stack[0]
            s.push(room)
        else:
            room = s.stack[-2]
            s.pop()

        for direction, next_room in poss_dir.items():
            if next_room == room:
                travel_path.append(direction)

    # print(travel_path)
    return travel_path

traversal_path = traversal_path + traverse_rooms(room_graph, 0)

print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
