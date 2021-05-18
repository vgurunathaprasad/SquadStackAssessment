from ParkingSlotRepository import ParkingSlotRepository
from ParkingSlot import ParkingSlot


class ParkingSlotService:
    def __init__(self):
        self.repo = ParkingSlotRepository()
        self.sizeOfParkingLot = 0
        self.parkingSlotStatusBoard = []

    def setSizeOfParkingLot(self, sizeOfParkingLot):
        self.sizeOfParkingLot = sizeOfParkingLot
        self.initializeParkingSlotStatusBoard()
        self.repo = ParkingSlotRepository()
        print('Created parking of ' + str(self.sizeOfParkingLot) + ' slots')

    def initializeParkingSlotStatusBoard(self):
        for index in range(self.sizeOfParkingLot + 1):
            self.parkingSlotStatusBoard.append(False)

    def parkingLotIsFull(self):
        return all(self.parkingSlotStatusBoard[1:])

    def getNearestEmptyParkingSlot(self):
        index = 1
        while self.parkingSlotStatusBoard[index] is True:
            index = index + 1
        return index

    def blockParkingSlot(self, slotNumber):
        self.parkingSlotStatusBoard[slotNumber] = True

    def unBlockParkingSlot(self, slotNumber):
        self.parkingSlotStatusBoard[slotNumber] = False

    def parkACar(self, carRegistrationNumber, driverAge):
        if self.parkingLotIsFull():
            print('Parking lot is full')
        else:
            slotNumber = self.getNearestEmptyParkingSlot()
            parkingSlot = ParkingSlot(slotNumber, carRegistrationNumber, driverAge)
            self.repo.addCarToParkingLot(parkingSlot)
            self.blockParkingSlot(slotNumber)
            print('Car with vehicle registration number "' + parkingSlot.carRegistrationNumber +
                  '" has been parked at slot number ' + str(parkingSlot.slotNumber))

    def unParkACar(self, slotNumber):
        parkingSlot = self.repo.getParkingSlotBySlotNumber(slotNumber)
        if parkingSlot.isValid():
            print('Slot number ' + str(parkingSlot.slotNumber) +
                  ' vacated, the car with vehicle registration number "' + parkingSlot.carRegistrationNumber +
                  '" left the space, the driver of the car was of age ' + str(parkingSlot.driverAge))
            self.repo.removeCarFromParkingLot(parkingSlot)
            self.unBlockParkingSlot(slotNumber)
        else:
            print('Slot number ' + str(slotNumber) + ' is empty. Nothing to leave')

    def getParkingSlotNumbersByDriverAge(self, driverAge):
        slots = self.repo.getParkingSlotsOfCarsByDriverAge(driverAge)
        if len(slots) == 0:
            print('No parked car matches the query')
        else:
            slotNumbers = []
            for slot in slots:
                slotNumbers.append(slot.slotNumber)
            print(','.join(map(str, slotNumbers)))

    def getParkingSlotNumberByCarRegistrationNumber(self, carRegistrationNumber):
        slot = self.repo.getParkingSlotOfCarByCarRegistrationNumber(carRegistrationNumber)
        if slot.isValid():
            print(slot.slotNumber)
        else:
            print('No parked car matches the query')

    def getCarRegistrationNumbersByDriverAge(self, driverAge):
        slots = self.repo.getParkingSlotsOfCarsByDriverAge(driverAge)
        if len(slots) == 0:
            print('No parked car matches the query')
        else:
            carRegistrationNumbers = []
            for slot in slots:
                carRegistrationNumbers.append(slot.carRegistrationNumber)
            print(','.join(carRegistrationNumbers))
