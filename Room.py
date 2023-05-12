from Exit import Exit
from Item import Item

class Room:
    MAXITEMS = 2 # max items in a room

    def __init__(self, description) -> None:
        self.description = description
        self.exits = []
        self.items = []

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def __str__(self) -> str:
        msg = "You are {desc}.\n".format(desc=self.description)
        msg += "Items:\n"
        msg += self._getItemNames() + "\n" + self._getExitString()
        return msg

    def getExit(self, direction) -> Exit:
        for e in self.exits:
            if direction == e.direction:
                return e
        return None

    def setExit(self, direction, neighbor, locked, opens_with = None) -> None:
        self.exits.append(Exit(direction, neighbor, locked, opens_with))

    def getAllExitDirections(self) -> list:
        exit_dirs = [e.direction for e in self.exits]
        return exit_dirs

    def isExitLocked(self, direction) -> bool:
        e = self.getExit(direction)
        if e is not None:
            return e.locked
        else:
            raise ValueError("No such exit")

    def exitOpensWith(self, direction) -> Item:
        e = self.getExit(direction)
        if e is not None:
            return e.opens_with
        else:
            raise ValueError("No such Exit")

    def unlockExit(self, direction):
        e = self.getExit(direction)
        if e is not None:
            e.locked = False
        else:
            raise ValueError("No such Exit")

    def addItem(self, item):
        if len(self.items) == Room.MAXITEMS:
            return False
        self.items.append(item)
        return True

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def getItem(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item

        return None


    def _getItemNames(self):
        item_names = ''
        for i in self.items:
            item_names += i.name + '\n'
        if len(self.items) == 0:
            item_names = 'None'
        return item_names

    def _getExitString(self):
        exits = "Exits: "
        for e in self.exits:
            exits += e.direction + " "
        return exits
