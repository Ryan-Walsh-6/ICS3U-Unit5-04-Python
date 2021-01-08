#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # calculates volume

    # process & output
    volume_of_cylinder = (math.pi) * (radius) ** 2 * (height)

    return volume_of_cylinder


def main():
    # this program calculates the volume of a cylinder

    while True:
        try:
            radius_from_user = input("Enter the radius of the cylinder (mm):")
            radius_from_user = float(radius_from_user)
            height_from_user = input("Enter the height of the cylinder (mm):")
            print("\n", end="")
            height_from_user = float(height_from_user)
            if radius_from_user < 0 or height_from_user < 0:
                print("Please ensure all values are positive.")
                print("\n", end="")
            else:
                break
        except Exception:
            print("Please enter a valid number.")
            print("\n", end="")

    # call function
    volume = calculate_volume(radius_from_user, height_from_user)

    print("The volume of a cylinder with radius {0}mm and height {1}mm is"
          " {2:,.2f}mm³".format(radius_from_user, height_from_user, volume))


if __name__ == "__main__":
    main()
