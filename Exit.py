from Item import Item

class Exit:
    def __init__(self, direction: str, neighboringRoom, locked: bool, opens_with: Item) -> None:
        self.direction = direction
        self.neighboringRoom = neighboringRoom # neighboring Room object
        self.locked = locked
        self.opens_with = opens_with

    @property
    def direction(self) -> str:
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        self._direction = direction

    @property
    def neighboringRoom(self):
        return self._neighboringRoom

    @neighboringRoom.setter
    def neighboringRoom(self, neighboringRoom) -> None:
        self._neighboringRoom = neighboringRoom

    @property
    def locked(self) -> bool:
        return self._locked

    @locked.setter
    def locked(self, locked: bool) -> None:
        self._locked = locked

    @property
    def opens_with(self) -> Item:
        return self._opens_with

    @opens_with.setter
    def opens_with(self, opens_with: Item) -> None:
        self._opens_with = opens_with
