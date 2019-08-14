from src.oystercard.enums.fare_type import FareType
from src.oystercard.enums.transport_type import TransportType
from src.oystercard.enums.station_type import StationType
from src.oystercard.entity.fare import Fare
from src.oystercard.entity.card import Card
from src.oystercard.entity.journey import Journey
from src.oystercard.entity.station import Station
import pytest
from src.oystercard.exceptions.fare_excpetion import CustomFareException


class TestFare:

    def test_fare_on_bus_charging_ko(self):
        card = Card()
        fare = Fare()
        card.top_up(FareType.BUS_FARE.get_price() - 1.0)
        with pytest.raises(CustomFareException):
            fare.check_limit(TransportType.BUS.get_transport(), card)

    def test_fare_on_bus_charging_maximum(self):
        card = Card()
        fare = Fare()
        card.top_up(FareType.BUS_FARE.get_price())
        fare.charge_maximum(TransportType.BUS.get_transport(), card)
        assert card.get_balance() == 0.0

    def test_fare_on_tube_charging_maximum(self):
        card = Card()
        fare = Fare()
        card.top_up(FareType.MAX_TUBE_FARE.get_price())
        fare.charge_maximum(TransportType.TUBE.get_transport(), card)
        assert card.get_balance() == 0.0

    def test_fare_on_any_bus_journey(self):
        card = Card()
        fare = Fare()
        card.top_up(FareType.BUS_FARE.get_price())
        journey_bus_from_earlscourt_to_chelsea = Journey()
        journey_bus_from_earlscourt_to_chelsea.set_start_point(TransportType.BUS.get_transport(), None, card)
        journey_bus_from_earlscourt_to_chelsea.set_end_point(None)
        fare.charge(TransportType.BUS, journey_bus_from_earlscourt_to_chelsea, card, True)
        assert card.get_balance() == 0

    def test_fare_on_anywhere_in_zone_one(self):
        card = Card()
        start_station = Station()
        end_station = Station()
        start_station.set_station(StationType.HOLBORN.get_name(), StationType.HOLBORN.get_zone())
        end_station.set_station(StationType.EARLSCOURT.get_name(), StationType.EARLSCOURT.get_zone())
        card.top_up(FareType.MAX_TUBE_FARE.get_price())
        journey_tube_from_holborn_to_earlscourt = Journey()
        journey_tube_from_holborn_to_earlscourt.set_start_point(TransportType.TUBE.get_transport(),
                                                                start_station.get_station(), card)
        journey_tube_from_holborn_to_earlscourt.set_end_point(end_station.get_station())
        assert card.get_balance() == FareType.MAX_TUBE_FARE.get_price() - FareType.ZONE_ONE_FARE.get_price()

    def test_fare_on_any_one_zone_outside_zone_one(self):
        card = Card()
        start_station = Station()
        end_station = Station()
        start_station.set_station(StationType.HAMMERSMITH.get_name(), StationType.HAMMERSMITH.get_zone())
        end_station.set_station(StationType.EARLSCOURT.get_name(), StationType.EARLSCOURT.get_zone())
        card.top_up(FareType.MAX_TUBE_FARE.get_price())
        journey_tube_from_hammersmith_to_earlscourt = Journey()
        journey_tube_from_hammersmith_to_earlscourt.set_start_point(TransportType.TUBE.get_transport(),
                                                                    start_station.get_station(), card)
        journey_tube_from_hammersmith_to_earlscourt.set_end_point(end_station.get_station())
        assert card.get_balance() == FareType.MAX_TUBE_FARE.get_price() - FareType.ONE_ZONE_NOT_INCLUDING_ZONE_ONE_FARE.get_price()

    def test_fare_on_any_two_zones_including_zone_one(self):
        card = Card()
        start_station = Station()
        end_station = Station()
        start_station.set_station(StationType.HAMMERSMITH.get_name(), StationType.HAMMERSMITH.get_zone())
        end_station.set_station(StationType.HOLBORN.get_name(), StationType.HOLBORN.get_zone())
        card.top_up(FareType.MAX_TUBE_FARE.get_price())
        journey_tube_from_hammersmith_to_holborn = Journey()
        journey_tube_from_hammersmith_to_holborn.set_start_point(TransportType.TUBE.get_transport(),
                                                                 start_station.get_station(), card)
        journey_tube_from_hammersmith_to_holborn.set_end_point(end_station.get_station())
        assert card.get_balance() == FareType.MAX_TUBE_FARE.get_price() - FareType.TWO_ZONES_INCLUDING_ZONE_ONE_FARE.get_price()

    def test_fare_on_any_two_zones_excluding_zone_one(self):
        card = Card()
        start_station = Station()
        end_station = Station()
        start_station.set_station(StationType.HAMMERSMITH.get_name(), StationType.HAMMERSMITH.get_zone())
        end_station.set_station(StationType.WIMBLEDON.get_name(), StationType.WIMBLEDON.get_zone())
        card.top_up(FareType.MAX_TUBE_FARE.get_price())
        journey_tube_from_hammersmith_to_wimbledon = Journey()
        journey_tube_from_hammersmith_to_wimbledon.set_start_point(TransportType.TUBE.get_transport(),
                                                                   start_station.get_station(), card)
        journey_tube_from_hammersmith_to_wimbledon.set_end_point(end_station.get_station())
        assert card.get_balance() == FareType.MAX_TUBE_FARE.get_price() - FareType.TWO_ZONES_EXCLUDING_ZONE_ONE_FARE.get_price()

    def test_fare_on_any_three_zones(self):
        card = Card()
        start_station = Station()
        end_station = Station()
        start_station.set_station(StationType.HOLBORN.get_name(), StationType.HOLBORN.get_zone())
        end_station.set_station(StationType.WIMBLEDON.get_name(), StationType.WIMBLEDON.get_zone())
        card.top_up(FareType.MAX_TUBE_FARE.get_price())
        journey_tube_from_holborn_to_wimbledon = Journey()
        journey_tube_from_holborn_to_wimbledon.set_start_point(TransportType.TUBE.get_transport(),
                                                               start_station.get_station(), card)
        journey_tube_from_holborn_to_wimbledon.set_end_point(end_station.get_station())
        assert card.get_balance() == FareType.MAX_TUBE_FARE.get_price() - FareType.THREE_ZONES_FARE.get_price()
