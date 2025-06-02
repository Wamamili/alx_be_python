# Weather advice: provides clothing recommendations based on current weather conditions.

def main():
    # user input for weather condition
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Clothing recommendation
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    main()
