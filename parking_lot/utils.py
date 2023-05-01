def read_a_car_number():
    try:
        car_number = int(input("enter your car number \n"))
        return car_number
    except ValueError:
        print("kindly enter a valid number")