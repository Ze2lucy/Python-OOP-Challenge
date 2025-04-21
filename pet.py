# Pet state
pet = {
    "name": "", "type": "", "age": 0,
    "hunger": 0, "energy": 0, "happiness": 0,
    "toys": [], "tricks": []
}


petToys = {
    "cat": ["scratching post", "toy mouse"],
    "dog": ["chew bone", "frisbee"],
    "fish": ["underSea castle", "net", "buried treasure"]
}


def initPet():
    petOptions = list(petToys.keys())
    petType = ""

    while petType not in petOptions:
        print("Please input a type of pet from the following options:")
        for option in petOptions:
            print(option)
        petType = input("Please input one of the pets: ").lower()

    pet["type"] = petType
    pet["toys"] = petToys[petType]
    print(f"\nYou chose a {petType}. Here are its toys: {pet['toys']}")

    pet["name"] = input(f"What would you like to name your {petType}? ")

    while True:
        try:
            pet["energy"] = int(
                input("How much energy does your pet have? (1-10): "))
            if 1 <= pet["energy"] <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

    # Get pet happiness
    while True:
        try:
            pet["happiness"] = int(input("How happy is your pet? (1-10): "))
            if 1 <= pet["happiness"] <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

    # Get pet hunger level
    while True:
        try:
            pet["hunger"] = int(input("How hungry is your pet? (0-10): "))
            if 0 <= pet["hunger"] <= 10:
                break
            else:
                print("Please enter a number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")

# Pet actions


def eat():
    pet["hunger"] = max(0, pet["hunger"] - 3)
    pet["happiness"] = min(10, pet["happiness"] + 1)
    print(
        f"{pet['name']} just ate! Hunger: {pet['hunger']}, Happiness: {pet['happiness']}")


def sleep():
    pet["energy"] = min(10, pet["energy"] + 5)
    print(f"{pet['name']} is well-rested. Energy: {pet['energy']}")


def play():
    pet["energy"] = max(0, pet["energy"] - 2)
    pet["happiness"] = min(10, pet["happiness"] + 2)
    pet["hunger"] = min(10, pet["hunger"] + 1)
    print(f"{pet['name']} played with its toys! Energy: {pet['energy']}, Happiness: {pet['happiness']}, Hunger: {pet['hunger']}")


def train(trick):
    if trick in pet["tricks"]:
        print(f"{pet['name']} already knows how to {trick}!")
    else:
        pet["tricks"].append(trick)
        print(f"{pet['name']} has learned how to {trick}!")


def show_tricks():
    print(f"\n{pet['name']}'s Learned Tricks:")
    if pet["tricks"]:
        for i, trick in enumerate(pet["tricks"], start=1):
            print(f"{i}. {trick}")
    else:
        print("No tricks learned yet.")


def get_status():
    print("\n--- Pet Status ---")
    for key, value in pet.items():
        if key != "tricks":
            print(f"{key.capitalize()}: {value}")
    print("------------------\n")


# Example of how to use it:
initPet()
get_status()DeprecationWarning
play()
eat()
sleep()
train("roll over")
train("sit")
train("roll over")  # trying to teach again
show_tricks()
get_status()
