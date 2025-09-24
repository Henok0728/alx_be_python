ask= input("What's the weather like today? (sunny, rainy, snowy, windy): ").strip().lower()
if ask == "sunny":
    print(" Wear a t-shirt and sunglasses.")
elif ask == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif ask == "cold":
    print(" Make sure to wear a warm coat and a scarf.")
else:
    print(" Sorry, I don't have recommendations for this weather."):