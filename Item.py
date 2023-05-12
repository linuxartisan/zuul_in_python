
class Item:
    def __init__(self, name, description):
        if not name:
            raise ValueError("Missing name")
        if not description:
            raise ValueError("Missing description")

        self.name = name
        self.description = description

    
    def __str__(self) -> str:
        return f"{self.name} - {self.description}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
