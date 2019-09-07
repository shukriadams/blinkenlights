class RGBColor():

    value = 0
    mod = 0

    def __init__(self, seed):
        self.mod = seed

    def increment(self):
        if self.value + self.mod > 255 or self.value + self.mod < 0:
            self.mod = self.mod * -1
        
        self.value = self.value + self.mod