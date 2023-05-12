
class Item:
    def __init__(self, name: str, description: str) -> None:
        if not name:
            raise ValueError("Missing name")
        if not description:
            raise ValueError("Missing description")

        self.name = name
        self.description = description

    
    def __str__(self) -> str:
        return f"{self.name} - {self.description}"


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description
