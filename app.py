#!/usr/bin/env python3
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
import connexion
from stations import StationRegistry

registry = StationRegistry()


def get_station_list():
    return registry.get_list()


def get_station(station_id):
    return registry.get(station_id)


app = connexion.FlaskApp(
    __name__, specification_dir='./', options={'swagger_url': '/'}
)
app.add_api('openapi.yaml')

if __name__ == "__main__":
    app.run(port=5000)
