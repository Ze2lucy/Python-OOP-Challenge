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
