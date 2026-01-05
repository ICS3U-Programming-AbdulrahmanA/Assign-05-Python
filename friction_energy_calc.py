#!/usr/bin/env python3
# Created by: Abdul
# Created on: 2025/12/18
# This program calculates resting energy and frictional force of an object

# Constants
# speed of light (m/s)
C = 3.00e8
# gravitational acceleration (m/s^2)
G = 9.81

# function to calculate resting energy
def calculate_energy(mass):
    energy = mass * C ** 2
    return energy


# function to calculate friction force
def calculate_friction_force(mass, material_choice):
    # Set coefficient of friction based on user input
    if material_choice == 1:
        # Metal on Metal
        mu = 0.60
    elif material_choice == 2:
        # Wood on Wood
        mu = 0.40
    elif material_choice == 3:
        # Wood on Metal
        mu = 0.30      
    elif material_choice == 4:
        # Rubber on Concrete
        mu = 0.80
    elif material_choice == 5:
        # Ice on Ice
        mu = 0.05
    else:
        # Safety
        mu = 0.0

    # to calculate normal force
    normal_force = mass * G    
    # to calculate frictional force    
    friction_force = mu * normal_force  

    return friction_force, mu


def main():
    print("Energy and Friction Calculator")

    while True:
        try:
            mass = float(input("Enter the mass of the object (kg): "))

            print("\nSelect the materials in contact:")
            print("1. Metal on Metal")
            print("2. Wood on Wood")
            print("3. Wood on Metal")
            print("4. Rubber on Concrete")
            print("5. Ice on Ice")

            choice = int(input("Enter your choice (1-5): "))

            # Input validation
            if mass > 0 and 1 <= choice <= 5:
                break
            else:
                print("\nError: Mass must be positive and choice must be 1–5.\n")

        except ValueError:
            print("\nError: Please enter numeric values only.\n")

    # Function calls
    energy = calculate_energy(mass)
    friction_force = calculate_friction_force(mass, choice)[0]
    mu = calculate_friction_force(mass, choice)[1]

    # Output results
    print("\n--- Results ---")
    print(f"Mass: {mass:.2f} kg")
    print(f"Coefficient of friction (μ): {mu}")
    print(f"Rest Energy: {energy:.2e} J")
    print(f"Friction Force: {friction_force:.2f} N")


if __name__ == "__main__":
    main()
