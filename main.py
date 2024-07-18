# This is a sample Python script.
from rooms import Room
from room_types import RoomTypes
from hotel import Hotel


room1 = Room(RoomTypes.SINGLE, 101, 12)
room2 = Room(RoomTypes.SINGLE_DELUXE, 201, 20)
room3 = Room(RoomTypes.DOUBLE, 301, 40)
room4 = Room(RoomTypes.DOUBLE_DELUXE, 401, 45)
room5 = Room(RoomTypes.APARTMENT, 501, 50)
room6 = Room(RoomTypes.VIP, 601, 80)

print(room5)
print(room1)
print("_________________")
hotel = Hotel()

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)
hotel.add_room(room4)
hotel.add_room(room5)
hotel.add_room(room6)
print(hotel.available_rooms())
print(hotel.rooms_for_cleaning())
room1.book_room()
#print(hotel.room_by_type())
print("_________________")
print(hotel.available_rooms())
#room1.check_out()
room4.book_room()
room2.book_room()

print(hotel.rooms_for_cleaning())
print("_________________")
room1.cleaning()
print(hotel.available_rooms())
print(hotel.rooms_for_cleaning())
print(hotel.booked_rooms())
print("_________________")
room1.check_out()
room2.check_out()
print(hotel.available_rooms())
print(hotel.rooms_for_cleaning())
print(hotel.booked_rooms())

print("_________________")
print(hotel.room_by_price(120))
