
class Command:
    def __init__(self, first_word: str, second_word: str) -> None:
        self.command_word = first_word
        self.second_word = second_word

    @property
    def command_word(self) -> str:
        return self._command_word

    @command_word.setter
    def command_word(self, command_word: str) -> None:
        self._command_word = command_word

    @property
    def second_word(self) -> str:
        return self._second_word

    @second_word.setter
    def second_word(self, second_word: str) -> None:
        self._second_word = second_word

    def isUnknown(self) -> bool:
        return self.command_word is None

    def hasSecondWord(self) -> bool:
        return self.second_word is not None
