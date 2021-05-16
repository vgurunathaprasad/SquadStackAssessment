from ParkingSlotService import ParkingSlotService

service = ParkingSlotService()


def parkingLotIsCreated():
    return service.sizeOfParkingLot > 0


if __name__ == '__main__':
    while True:
        input_query = input("#")
        query = input_query.split()
        if query[0] == 'Create_parking_lot':
            parkingLotSize = int(query[1])
            service.setSizeOfParkingLot(parkingLotSize)
        elif query[0] == 'Park':
            if parkingLotIsCreated():
                carRegistrationNumber = query[1]
                driverAge = int(query[3])
                service.parkACar(carRegistrationNumber, driverAge)
        elif query[0] == 'Slot_numbers_for_driver_of_age':
            if parkingLotIsCreated():
                driverAge = int(query[1])
                service.getParkingSlotNumbersByDriverAge(driverAge)
        elif query[0] == 'Slot_number_for_car_with_number':
            if parkingLotIsCreated():
                carRegistrationNumber = query[1]
                service.getParkingSlotNumberByCarRegistrationNumber(carRegistrationNumber)
        elif query[0] == 'Leave':
            if parkingLotIsCreated():
                slotNumber = int(query[1])
                service.unParkACar(slotNumber)
        elif query[0] == 'Vehicle_registration_number_for_driver_of_age':
            if parkingLotIsCreated():
                driverAge = int(query[1])
                service.getCarRegistrationNumbersByDriverAge(driverAge)
        elif query[0] == 'Quit':
            print('Tata... Bye! Bye!')
            break
