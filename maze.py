#!/usr/bin/env python

## Open an xls based data file, and read in the values
## Call our algorith method to check if a row is indeed malicious based on the previous rows,
## and previous information the detector was given

import urllib3, json
import logging, sys

logging.basicConfig(filename='out.log',level=logging.DEBUG)
sys.setrecursionlimit(10000)

class Maze(object):

    def __init__(self, url):

        self.url = url
        self.init_path = url + '/api/init'
        self.http = urllib3.PoolManager()


        # Initialize our Maze
        request = self.http.request('POST', self.init_path)
        request = json.loads(request.data)
        self._guid = request["currentCell"]["mazeGuid"]

        # Now initialize all our paths
        self.move_path = url + '/api/move' + '?mazeGuid=' + self._guid
        self.jump_path = url + '/api/jump' + '?mazeGuid=' + self._guid
        self.cell_path = url + '/api/currentCell' + '?mazeGuid=' + self._guid

    def guid(self):
        return self._guid

    def atEnd(self):
        request = self.http.request('GET', self.cell_path)
        logging.debug(request.data)
        return json.loads(request.data)['currentCell']['atEnd'] == 'True'


    def current_location(self):
        request = self.http.request('GET', self.cell_path)
        currentLocation = json.loads(request.data)['currentCell']
        #print "Location " + str(currentLocation['x']) + ", " + str(currentLocation['y'])
        return currentLocation

    def jumpTo(self, node):
        #print "Jumping to " + str(self.jump_path) + "&" + str(node.getLocationString())
        self.http.request('POST', str(self.jump_path) + "&" + str(node.getLocationString()))

    def move(self, direction):
        #print "Moving as follows: " + str(self.move_path) + "&direction=" + str(direction).upper()
        request = self.http.request('POST', str(self.move_path) + "&direction=" + str(direction).upper())
        return json.loads(request.data)['currentCell']


