from ParkingSlot import ParkingSlot


class ParkingSlotRepository:
    def __init__(self):
        self.parkingSlots = []
        self.emptyParkingSlot = ParkingSlot(-1, "", 0)

    def addCarToParkingLot(self, parkingCar):
        self.parkingSlots.append(parkingCar)

    def removeCarFromParkingLot(self, parkedCar):
        self.parkingSlots.remove(parkedCar)

    def getParkingSlotsOfCarsByDriverAge(self, driverAge):
        parkingSlots = []
        if len(self.parkingSlots) > 0:
            for slot in self.parkingSlots:
                if slot.driverAge == driverAge:
                    parkingSlots.append(slot)
        return parkingSlots

    def getParkingSlotOfCarByCarRegistrationNumber(self, carRegistrationNumber):
        parkingSlot = self.emptyParkingSlot
        if len(self.parkingSlots) > 0:
            for slot in self.parkingSlots:
                if slot.carRegistrationNumber == carRegistrationNumber:
                    parkingSlot = slot
                    break
        return parkingSlot

    def getParkingSlotBySlotNumber(self, slotNumber):
        parkingSlot = self.emptyParkingSlot
        if len(self.parkingSlots) > 0:
            for slot in self.parkingSlots:
                if slot.slotNumber == slotNumber:
                    parkingSlot = slot
                    break
        return parkingSlot
