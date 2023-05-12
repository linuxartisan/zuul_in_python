from Item import Item

class Exit:
    def __init__(self, direction :str, neighbor, locked :bool, opens_with :Item):
        self.direction = direction
        self.neighbor = neighbor
        self.locked = locked
        self.opens_with = opens_with

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @property
    def neighbor(self):
        return self._neighbor

    @neighbor.setter
    def neighbor(self, neighbor):
        self._neighbor = neighbor

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, locked):
        self._locked = locked

    @property
    def opens_with(self):
        return self._opens_with

    @opens_with.setter
    def opens_with(self, opens_with):
        self._opens_with = opens_with
