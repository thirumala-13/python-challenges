import math


class Shape:
    """
    TODO:
    Base class for all shapes. Defines the interface that all shapes must follow.

    The __init__ stores the color.
    The area() and perimeter() methods raise NotImplementedError —
    they MUST be overridden in subclasses.
    The describe() method uses area() and the class name to return a description.
    """

    def __init__(self, color):
        """
        TODO: Store color as self.color
        """
        self.color = color


    def area(self):
        """
        TODO: Raise NotImplementedError.
        This forces subclasses to provide their own implementation.

        raise NotImplementedError("Subclasses must implement area()")
        """
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        """
        TODO: Raise NotImplementedError.
        """
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        """
        TODO:
        Return a string describing the shape.
        Format: "A {color} {ClassName} with area {area:.2f}"

        Example:
            circle = Circle("red", 5)
            circle.describe()  → "A red Circle with area 78.54"

        Hint:
            f"A {self.color} {type(self).__name__} with area {self.area():.2f}"
        """
        return f"A {self.color} {type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):
    """
    TODO:
    A circle shape.

    __init__(color, radius):
        Call super().__init__(color) to set the color.
        Store self.radius = radius.

    area(): π × r²  →  math.pi * self.radius ** 2
    perimeter(): 2 × π × r  →  2 * math.pi * self.radius
    """

    def __init__(self, color, radius):
        # TODO: Call super().__init__(color), then store self.radius = radius
        super().__init__(color)
        self.radius = radius

    def area(self):
        # TODO: Return math.pi * self.radius ** 2
        return math.pi * self.radius ** 2       
    

    def perimeter(self):
        # TODO: Return 2 * math.pi * self.radius
        return 2 * math.pi * self.radius    


class Rectangle(Shape):
    """
    TODO:
    A rectangle shape.

    __init__(color, width, height):
        Call super().__init__(color).
        Store self.width and self.height.

    area(): width × height
    perimeter(): 2 × (width + height)
    """

    def __init__(self, color, width, height):
        # TODO: Call super().__init__(color), store width and height
        super().__init__(color)
        self.width = width
        self.height = height


    def area(self):
        # TODO: Return self.width * self.height
        return self.width * self.height

    def perimeter(self):
        # TODO: Return 2 * (self.width + self.height)
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """
    TODO:
    A triangle shape defined by three side lengths a, b, c.

    __init__(color, a, b, c):
        Call super().__init__(color).
        Store self.a, self.b, self.c.

    area(): Use Heron's formula:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    perimeter(): a + b + c
    """

    def __init__(self, color, a, b, c):
        # TODO: Call super().__init__(color), store self.a, self.b, self.c
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # TODO: Implement Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))     

    def perimeter(self):
        # TODO: Return self.a + self.b + self.c
        return self.a + self.b + self.c
