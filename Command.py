
class Command:
    def __init__(self, first_word, second_word) -> None:
        self.command_word = first_word
        self.second_word = second_word

    @property
    def command_word(self):
        return self._command_word

    @command_word.setter
    def command_word(self, command_word):
        self._command_word = command_word

    @property
    def second_word(self):
        return self._second_word

    @second_word.setter
    def second_word(self, second_word):
        self._second_word = second_word

    def isUnknown(self):
        return self.command_word is None

    def hasSecondWord(self):
        return self.second_word is not None
