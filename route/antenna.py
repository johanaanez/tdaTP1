class Antenna:

    def __init__(self, id, location, radius):
        self.id = id
        self.start = location - radius
        self.end = location + radius
