class RGBColor():
    
    # do not access directly 
    _value = 0
    
    # speed is the amount by which color changes per transition. Minimum should be 1, maximum should be something that's not so close
    # to 255 that a step is not possible
    _speed = 0

    # maximum value of light. normally 255, but can be capped to suppress a particular color
    _ceiling = 0


    def __init__(self, speed, ceiling = 255):
        self._speed = speed
        self._ceiling = ceiling


    # increments the color value, and returns color
    def incrementAndGetValue(self):
        
        # change direction of transition if ceiling or floor reached
        nextValue = self._value + self._speed
        if nextValue > self._ceiling or nextValue < 0:
            self._speed = self._speed * -1
        
        self._value = self._value + self._speed
        return self._value
