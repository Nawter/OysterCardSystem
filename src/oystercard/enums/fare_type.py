from enum import Enum


class FareType(Enum):
    BUS_FARE = 1.8
    MAX_TUBE_FARE = 3.2
    ZONE_ONE_FARE = 2.5
    ONE_ZONE_NOT_INCLUDING_ZONE_ONE_FARE = 2.0
    TWO_ZONES_INCLUDING_ZONE_ONE_FARE = 3.0
    TWO_ZONES_EXCLUDING_ZONE_ONE_FARE = 2.25
    THREE_ZONES_FARE = 3.20

    def get_fare(self):
        return self.name

    def get_price(self):
        return self.value
