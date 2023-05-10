import time

class ParkingLot:
    MAX_CAPACITY = 40
    LEVEL_CAPACITY = 20
    EMPTY_SPOT = 0

    def __init__(self) -> None:
        """Initialize the parking lots"""
        self.lots = [self.EMPTY_SPOT] * self.MAX_CAPACITY

    def find_index(self, element) -> int:
        """
        Find index of the element in the parking lots list
        """
        try:
            return self.lots.index(element)
        except ValueError:
            return -1

    def assign_parking_lot(self, vehicle_number) -> dict:
        """
        Assign parking lot for given vehicle number.
        """
        # checks the vehicle number already exist or not
        if vehicle_number in self.lots:
            return { "status": "error", "message": "Vehicle with given number is already exists. Please check number again." }

        ind = self.find_index(self.EMPTY_SPOT)
        # check whether parking lot is full or not
        if ind == -1:
            return { "status": "error", "message": "Parking lot is currently full." }

        self.lots[ind] = vehicle_number
        level = "A" if ind < self.LEVEL_CAPACITY else "B"

        return {"level": level, "spot": ind + 1}

    def retrieve_vehicle(self, vehicle_number) -> dict:
        """
        Retrieve Vehicle from parking lot if already parked.
        """
        # find the spot number of vehicle
        ind = self.find_index(vehicle_number)
        if ind == -1:
            return { "status": "error", "message": "Vehicle not exist with given number" }

        self.lots[ind] = self.EMPTY_SPOT
        level = "A" if ind < self.LEVEL_CAPACITY else "B"

        return {"level": level, "spot": ind + 1}


if __name__ == "__main__":
    parking_lot = ParkingLot()
    while True:
        try:
            op = int(input(
                    "\t\t** Parking Lot **\n"
                    "Select the below option you want to perform:\n\n"
                    "1. Assign Parking Lot\n"
                    "2. Retrieve From Parking\n\n"
                    "Select input: "
                ))
            if op not in [1, 2]:
                raise ValueError("Invalid option selected. Please select correct option.")

            num = input("Enter vehicle number: ")
            out = parking_lot.assign_parking_lot(num) if op == 1 else parking_lot.retrieve_vehicle(num)
            print(out)

            ch = input("Do you want to continue? (Press Y if yes): ")
            if ch.lower() != "y":
                break
        except ValueError as e:
            print("Error: ", e)
            time.sleep(2)
