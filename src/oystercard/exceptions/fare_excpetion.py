class CustomFareException(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
