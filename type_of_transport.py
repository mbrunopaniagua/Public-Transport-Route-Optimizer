import enum


class Transport(enum.Enum):
    METRO = 1, "Metro", "metro_stations.json"
    RENFE = 2, "Renfe", "renfe_stations.json"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: int, text: str = None, file: str = None):
        self._text_ = text
        self._file_ = file

    def __str__(self):
        return str(self.value)

    # this makes sure that the description is read-only
    @property
    def text(self):
        return self._text_

    @property
    def file(self):
        return self._file_
