from maze import *
from node import *

#!/usr/bin/env python

# 1. Create a Maze on initialization
maze = Maze("http://epdeveloperchallenge.com")

print "Found a GUID as :", maze.guid()

# 2. Retreive our current location in the Maze which shows us future options and start by marking it unvisited
currentCell = maze.current_location()
starting_node = Node(currentCell, False, 0)

unvisited = []
unvisited.append(starting_node)
solution = ''

#Base Case
if maze.atEnd():
    solution = maze.current_location['note']
    print 'Congratulations, here is the message: ' + solution


def check_unvisited(unvisited_nodes):
    for node in unvisited_nodes:
        maze.jumpTo(node)

        for direction in node.possible_directions():
            currentCell = maze.move(direction)

            if maze.atEnd():
                solution = maze.current_location['note']
                return
            else:
                # Check the current location and see if hav neighbours to check
                # currentCell = maze.current_location()
                poss_node = Node(currentCell, False, 0)
                if poss_node.hasMoves():
                    unvisited_nodes.append(poss_node)

            maze.jumpTo(node)


        unvisited_nodes.remove(node)
        check_unvisited(unvisited_nodes)


check_unvisited(unvisited)


print 'Congratulations, here is the message: ' + solution




