from rooms import Room


class Hotel:
    def __init__(self) -> None:
        self._rooms: [Room] = []

    def add_room(self, room: Room) -> None:
        if room in self._rooms:
            raise ValueError("Can't add the same room twice!")
        self._rooms.append(room)

    @property
    def rooms(self):
        return self._rooms.copy()

    def available_rooms(self):
        return [str(room) for room in self._rooms if room.available and room.clean]

    def rooms_for_cleaning(self):
        return [str(room) for room in self._rooms if not room.clean]

    def booked_rooms(self):
        return [str(room) for room in self._rooms if not room.available]

    def room_by_type(self, room_type):
        return [str(room) for room in self._rooms if room.type == room_type]

    def room_by_price(self, price):
        return [f'{str(room)} : {self.calculate_price(room, 2)}' for room in self._rooms if self.calculate_price(room, 2) <= price]

    def calculate_price(self, room: Room, modifier: int) -> float:
        return room.default_price * modifier
