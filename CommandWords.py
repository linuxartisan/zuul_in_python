
class CommandWords:
    validCommands = ("go", "quit", "help", "take", "inventory", "drop", "use", "look")

    @classmethod
    def showAll(cls):
        print(cls.validCommands)

    @classmethod
    def isCommand(cls, command):
        return command in cls.validCommands
