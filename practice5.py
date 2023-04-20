# Triangle with Inheritance
# 
# Build off your RegularPolygon class and create another class called Triangle. The Triangle class should have functionality that calculates both the perimeter and the area of the triangle. The calculated values for both the perimeter and area should be assigned to respective instance properties on the Triangle class.

# The area of a triangle can be calculated with Heron's formula: √(s(s-a)(s-b)(s-c)), where s is the semi-perimeter of the triangle. The semi-perimeter is the perimeter divided by 2. The square root function sqrt() can be imported from the built-in math package.

# Write your class here.
from math import sqrt


class RegularPolygon:
  def __init__(self, _sides, _length):
    _type = 'Polygon'
    if _sides < 3: raise Exception('A polygon must have at least 3 sides.')
    else: 
      self._sides = _sides
      self._length = _length

  @property
  def num_sides(self):
    return self._sides
  
  @property
  def length(self):
    return self._length    

  @property
  def type(self):
    return self._type    

  def identify_polygon(self):
    if self._sides == 3 : self._type = 'Triangle'
    if self._sides == 4 : self._type = 'Quadrilateral'
    if self._sides == 5 : self._type = 'Pentagon'
    if self._sides == 6 : self._type = 'Hexagon'
    if self._sides == 7 : self._type = 'Heptagon'
    if self._sides == 8 : self._type = 'Octagon'
    if self._sides == 9 : self._type = 'Nonagon'
    if self._sides == 10: self._type = 'Decagon'
    if self._sides >= 10: self._type = f'Polygon with {self._sides} sides'

  @classmethod
  def polygon_factory(cls, lst_tup):
    return [cls(sides, len) for sides, len in lst_tup ]

  @staticmethod
  def get_perimeter(polygon):
    return polygon.num_sides*polygon.length  

  def __repr__(self):
        return f"<Polygon ({self._sides}, {self._length})>"


class Triangle(RegularPolygon):
  def __init__(self, _sides, _length):    
    super().__init__(_sides, _length)
    if self._sides != 3:
      raise Exception('A triangle must have exactly three sides')
      
  
  @property
  def perimeter(self):
    return self._sides * self._length

  @property
  def area(self):
    a = b = c = self._length
    s = self.perimeter / 2
    print(a,b,c,s)
    return sqrt(s*(s-a)*(s-b)*(s-c))
    

triangle_a = Triangle(3, 3)
print(triangle_a.perimeter) # 9
print(triangle_a.area) # 3.8971...

triangle_b = Triangle(3, 12)
print(triangle_b.perimeter) # 36
print(triangle_b.area) # 62.3538...

try:
  triangle_c = Triangle(4, 12)
  print(triangle_c.perimeter) # Exception: A triangle must have exactly three sides
except Exception as e:
  print(repr(e))