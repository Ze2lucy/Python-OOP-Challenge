
pet = {"name": "", "type": "", "age": 0, "hunger": 0.0, "toys": ""}

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
    print(f"You chose a {petType}. Here are its toys: {pet['toys']}")
    print(petType)


# Call the function
initPet()
