# Inheritance in Python my G

class mammals:
    def bark(self):
        print("I'm a dog - I'm finna bite you")

    def meow(self):
        print("I'm a cat - I'm finna scratch your back")


class dogs(mammals):
    def feed(self):
        print("I only eat shit that makes me feel good")


class cats(mammals):
    def feed(self):
        print("Milk is my potion, If I don't get it. I die:-)")


dog1 = dogs()
dog1.feed()
cat1 = cats()
cat1.feed()

