from enum import Enum


class StationType(Enum):
    HOLBORN = [1]
    EARLSCOURT = [1, 2]
    HAMMERSMITH = [2]
    WIMBLEDON = [3]

    def get_name(self):
        return self.name

    def get_zone(self):
        return self.value
