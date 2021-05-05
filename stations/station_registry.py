import os
import json


RESOURCES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data', 'resources'
)

class StationRegistry:

    def __init__(self):
        self.station_list = []

        with open(os.path.join(RESOURCES, 'stations.json'), 'r') as json_file:
            self.station_list = json.load(json_file)

    def get(self, station_id):
        try:
            return next(filter(lambda s: s["id"] == str(station_id), self.station_list))
        except StopIteration:
            raise StationDoesNotExist()

    def get_list(self):
        return self.station_list

class StationDoesNotExist(Exception):
    pass
