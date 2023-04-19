p=print
class AngryBird:
    __slots__ = ['_x', '_y'] # optional memory reserve to work faster
    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            value = 0
        self._x = value
    
   
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        if value < 0:
            value = 0
        self._y = value
    
    def __repr__(self):
        return f"<AngryBird ({self._x}, {self._y})>"

b1 = AngryBird()
b2 = AngryBird(x=1)
# p((b1.get_x(), b1.get_y()))
p((b1.x, b1.y))

b3 = AngryBird(y=18)
b4 = AngryBird(10, 10)
p( b4._x, b4._y)

bird = AngryBird(1, 2)
print(bird)

bird = AngryBird()
bird.x = 12
bird.y = -20 # Won't get set because of the setter method

print(bird.x, bird.y)  #> 12 0