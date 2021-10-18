#!/usrbin/python3
"""
Module with definition for class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class contains instantiation of the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This function is the instantiation of the
        square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string representation of square
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))
