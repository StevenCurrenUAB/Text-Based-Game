# Text Based Game for fun

inventory = []

def checkInventory():
    if len(inventory) == 0:
        print("The inventory is empty")
    else:
        for i in inventory:
            print(i)

while (True):

    beginning = input("You wake up in your bedroom. What do you do?: ")

    if beginning == "list commands":
        print("look around, take chocolate, check inventory, sleep")

    if beginning == "look around":
        print("You look around your bedroom. There is a chocolate bar on the nightstand")

    if beginning == "take chocolate":
        print("You take the chocolate bar")
        inventory.append("Chocolate Bar")

    if beginning == "check inventory":
        checkInventory()

    if beginning == "sleep":
        print("You go back to sleep")
        break