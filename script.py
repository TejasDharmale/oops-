class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof Woof!")

        return "Woof Woof!"


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner1 = Owner("John Doe", "123 Main St", "555-1234")
dog = Dog("Bruce", "Labrador", owner1)
dog.bark()

print(dog.name)
print(dog.breed)
print(dog.owner.name)
print(dog.owner.address)
print(dog.owner.contact_number)

owner2 = Owner("Jane Smith", "456 Elm St", "555-5678")
dog2 = Dog("Max", "Golden Retriever", owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.name)
print(dog2.owner.address)
print(dog2.owner.contact_number)
