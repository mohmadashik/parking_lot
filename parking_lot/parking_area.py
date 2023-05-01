from config import DevelopementConfig
class ParkingArea:
    def __init__(self):
        self.parking_spaces = {}
        for level in DevelopementConfig.LEVELS:
           self.parking_spaces[level]=[]
    def able_to_park_in_level(self,level):
        return len(self.parking_spaces[level])<DevelopementConfig.NO_OF_SPOTS
    def park_a_car(self,car_number):
        for level in DevelopementConfig.LEVELS:
            if self.able_to_park_in_level(level):
                self.parking_spaces[level].append(car_number)
                return "parked succesfully"
        return "parking lot is full"
    def get_car_spot(self,car_number):
        result = {}
        i = 1
        for level in DevelopementConfig.LEVELS:
            if car_number in self.parking_spaces[level]:
                result = {"level":level,"spot":self.parking_spaces[level].index(car_number)+i}
                return result
            i+=DevelopementConfig.NO_OF_SPOTS
        return "This car is not parked in this parking lot sir"
    def display_all_car_spots(self):
        print(self.parking_spaces)