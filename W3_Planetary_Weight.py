MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Inputs earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Inputs planet name
    planet = input("Enter a planet: ")

    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("No such planet exists in solar system!")
        gravity_constant = 0

    # Multiplication 
    planetary_weight = round(earth_weight * gravity_constant , 2)

    # Print the result
    print(f"The equivalent weight on {planet}: {planetary_weight}")

if __name__ == "__main__":
    main()