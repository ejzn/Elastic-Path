
class Node(object):

    def __init__(self, cell, visited=False, distance=1000000):

        self.VISITED = 'VISITED'
        self.MOVEABLE = 'UNEXPLORED'

        self.location = {'x' : cell['x'], 'y': cell['y']}
        self.neighbours = {'north' : cell['north'], 'south': cell['south'], 'east' : cell['east'], 'west': cell['west']}
        self.visited = visited

    def getLocationString(self):
        return 'x=' + str(self.location['x']) +  '&' + 'y=' + str(self.location['y'])

    def setVisited(self):
        this.visited = True

    def possible_directions(self):
        dirs = []
        for direction in self.neighbours:
            if self.neighbours[direction] == self.MOVEABLE:
                dirs.append(direction)
        return dirs

    def hasMoves(self):
        return self.possible_directions() > 0
