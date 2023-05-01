from utils import read_a_car_number
from ui import get_user_choice,show_welcome_text
from parking_area import ParkingArea

def main():
    show_welcome_text()
    choice = 1
    parking_lot_object = ParkingArea()
    while choice:
        choice = get_user_choice()
        if choice == 1:
            car_number = read_a_car_number()
            response = parking_lot_object.park_a_car(car_number=car_number)
            print(response)
        elif choice == 2:
            car_number = read_a_car_number()
            response = parking_lot_object.get_car_spot(car_number=car_number)
            print(response)
        elif choice == 3:
             parking_lot_object.display_all_car_spots()
        elif not choice :
            print('Farewell')
        else:
            print('please choose a valid choice')     
if __name__ == "__main__":
    main()