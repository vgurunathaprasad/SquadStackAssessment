class ParkingSlot:
    def __init__(self, slotNumber, carRegistrationNumber, driverAge):
        self.slotNumber = slotNumber
        self.carRegistrationNumber = carRegistrationNumber
        self.driverAge = driverAge

    def isValid(self):
        state = True
        if self.slotNumber == -1:
            state = False
        return state
