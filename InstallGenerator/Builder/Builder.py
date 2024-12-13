class Builder:
    def __init__(self):
        self.data = {}

    def buildPart(self, key, value):
        self.data[key] = value

    def get(self):
        return self.data
