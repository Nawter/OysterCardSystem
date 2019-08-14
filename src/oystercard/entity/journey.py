from src.oystercard.entity.fare import Fare
from src.oystercard.exceptions.fare_excpetion import CustomFareException
from src.oystercard.entity.station import Station


class Journey(object):

    def __init__(self):
        self._card = None
        self._transport_type = None
        self._start_point = Station
        self._end_point = Station

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, transport, start_point, card):
        try:
            Fare.check_limit(transport, card)
            Fare.charge_maximum(transport, card)
            self._card = card
            self._transport_type = transport
            self._start_point = start_point
        except CustomFareException:
            print('CustomFareException from journey')

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, end_point):
        try:
            self._end_point = end_point
            Fare.charge(self._transport_type, self, self._card, self.is_card_crossing_zone_one())
        except CustomFareException:
            print('CustomFareException from journey')

    def get_crossed_zones(self):
        if self.get_start_point() is not None and self.get_end_point() is not None:
            minimum = 9

            for start_point in self.get_start_point().get_zone():
                for end_point in self.get_end_point().get_zone():
                    visited = abs(start_point - end_point) + 1
                    if visited < minimum:
                        minimum = visited
                    if minimum == 1:
                        break

            return minimum

    def is_card_crossing_zone_one(self):
        if self.get_start_point() is not None and self.get_end_point() is not None:
            if len(self.get_start_point().get_zone()) == 1 and 1 in self.get_start_point().get_zone():
                return True

            if len(self.get_end_point().get_zone()) == 1 and 1 in self.get_end_point().get_zone():
                return True

            return False
