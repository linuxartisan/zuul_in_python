import re
from Command import Command
from CommandWords import CommandWords

class Parser:
    def getCommand(self):
        inputLine = input("> ")

        result = re.split(r"\s", inputLine, maxsplit=2)
        word1 = None
        word2 = None
        if len(result) >= 1:
            word1 = result[0]
            if len(result) >= 2:
                word2 = result[1]

        if word1 is None or not CommandWords.isCommand(word1):
            return None

        return Command(word1, word2)
