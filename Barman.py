class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Drink:
    def __init__(self, ingredient1, ingredient2, ingredient3, volume):
        self.ingredient1 = ingredient1
        self.ingredient2 = ingredient2
        self.ingredient3 = ingredient3
        self.volume = volume

class Barman:
    def createDrink(self, name1, amount1, name2, amount2, name3, amount3):
        total_volume = amount1 + amount2 + amount3
        proportion1 = amount1 / total_volume
        proportion2 = amount2 / total_volume
        proportion3 = amount3 / total_volume
        ingredient1 = Ingredient(name1, amount1)
        ingredient2 = Ingredient(name2, amount2)
        ingredient3 = Ingredient(name3, amount3)
        drink = Drink(ingredient1, ingredient2, ingredient3, total_volume)
        return drink

    def printDrink(self, drink):
        print("Składniki drinka to:", drink.ingredient1.name, ",", drink.ingredient2.name, ",", drink.ingredient3.name, "w proporcjach", format(drink.ingredient1.amount/drink.volume, '.2f'), ",", format(drink.ingredient2.amount/drink.volume, '.2f'), ",", format(drink.ingredient3.amount/drink.volume, '.2f'), ". Jego pojemność to", drink.volume, "ml")

barman = Barman()
drink = barman.createDrink("Sok ananasowy", 100, "Likier Malibu", 50, "Mleko kokosowe", 100)
barman.printDrink(drink)
