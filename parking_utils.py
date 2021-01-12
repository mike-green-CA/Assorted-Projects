# Author: Michael Green.
# Date: 2020-12-01
# Solution for: "parking_utils.py".

import re


def validate_car_info(make, model, year, license):
    """This method will validate the cars:
        - Make
        - Model
        - Year
        - License
    If they're all valid it will return True.
    """

    if validate_make(make) == False:
        return False

    elif validate_model(model) == False:
        return False

    elif validate_year(year) == False:
        return False

    elif validate_license(license) == False:
        return False

    return True


def validate_make(make):
    """Validates the make making sure its Upper case and lower case letters, numbers, and spaces."""
    make_regex = "[a-zA-Z0-9 ]+"
    is_valid = True

    if re.search(make_regex,make) is None:
        raise ValueError("The Make is invalid")
        is_valid = False

    return is_valid


def validate_model(model):
    """Validates the model making sure its Upper case and lower case letters, numbers, and spaces."""
    model_regex = "[a-zA-Z0-9 ]+"
    is_valid = True

    if re.search(model_regex,model) is None:
        raise ValueError("The Model is invalid")
        is_valid = False

    return is_valid


def validate_year(year):
    """Makes sure the year is 4 digits, and greater than 1900"""
    minimum_year = 1900
    year_regex = "^[0-9]{4}$"
    is_valid = True

    if re.search(year_regex, year) is None:
        raise ValueError("The Year is invalid")
        is_valid = False

    if int(year) < minimum_year:
        raise ValueError("The Year is invalid")
        is_valid = False

    return is_valid


def validate_license(license):
    """Validates the license"""
    license_regex = "^[A-Z]+[0-9]*$"
    is_valid = True

    if re.search(license_regex,license) is None:
        raise ValueError("The License is invalid")
        is_valid = False

    return is_valid
