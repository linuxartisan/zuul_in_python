from Parser import Parser
from Room import Room
from Item import Item
from CommandWords import CommandWords
from Command import Command


# CONSTANTS
LOCKED = True
UNLOCKED = False
TIMELIMIT = 20
MAXITEMCAPACITY = 5

# global vars
parser :Parser = Parser()
currentRoom :Room = None
finalRoom :Room = None
itemsWithPlayer = []
backtrack = []


def main():
    try:
        play()
    except BaseException as ex:
        print(ex)

def createRooms():
    global currentRoom
    global finalRoom

    # create the rooms
    outside = Room("outside the hospital")
    waitingArea = Room("in the waiting area")
    reception = Room("in the hospital's reception area")
    opd = Room("in the OPD section")
    restrooms = Room("in the restrooms")
    passage0 = Room("in the ground floor passage")
    generalWard = Room("in the hospital's General Ward")
    lobby = Room("in the lobby on 1st floor")
    passage1 = Room("in the first floor passage")
    icu = Room("in the ICU")
    operationTheator = Room("in the Operation Theator")
    deluxeRoom1 = Room("in the private Delux Room 1")
    deluxeRoom2 = Room("in the private Delux Room 2")
    deluxeRoom3 = Room("in the private Delux Room 3")

    # create items
    keyToEntrance = Item("Key1", "opens the door to the Waiting Area")
    keyToGeneralWard = Item("Key2", "opens the door to the General Ward")
    keyToICU = Item("Key3", "opens the ICU door")
    oxygenTank = Item("Oxygen_Tank", "required for patients having difficulty in breathing")
    walker = Item("Walker", "assists patients with major leg injuries to walk")
    crutches = Item("Crutches", "assists patients with minor leg injuries to walk")
    insulinPump = Item("Insulin_Pump", "required for diabetic patients")
    nebulizer = Item("Nebulizer", "used by patients for taking steam")
    ventilator = Item("Ventilator", "used for patients with weak lungs")
    wheelchair = Item("Wheel_Chair", "required for transporting patients within the hospital")
    electricWheelchair = Item("Electric_Wheel_Chair", "required for transporting patients within the hospital")
    syringe1 = Item("Syringe_1", "Used for injections and IV")
    syringe2 = Item("Syringe_2", "Used for injections and IV")
    syringe3 = Item("Syringe_3", "Used for injections and IV")
    syringe4 = Item("Syringe_4", "Used for injections and IV")
    syringe5 = Item("Syringe_5", "Used for injections and IV")

    # initialise room exits
    outside.setExit("north", waitingArea, LOCKED, keyToEntrance)


    waitingArea.setExit("west", reception, UNLOCKED)
    waitingArea.setExit("north", passage0, UNLOCKED)
    waitingArea.setExit("south", outside, UNLOCKED)
    waitingArea.setExit("east", opd, UNLOCKED)
    waitingArea.setExit("up", lobby, UNLOCKED)

    reception.setExit("east", waitingArea, UNLOCKED)

    opd.setExit("west", waitingArea, UNLOCKED)

    passage0.setExit("west", restrooms, UNLOCKED)
    passage0.setExit("east", generalWard, LOCKED, keyToGeneralWard)
    passage0.setExit("south", waitingArea, UNLOCKED)

    restrooms.setExit("east", passage0, UNLOCKED)

    generalWard.setExit("west", passage0, UNLOCKED)

    lobby.setExit("down", waitingArea, UNLOCKED)
    lobby.setExit("west", icu, LOCKED, keyToICU)
    lobby.setExit("east", operationTheator, UNLOCKED)
    lobby.setExit("north", passage1, UNLOCKED)

    icu.setExit("east", lobby, UNLOCKED)

    operationTheator.setExit("west", lobby, UNLOCKED)

    passage1.setExit("west", deluxeRoom3, UNLOCKED)
    passage1.setExit("north", deluxeRoom2, UNLOCKED)
    passage1.setExit("east", deluxeRoom1, UNLOCKED)
    passage1.setExit("south", lobby, UNLOCKED)

    deluxeRoom1.setExit("west", passage1, UNLOCKED)
    deluxeRoom2.setExit("south", passage1, UNLOCKED)
    deluxeRoom3.setExit("east", passage1, UNLOCKED)

    # starting and final rooms
    currentRoom = outside # start the game in the waiting area
    finalRoom = icu       # room for winning the game


    # add items to the rooms
    outside.addItem(keyToEntrance)

    passage0.addItem(keyToGeneralWard)

    restrooms.addItem(walker)

    opd.addItem(syringe1)
    opd.addItem(nebulizer)

    deluxeRoom1.addItem(oxygenTank)
    deluxeRoom1.addItem(syringe2)

    deluxeRoom2.addItem(keyToICU)

    passage1.addItem(crutches)

    operationTheator.addItem(insulinPump)
    operationTheator.addItem(syringe3)

    reception.addItem(syringe5)
    reception.addItem(syringe4)

    lobby.addItem(wheelchair)

    deluxeRoom3.addItem(electricWheelchair)

    generalWard.addItem(ventilator)


def play():
    createRooms()
    _printWelcome()

    # repeatedly read commands and execute them
    finished = False
    while not finished:
        try:
            command = parser.getCommand()
            finished = processCommand(command)
        except BaseException as ex:
            print(ex)

    print("Thank you for playing.  Good bye.")


def processCommand(command):
    wantToQuit = False

    if command is None or command.isUnknown():
        print("I don't know what you mean...")
        return False

    commandWord = command.command_word
    if commandWord == "help":
        _printHelp()

    elif commandWord == "go":
        _goRoom(command)

    elif commandWord == "quit":
        wantToQuit = _quit(command)

    elif commandWord == "take":
        _takeItem(command)

    elif commandWord == "inventory":
        _displayInventory()

    elif commandWord == "drop":
        _dropItem(command)

    elif commandWord == "use":
        _useItem(command)

    elif commandWord == "look":
        _look(command)

    # else command not recognised.

    checkWinningCondition()

    return wantToQuit


def checkWinningCondition():
    global finalRoom

    # if Ventilator and Insulin Pump are dropped in ICU,
    # then player wins
    item1 = finalRoom.getItem("Ventilator")
    item2 = finalRoom.getItem("Insulin_Pump")

    if item1 and item2:
        print("Congrats! You have won the game.")


# Helper functions
def _printWelcome():
    # global currentRoom

    print()
    print("Welcome to the World of Zuul!")
    print("World of Zuul is a new, mildly interesting adventure game.")
    print("Type 'help' if you need help.")
    print()
    print(currentRoom)

def _printHelp():
    global currentRoom

    print("You are at a hospital. You are alone.")
    print("You wander around as you search for two specific items.")
    print("These items are to be carried to the ICU for you to win the game.")
    print("The items are:")
    print("1. Ventilator")
    print("2. Insulin Pump")
    print()
    print("Your command words are:")
    CommandWords.showAll()

    print()
    print(currentRoom)


def _goRoom(command :Command):
    global currentRoom
    global finalRoom
    global backtrack

    if not command.hasSecondWord():
        # if there is no second word, we don't know where to go...
        print("Go where?")
        return

    # check whether player has done max. allowed moves
    if _isTimeLimitExpired():
        print("Time up!")
        return

    direction = command.second_word

    # Try to leave current room.
    # nextRoom = currentRoom.getExit(direction).neighbor
    nextRoom = None
    exitToNextRoom = currentRoom.getExit(direction)
    if exitToNextRoom is None:
        nextRoom = exitToNextRoom.neighboringRoom

    if nextRoom is None:
        print("There is no door!")

    else:
        if currentRoom.isExitLocked(direction):
            print("The door is locked. Need to open it with a key.")
            return

        # push the current room on to the stack before moving ahead
        backtrack.append(currentRoom)

        # go to the next room
        currentRoom = nextRoom
        print(currentRoom)


def _takeItem(command :Command):
    global itemsWithPlayer
    if not command.hasSecondWord():
        # if there is no second word, we don't know what to take...
        print("Take what?")
        return

    if len(itemsWithPlayer) == MAXITEMCAPACITY:
        # if the player's inventory is full, they can't carry more
        print("Can't carry any more!")
        return

    # get item name
    itemName = command.second_word

    # get the Item object
    item = currentRoom.getItem(itemName)

    if item is None:
        print("Take what? Check the item name again.")
        return

    # try adding the item to inventory
    if len(itemsWithPlayer) < MAXITEMCAPACITY and item not in itemsWithPlayer:
        itemsWithPlayer.append(item)
        currentRoom.removeItem(item)


def _dropItem(command :Command):
    global itemsWithPlayer

    if not command.hasSecondWord():
        # if there is no second word, we don't know what to drop...
        print("Drop what?")
        return

    if len(currentRoom.items) >= Room.MAXITEMS:
        # if room is full, we can't add more items to it.
        print("The room is full! Can't drop an item here.")
        print("You'll have to carry it")
        return

    # get item name
    itemName = command.second_word

    # get the Item object from the player's inventory
    item :Item = _getItemFromInventory(itemName)

    if item is None:
        print("Drop what? Check the item name again.")
        return

    # try dropping the item in the room
    try:
        itemsWithPlayer.remove(item)
        currentRoom.addItem(item)
    except ValueError:
        pass


def _getItemFromInventory(itemName):
    for i in itemsWithPlayer:
        if i.name.lower() == itemName.lower():
            return i

    return None

def _useItem(command :Command):
    if not command.hasSecondWord():
        # if there is no second word, we don't know what to take...
        print("Use what?")
        return

    # get the item name
    itemName = command.second_word

    # get the item in the player's inventory
    item = _getItemFromInventory(itemName)

    if item is None:
        print("Use what? Check the item name again.")
        return

    # get all exits (directions only)
    exits = currentRoom.getAllExitDirections()

    for direction in exits:
        # try and get the key to the door in the direction of current room
        key = currentRoom.exitOpensWith(direction)

        # if we have the correct key
        if key is not None and key == item:
            # unlock the door
            currentRoom.unlockExit(direction)
            return

    # if we don't have the key, print message
    print("You don't have the required key.")


def _look(command :Command):
    if not command.hasSecondWord():
        # if there is no second word, show the room's description
        print(currentRoom)
        return

    # get the item name
    itemName = command.second_word

    # get the item present in the room
    item = currentRoom.getItem(itemName)

    if item is None:
        print("Look what? Check the item name again.")
        return

    print(item)


def _displayInventory():
    # loop over all items in inventory
    for item in itemsWithPlayer:
        print(item)

    print("")



def _isTimeLimitExpired():
    return len(backtrack) == TIMELIMIT


def _quit(command):
    if command.hasSecondWord():
        print("Quit what?")
        return False
    else:
        return True  # signal that we want to quit


if __name__ == "__main__":
    main()
