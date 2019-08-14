import logging

from src.oystercard.entity.card import Card
from src.oystercard.entity.journey import Journey
from src.oystercard.entity.station import Station
from src.oystercard.enums.station_type import StationType
from src.oystercard.enums.transport_type import TransportType


def app():
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    card = Card()
    logger.info('Ready to top up your card')
    card.top_up(30.0)
    logger.info('Card loaded with: {} pounds'.format(card.get_balance()))

    start_station = Station()
    end_station = Station()
    start_station.set_station(StationType.HOLBORN.get_name(), StationType.HOLBORN.get_zone())
    end_station.set_station(StationType.EARLSCOURT.get_name(), StationType.EARLSCOURT.get_zone())
    journey_tube_from_holborn_to_earlscourt = Journey()
    journey_tube_from_holborn_to_earlscourt.set_start_point(TransportType.TUBE.get_transport(),
                                                            start_station.get_station(), card)
    journey_tube_from_holborn_to_earlscourt.set_end_point(end_station.get_station())

    logger.info(
        'Card balance after your first journey from Holborn [London Underground] to Earl’s Court  is : {} pounds'.format(
            card.get_balance()))

    journey_bus_from_earlscourt_to_chelsea = Journey()
    journey_bus_from_earlscourt_to_chelsea.set_start_point(TransportType.BUS.get_transport(), None, card)
    journey_bus_from_earlscourt_to_chelsea.set_end_point(None)

    logger.info(
        'Card balance after your second journey from Earl’s Court [London Bus 328] to Chelsea  is : {} pounds'.format(
            card.get_balance()))

    start_station.set_station(StationType.EARLSCOURT.get_name(), StationType.EARLSCOURT.get_zone())
    end_station.set_station(StationType.HAMMERSMITH.get_name(), StationType.HAMMERSMITH.get_zone())
    journey_tube_from_earlscourt_to_hammersmith = Journey()
    journey_tube_from_earlscourt_to_hammersmith.set_start_point(TransportType.TUBE.get_transport(),
                                                                start_station.get_station(), card)
    journey_tube_from_earlscourt_to_hammersmith.set_end_point(end_station.get_station())

    logger.info(
        'Card balance after your third journey from Earl’s Court [London Underground] to Hammersmith  is : {} pounds'.format(
            card.get_balance()))
