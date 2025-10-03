cup_size= input("Choose coffee cup size (small, medium, large): ").lower()

if cup_size=="small":
    print(f"cost: 10 Rs")
elif cup_size=="medium":
    print(f"cost: 15 Rs")
elif cup_size=="large":
    print(f"cost: 20 Rs")
else:
    print(f"Selected cup size is not available")