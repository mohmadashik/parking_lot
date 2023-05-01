def show_welcome_text():
    print("Welcome to Ashik's Parking Lot")

def get_user_choice():
    try:
        print("choose your option")
        print("1.park a new car in the lot")
        print("2.retreive the parking spot of your car")
        print("3.display all cars")  # I have added this extra feature to list all the cars
        print("0.quit")
        choice = int(input())
        return choice
    except ValueError:
        print("please enter a valid number as an input")