from room_types import RoomTypes


class Room:

    _MINIMUM_PRICE = 10

    def __init__(self, room_type: RoomTypes, room_number: int, default_price: int) -> None:
        self._room_type = room_type
        self.available = True
        self._number = room_number
        self.default_price = default_price
        self._clean = True

    def __str__(self):
        return f'Room: {self._number} {self._room_type}'

    @property
    def type(self) -> RoomTypes:
        return self._room_type

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    @property
    def number(self):
        return self._number

    @property
    def default_price(self):
        return self._default_price

    @default_price.setter
    def default_price(self, value):
        if value >= Room._MINIMUM_PRICE:
            self._default_price = value
        else:
            raise ValueError('Cannot set price below minimum!')

    @property
    def clean(self):
        return self._clean

    @clean.setter
    def clean(self, value):
        self._clean = value

    def book_room(self):
        if not self.available:
            raise ValueError("This room is unavailable")
        if not self.clean:
            raise ValueError("Can't book a dirty room!")

        self.available = False

    def check_out(self):
        if self.available:
            raise ValueError("This room is not booked!")
        self.available = True
        self.clean = False

    def cleaning(self):
        self.clean = True
