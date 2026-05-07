MARS_MULTIPLE = 0.378

def main():
    # Getting the input from the user / earth weight
    earth_weight = input("Enter your weight on Earth : ") # text > float    50.5555 , 65 , 100, 120
    earth_weight = float(earth_weight)

    # Applying the multiplication to find mars weight
    # 37.8% = 0.378
    mars_weight = earth_weight * MARS_MULTIPLE
    mars_weight = round(mars_weight , 2)

    # Printing out the result
    # print("Your equivalent weight on Mars is : ", mars_weight )

    print(f"Your equivalent weight on Mars is : {mars_weight}")
    
    
if __name__ == "__main__":
    main()