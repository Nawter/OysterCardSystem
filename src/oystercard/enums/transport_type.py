from enum import Enum


class TransportType(Enum):
    BUS = "Bus"
    TUBE = "Tube"

    def get_transport(self):
        return self.value
