class Station(object):

    def __init__(self):
        self._name = None
        self._zone = None

    def get_station(self):
        return self

    def set_station(self, name, zone):
        self._name = name
        self._zone = zone

    def get_zone(self):
        return self._zone
