class Pet:
    def __init__(self, owner, name, age):
        self.owner = owner
        self.name = name
        self.age = age

    def pet_info(self):
        print(f"{self.name}\nAge: {self.age}\nOwner: {self.owner}")

class Dog(Pet):
    def __init__(self, owner, name, age, breed):
        self.breed = breed
        super().__init__(owner, name, age)

    def pet_info(self):
        super().pet_info()
        print(f"Breed: {self.breed}")

