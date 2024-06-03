class Animal:
    def make_sound(self):
        pass

    def move(self):
        pass

    def feed(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print("Chirp")

    def move(self):
        print("Fly")

    def feed(self):
        print(" I use my beak to feed")    

class Fish(Animal):
    def make_sound(self):
        print("Click")

    def move(self):
        print("Swim") 

    def feed(self):
        print(" I vaccum my food")  

class Dog(Animal):
    def make_sound(self):
        print("Bark") 

    def move(self):
        print("Run") 

    def feed(self):
        print("I use my teeth") 

class Human(Animal):
    def make_sound(self):
        print("Speak") 

    def move(self):
        print("Walk") 

    def feed(self):
        print("I chew my food")                                                            