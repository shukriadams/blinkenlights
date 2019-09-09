class RGBColor():

    def __init__(self, speed):
        self._speed = speed
    
    # do not access directly 
    _value = 0
    
    # speed is the amount by which color changes per transition. Minimum should be 1, maximum should be something that's not so close
    # to 255 that a step is not possible
    _speed = 0
  
    # increments the color value, and returns color
    def incrementAndGetValue(self):
        
        # change direction of transition if reach ceiling or floor
        nextValue = self._value + self._speed
        if nextValue > 255 or nextValue < 0:
            self._speed = self._speed * -1
        
        self._value = self._value + self._speed
        return self._value
