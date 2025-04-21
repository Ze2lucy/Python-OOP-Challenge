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
