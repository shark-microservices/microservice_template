import connexion


from stations import StationRegistry, StationDoesNotExist

registry = StationRegistry()

def get_station_list():
    return registry.get_list()

def get_station(station_id):
    return registry.get(station_id)


app = connexion.FlaskApp(
    __name__, specification_dir='./', options={'swagger_url': '/'}
)
app.add_api('openapi.yaml')
app.run(port=5000)
