import enum


class TravelMode(enum.Enum):
    SHORTEST_DISTANCE = 1, "Shortest distance"
    FEWER_STATIONS = 2, "Fewer stations"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: int, text: str = None):
        self._text_ = text

    def __str__(self):
        return str(self.value)

    # this makes sure that the description is read-only
    @property
    def text(self):
        return self._text_
