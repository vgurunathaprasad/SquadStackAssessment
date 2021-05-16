parking_base = []
total_parking_slots = 0
all_parking_slots_status = []
parking_lot_is_created = False

class slot:
    def __init__(self,parked_slot_number,vehicle_number,driver_age):
        self.parked_slot_number = parked_slot_number
        self.vehicle_number = vehicle_number
        self.driver_age = driver_age

def get_slots_where_age_of_the_driver_is(age):
    slot_numbers = []
    for vehicle in parking_base:
        if(vehicle.driver_age == age):
            slot_numbers.append(vehicle.parked_slot_number)
    return slot_numbers

def get_vehicles_where_age_of_the_driver_is(age):
    vehicle_numbers = []
    for vehicle in parking_base:
        if(vehicle.driver_age == age):
            vehicle_numbers.append(vehicle.vehicle_number)
    return vehicle_numbers

def get_slot_where_vehicle_number_is(vehicle_number):
    slot_number = -1
    for vehicle in parking_base:
        if(vehicle.vehicle_number == vehicle_number):
            slot_number = vehicle.parked_slot_number
            break;
    return slot_number

def create_parking_slots(total_available_slots):
    total_parking_slots = total_available_slots
    for i in range(total_parking_slots+1):
        all_parking_slots_status.append(0)
    parking_base = []

def parking_base_is_full():
    return all(all_parking_slots_status[1:])

def park_vehicle(vehicle_number,driver_age):
    if(parking_base_is_full()):
        return -1
    parking_slot =  get_nearest_available_slot()
    all_parking_slots_status[parking_slot] = 1
    parked_vehicle = create_slot_for_vehicle(parking_slot,vehicle_number,driver_age)
    parking_base.append(parked_vehicle)
    return parking_slot

def get_nearest_available_slot():
    i=1
    while(all_parking_slots_status[i] != 0):
        i+=1
    return i

def create_slot_for_vehicle(nearest_available_parking_slot_number,vehicle_number,driver_age):
    new_slot = slot(nearest_available_parking_slot_number,vehicle_number,driver_age)
    return new_slot

def leave_parking(parking_slot):
    if(all_parking_slots_status[parking_slot] == 1):
        for vehicle in parking_base:
            if vehicle.parked_slot_number == parking_slot:
                all_parking_slots_status[parking_slot] = 0
                return vehicle
    return -1

def remove_vehicle_from_parking_base(vehicle):
    parking_base.remove(vehicle)
    

while(True):
    query = input("#")
    query_parse = query.split()
    if query_parse[0].startswith("Create_parking_lot"):
        
        parking_lot_size = int(query_parse[1])
        create_parking_slots(parking_lot_size)
        print("Created parking of "+str(parking_lot_size)+" slots")
        parking_lot_is_created = True
        
    elif query_parse[0].startswith("Park"):

        if parking_lot_is_created:
            vehicle_num = query_parse[1]
            driver_age = query_parse[3]
            slot_num = park_vehicle(vehicle_num,driver_age)
            if slot_num == -1:
                print("Parking lot is full")
            else:
                print('Car with vehicle registration number "'+vehicle_num+'" has been parked at slot number '+str(slot_num))
                
    elif query_parse[0].startswith("Slot_numbers_for_driver_of_age"):

        if parking_lot_is_created:
            age = query_parse[1]
            slots = get_slots_where_age_of_the_driver_is(age)
            if(len(slots)>0):
                print(','.join(map(str,slots)))
            else:
                print("No parked car matches the query")
        else:
            print("Parking lot unavailable")
        
    elif query_parse[0].startswith("Slot_number_for_car_with_number"):

        if parking_lot_is_created:
            vehicle_num = query_parse[1]
            slot_num = get_slot_where_vehicle_number_is(vehicle_num)
            if slot_num == -1:
                print("No parked car matches the query")
            else:
                print(slot_num)
        else:
            print("Parking lot unavailable")
        
    elif query_parse[0].startswith("Leave"):
        if parking_lot_is_created:
            slot_num = int(query_parse[1])
            vslot = leave_parking(slot_num)
            if(slot != -1):
                print('Slot number '+str(vslot.parked_slot_number)+' vacated, the car with vehicle registration number "'+
                      vslot.vehicle_number+'" left the space, the driver of the car was of age '+
                      vslot.driver_age)
                remove_vehicle_from_parking_base(vslot)
            else:
                print("No parked car matches the query")
            
        else:
            print("Parking lot unavailable")
        
    elif query_parse[0].startswith("Vehicle_registration_number_for_driver_of_age"):
        if parking_lot_is_created:
            age = query_parse[1]
            vehicle_numbers = get_vehicles_where_age_of_the_driver_is(age)
            if(len(vehicle_numbers)>0):
                print(','.join(map(str,vehicle_numbers)))
            else:
                print("No parked car matches the query")
        else:
            print("Parking lot unavailable")
        pass
    elif query_parse[0].startswith("Quit"):
        break

        
