# Author: Michael Green.
# Date: 2020-12-01
# Solution for: "parking.py".

import parking_utils
import json

list_of_cars = []


def write_to_cars_file():
    """Will write the list of dictionaries of books to the file."""
    try:
        file_name = "cars.json"
        out_file = open(file_name,"w")
        json.dump(list_of_cars, out_file, indent=4)

    except:
        print("error writing to json file")

    finally:
        out_file.close()


def read_from_cars_file():
    """Will read in the json file and load the info to a list of dictionaries to return."""
    new_list = []

    try:
        file_name = "cars.json"
        in_file = open(file_name,"r")
        new_list = json.load(in_file)

        in_file.close()

    except:
        print("error reading in json file")

    return new_list


def main():

    global list_of_cars
    list_of_cars = read_from_cars_file()

    quit_condition = False

    while not quit_condition:
        command = input("Please enter a command. Add Car (a), List Cars (n), Find Car (f), Remove Car (r) or Quit (q)")

        if command != 'a' and command != 'n' and command != 'f' and command != 'r' and command != 'q':
            print("Invalid command option, please try again.")
            continue

        if command == 'a':
            make = input("Enter the make: ")
            model = input("Enter the model: ")
            year = input("Enter the year: ")
            license = input("Enter the license: ")

            try:
                if parking_utils.validate_car_info(make,model,year,license):

                    the_car = {"make": make,
                               "model": model,
                               "year": year,
                               "license": license
                               }

                    duplicate_license = False
                    for car in range(len(list_of_cars)):
                        if list_of_cars[car]['license'] == license:
                            duplicate = True

                    if duplicate_license == True:
                        print("Car already exists in the Parking Lot")

                    else:
                        list_of_cars.append(the_car)
                        write_to_cars_file()

            except ValueError as e:
                print(e)

            except TypeError as te:
                print(te)

        if command == 'n':
            for car in list_of_cars:
                formatted_string = """%s %s %s with license plate %s""" % (car['year'],car['make'],car['model'],car['license'])
                print(formatted_string)

        if command == 'f':
            found_car = False
            license_query = input("License plate: ")
            if parking_utils.validate_license(license_query) == True:
                for car in range(len(list_of_cars)):
                    if license_query in list_of_cars[car]['license']:
                        formatted_string = """%s %s %s with license plate %s""" % (list_of_cars[car]['year'],
                                                                                   list_of_cars[car]['make'],
                                                                                   list_of_cars[car]['model'],
                                                                                   list_of_cars[car]['license'])
                        print(formatted_string)
                        found_car = True

                if found_car == False:
                    print("No car found.")

        if command == 'r':
            found_car = False
            license_query = input("License plate: ")
            if parking_utils.validate_license(license_query):
                for car in range(len(list_of_cars)):
                    if license_query == list_of_cars[car]['license']:
                        del list_of_cars[car]
                        found_car = True
                        write_to_cars_file()

            if found_car == False:
                print("No car found.")

        if command == 'q':
            quit_condition = True
            continue


if __name__ == '__main__':
    main()
