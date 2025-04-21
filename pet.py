class Pet:
    def __init__(self, name, pet_type, hunger=0, energy=5, happiness=5):
        self.name = name
        self.type = pet_type
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []
        self.toys = self.get_toys_by_type()

    def get_toys_by_type(self):
        petToys = {
            "cat": ["scratching post", "toy mouse"],
            "dog": ["chew bone", "frisbee"],
            "fish": ["underSea castle", "net", "buried treasure"]
        }
        return petToys.get(self.type, [])

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(
            f"{self.name} just ate! Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(
                f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")

    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
        else:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        print(f"\n{self.name}'s Learned Tricks:")
        if self.tricks:
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print("No tricks learned yet.")

    def get_status(self):
        print("\n--- Pet Status ---")
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Toys: {self.toys}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
        print("------------------\n")


def create_pet():
    pet_type = ""
    valid_types = ["cat", "dog", "fish"]

    while pet_type not in valid_types:
        print("Choose a pet type (cat, dog, fish):")
        pet_type = input("> ").lower()

    name = input(f"What would you like to name your {pet_type}? ")

    # You can set default values here or ask the user for them
    return Pet(name=name, pet_type=pet_type)


def main():
    pet = create_pet()

    menu = {
        "E": ("Feed your pet", pet.eat),
        "S": ("Let your pet sleep", pet.sleep),
        "P": ("Play with your pet", pet.play),
        "T": ("Train a new trick", lambda: pet.train(input("Enter a trick: "))),
        "K": ("Show learned tricks", pet.show_tricks),
        "G": ("Get pet status", pet.get_status),
        "Q": ("Quit", None)
    }


main()
