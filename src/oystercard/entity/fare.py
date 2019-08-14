from src.oystercard.enums.transport_type import TransportType
from src.oystercard.enums.fare_type import FareType


class Fare(object):

    @staticmethod
    def charge_maximum(transport, card):
        if transport == TransportType.BUS.get_transport():
            card.go_out(FareType.BUS_FARE.get_price())
        else:
            card.go_out(FareType.MAX_TUBE_FARE.get_price())

    @staticmethod
    def check_limit(transport, card):
        if transport == TransportType.BUS.get_transport():
            card.check_limit(FareType.BUS_FARE.get_price())

    @staticmethod
    def charge(transport, journey, card, cross_boundary_one):
        position = journey.get_crossed_zones()
        if transport == TransportType.TUBE.get_transport():
            if Fare.is_card_pass_one_zone(position) and cross_boundary_one:
                card.go_in(FareType.MAX_TUBE_FARE.get_price() - FareType.ZONE_ONE_FARE.get_price())
            elif Fare.is_card_pass_one_zone(position) and not cross_boundary_one:
                card.go_in(
                    FareType.MAX_TUBE_FARE.get_price() - FareType.ONE_ZONE_NOT_INCLUDING_ZONE_ONE_FARE.get_price())
            elif Fare.is_card_pass_two_zones(position) and cross_boundary_one:
                card.go_in(
                    FareType.MAX_TUBE_FARE.get_price() - FareType.TWO_ZONES_INCLUDING_ZONE_ONE_FARE.get_price())
            elif Fare.is_card_pass_two_zones(position) and not cross_boundary_one:
                card.go_in(FareType.MAX_TUBE_FARE.get_price() - FareType.TWO_ZONES_EXCLUDING_ZONE_ONE_FARE.get_price())
            elif Fare.is_card_pass_three_zones(position):
                card.go_in(FareType.MAX_TUBE_FARE.get_price() - FareType.THREE_ZONES_FARE.get_price())
        else:
            card.go_in(0.0)

    @staticmethod
    def is_card_pass_one_zone(position):
        return position == 1

    @staticmethod
    def is_card_pass_two_zones(position):
        return position == 2

    @staticmethod
    def is_card_pass_three_zones(position):
        return position == 3
