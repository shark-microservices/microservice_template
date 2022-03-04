#!/usr/bin/env python3
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
import os
import json


RESOURCES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data', 'resources'
)


class StationRegistry:
    """Documentation here."""

    def __init__(self):
        """Initialize."""
        self.station_list = []

        with open(os.path.join(RESOURCES, 'stations.json'), 'r') as json_file:
            self.station_list = json.load(json_file)

    def get(self, station_id):
        """Return documentation here."""
        try:
            return next(filter(
                lambda s: s["id"] == str(station_id), self.station_list)
            )
        except StopIteration:
            raise StationDoesNotExist()

    def get_list(self):
        """Return documentation here."""
        return self.station_list


class StationDoesNotExist(Exception):
    """Documentation here."""

    pass
