class RoomTypes:
    # DROPDOWN LIST
    SINGLE = 'Single room'
    SINGLE_DELUXE = 'Single deluxe room'
    DOUBLE = 'Double room'
    DOUBLE_DELUXE = 'Double deluxe room'
    APARTMENT = 'Appartment'
    VIP = 'VIP room'

    # DISPLAYABLE VALUES
    _rooms_description = {
        SINGLE: "Single room description",
        SINGLE_DELUXE: "Single Deluxe room description",
        DOUBLE: "Double room description",
        DOUBLE_DELUXE: "Double Deluxe room description",
        APARTMENT: "Apartment room description",
        VIP: "VIP room description"
    }

    # retrieve values from this function
    @classmethod
    def room_info(cls, room):
        if room not in cls._rooms_description.keys():
            raise ValueError('There is no such room in the hotel!')
        else:
            return cls._rooms_description[room]
