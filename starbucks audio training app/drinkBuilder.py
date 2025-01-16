import audioHandler
import drinkOptions

drinkNames = ["Affogato-style frappuccino blended coffee", 
              "Affogato-style frappuccino blended creme", 
              "latte"]
size = ["short", "tall", "grande", "venti", "trenta"]
shots = ["single", "double", "triple", "quad", "extra"]
espresso = ["blonde", "decaf", "regular", "frap roast"]
iced = ["iced", "not iced"]
blended = ["blended", "not blended"]
shaken = ["shaken", "not shaken"]
syrups = ["caramel", "cinnamon dolce", "hazelnut", "vanila", "classic", "peppermint", 
          "brown sugar", "strawberry", "chai", "honey blend", "liquid cane", "sugar free vanilla",
          "mocha", "white chocolate mocha", "caramel sauce", "dark caramel", "caramel brulee", 
          "gingerbread", "chestnut praline", "sugar cookie", "pecan", "pumpkin", "other"]
milk = ["nonfat", "2%", "whole milk", "soy milk", "lactaid", "coconut", "almond", "oat", "breve",
        "heavy cream", "add dairy", "vanilla sweet cream", "ND Vanilla Coffee Enhancer"]
milkSplashAmount = ["light", "regular", "extra"]
toppings = ["ice", "water", "whipped cream", "agave", "splenda", "sugar", "raw sugar", "stevia", "honey",
            "strawberry puree", "frappuccino chips", "vanilla bean powder", "matcha", "lemonade", "mocha drizzle",
            "line cup with mocha", "caramel drizle", "line cup with caramel", "foam", "strawberry inclusions",
            "mango dragonfruit inclusions", "pineapple inclusions", "cranberry inclusions"]

class DrinkOrder:
    def __init__(self, name, size, shots, espresso, iced, blended, shaken, syrups, 
                 syrupAmount, milkbase, milkSplash, milkSplashAmount, toppings, 
                 toppingsAmount, coldFoams, frapBase, frapBasePumps, directions):
        self.name = name
        self.size = size
        self.shots = shots
        self.espresso = espresso
        self.iced = iced
        self.blended = blended
        self.shaken = shaken
        self.syrups = syrups
        self.syrupAmount = syrupAmount
        self.milkbase = milkbase
        self.milkSplash = milkSplash
        self.milkSplashAmount = milkSplashAmount
        self.toppings = toppings
        self.toppingsAmount = toppingsAmount
        self.coldFoams = coldFoams
        self.frapBase = frapBase
        self.frapBasePumps = frapBasePumps
        self.directions = directions

    def printDrink(self):
        print(self.name)
        print(self.size)
        print(self.shots)
        print(self.espresso)
        print(self.iced)
        print(self.syrups)
        print(self.syrupAmount)
        print(self.milkbase)
        print(self.milkSplash)
        print(self.milkSplashAmount)
        print(self.toppings)
        print(self.toppingsAmount)
        print(self.coldFoams)
        print(self.directions)   

    def drinkDirections(self):
        print("Make a " + self.name)
        print("Grab a " + self.size + " cup and label it")
        if(self.size == size[2]):
            print("Queue two regular shots")
        if(self.iced == "not iced"):
            print("Fill steaming pitcher up to " + self.size + " line with 2% milk and steam milk")
        print("Add milk to cup, put on lid and hand off")

        audioHandler.SpeakText("Make a " + self.name)
        audioHandler.SpeakText("Grab a " + self.size + " cup and label it")
        if(self.size == size[2]):
            audioHandler.SpeakText("Queue two regular shots")
        if(self.iced == "not iced"):
            audioHandler.SpeakText("Fill steaming pitcher up to " + self.size + " line with 2% milk and steam milk")
        audioHandler.SpeakText("Add milk to cup, put on lid and hand off")
        

drinks = []
drinks.append(DrinkOrder(drinkOptions.drinkNames[0], size[1], shots[1], espresso[2], iced[1], "", 0, 
                        milk[1], "", "", "", "", "", ""))
drinks[0].printDrink()


# orderText = SpeechToText()
# print(orderText)
# if("grande latte" in orderText):
#     drinks[0].drinkDirections()