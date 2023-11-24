from abc import ABC, abstractmethod


class Shape(ABC):
    """
        Abstract base class for geometric shapes.
        """

    def __init__(self, name):
        """
        Initialize a shape with a given name.

        Parameters:
        - name (str): The name of the shape.
        """
        self._name = name

    def __str__(self):
        """
        Get a string representation of the shape.

        Returns:
        - str: A string describing the shape.
        """
        return self.draw()

    def get_name(self):
        """
        Get the name of the shape.

        Returns:
        - str: The name of the shape.
        """
        return self._name

    @property
    def name(self):
        """
               Initialize a shape with a given name.

               Parameters:
               - name (str): The name of the shape.
               """
        return self._name

    @abstractmethod
    def area(self):
        """
                Abstract method to calculate the area of the shape.

                This method must be implemented by concrete subclasses.

                Returns:
                - float: The area of the shape.
                """
        pass

    @abstractmethod
    def perimeter(self):
        """
               Abstract method to calculate the perimeter of the shape.

               This method must be implemented by concrete subclasses.

               Returns:
               - float: The perimeter of the shape.
               """
        pass

    def draw(self):
        """
                Get a string representation of the shape.

                Returns:
                - str: A string describing the shape.
                """
        return f"{self._name}, area: {self.area()}, perimeter: {self.perimeter()}"

    def __lt__(self, other):
        """
        Compare two shapes based on their areas.

        Parameters:
        - other (Shape): Another shape to compare.

        Returns:
        - bool: True if the area of this shape is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Check if two shapes have equal areas.

        Parameters:
        - other (Shape): Another shape to compare.

        Returns:
        - bool: True if the areas of both shapes are equal, False otherwise.
        """
        return self.area() == other.area()


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self._radius = radius

    def area(self):
        return 3.141592653589793 * (self._radius ** 2)

    def perimeter(self):
        return 2 * 3.141592653589793 * self._radius


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self._side = side

    def area(self):
        return self._side ** 2

    def perimeter(self):
        return 4 * self._side


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def area(self):
        s = (self._side1 + self._side2 + self._side3) / 2
        return (s * (s - self._side1) * (s - self._side2) * (s - self._side3)) ** 0.5

    def perimeter(self):
        return self._side1 + self._side2 + self._side3


# class ShapeFactory:
#     @staticmethod
#     def create_shape(shape_name, *args):
#         if shape_name == "Circle":
#             return Circle(*args)
#         elif shape_name == "Square":
#             return Square(*args)
#         elif shape_name == "Rectangle":
#             return Rectangle(*args)
#         elif shape_name == "Triangle":
#             return Triangle(*args)
#         else:
#             raise ValueError("Invalid shape name")

class ShapeFactory:
    """
    Factory class for creating instances of geometric shapes.
    """

    @staticmethod
    def create_circle(radius):
        """
        Create a Circle instance.

        Parameters:
        - radius (float): The radius of the circle.

        Returns:
        - Circle: A Circle instance.
        """
        return Circle(radius)

    @staticmethod
    def create_square(side_length):
        """
        Create a Square instance.

        Parameters:
        - side_length (float): The length of a side of the square.

        Returns:
        - Square: A Square instance.
        """
        return Square(side_length)

    @staticmethod
    def create_rectangle(length, width):
        """
        Create a Rectangle instance.

        Parameters:
        - length (float): The length of the rectangle.
        - width (float): The width of the rectangle.

        Returns:
        - Rectangle: A Rectangle instance.
        """
        return Rectangle(length, width)

    @staticmethod
    def create_triangle(side1, side2, side3):
        """
        Create a Triangle instance.

        Parameters:
        - side1 (float): The length of the first side of the triangle.
        - side2 (float): The length of the second side of the triangle.
        - side3 (float): The length of the third side of the triangle.

        Returns:
        - Triangle: A Triangle instance.
        """
        return Triangle(side1, side2, side3)



class DrawingProgram:

    def __init__(self, shapes=None):
        """
                Initialize a DrawingProgram with a list of shapes.

                Parameters:
                - shapes (list): A list of Shape objects.
                """
        self.shapes = shapes if shapes else []

    def __iter__(self):
        """
                Get an iterator for the DrawingProgram.

                Returns:
                - iter: An iterator for the DrawingProgram.
                """
        return iter(self.shapes)

    def add_shape(self, shape):
        """
               Add a shape to the DrawingProgram.

               Parameters:
               - shape (Shape): The shape to add.
               """
        self.shapes.append(shape)

    def remove_shape(self, shape):
        """
               Remove a shape from the DrawingProgram.

               Parameters:
               - shape (Shape): The shape to remove.

               Returns:
               - int: The number of occurrences of the shape removed.
               """
        count_removed = 0
        self.shapes = [s for s in self.shapes if s != shape]
        count_removed = len(self.shapes) - count_removed
        return count_removed

    def print_shape(self, shape):
        """
               Print occurrences of a specific shape in the DrawingProgram.

               Parameters:
               - shape (Shape): The shape to print.
               """
        matching_shapes = [str(s) for s in self.shapes if s.name == shape.name]
        print('\n'.join(matching_shapes))

    def sort_shapes(self):
        """
                Sort the shapes in the DrawingProgram based on name and area.
                """
        self.shapes = sorted(self.shapes, key=lambda x: (x.name, x.area()))

    def __str__(self):
        """
                Get a string representation of the DrawingProgram.

                Returns:
                - str: A string describing the DrawingProgram.
                """
        return '\n'.join(str(shape) for shape in self.shapes)

    def get_shape(self, index):
        """
                Get a shape at a specific index in the DrawingProgram.

                Parameters:
                - index (int): The index of the shape.

                Returns:
                - Shape or None: The shape at the specified index, or None if the index is out of range.
                """
        if 0 <= index < len(self.shapes):
            return self.shapes[index]
        return None

    def set_shape(self, index, shape):
        """
                Set a shape at a specific index in the DrawingProgram.

                Parameters:
                - index (int): The index to set the shape at.
                - shape (Shape): The shape to set.

                Notes:
                If the index is out of range, this method does nothing.
                """
        if 0 <= index < len(self.shapes):
            self.shapes[index] = shape


class DrawingProgramIterator:
    """
          Initialize an iterator for the DrawingProgram.

          Parameters:
          - drawing_program (DrawingProgram): The DrawingProgram to iterate over.
          """
    def __init__(self, drawing_program):
        """
       Initialize an iterator for the DrawingProgram.

       Parameters:
       - drawing_program (DrawingProgram): The DrawingProgram to iterate over.
       """
        self._drawing_program = drawing_program
        self._index = 0

    def __iter__(self):
        """
        Get the iterator object.
        """
        return self

    def __next__(self):
        """
       Get the next shape in the iteration.

       Returns:
       - Shape: The next shape.

       Raises:
       - StopIteration: If the end of the iteration is reached.
       """
        if self._index < len(self._drawing_program.shapes):
            result = self._drawing_program.shapes[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


class DrawingProgramMain:
    """
    Run the main logic of the DrawingProgram.

    This method demonstrates the usage of the DrawingProgram and related classes.
    """
    @staticmethod
    def run():
        # Create a DrawingProgram
        drawing_program = DrawingProgram()

        # Add shapes to the DrawingProgram
        circle = ShapeFactory.create_circle(2.0)
        square = ShapeFactory.create_square(3.0)
        drawing_program.add_shape(circle)
        drawing_program.add_shape(square)

        # Print the original DrawingProgram
        print("Original DrawingProgram:")
        for shape in drawing_program:
            print(shape)

        # Sort the shapes in the DrawingProgram
        drawing_program.sort_shapes()

        # Print the DrawingProgram after sorting
        print("\nDrawingProgram after sorting:")
        for shape in drawing_program:
            print(shape)

        # Add more shapes to the DrawingProgram
        rectangle = ShapeFactory.create_rectangle(2.0, 4.0)
        triangle = ShapeFactory.create_triangle(3.0, 4.0, 5.0)
        drawing_program.add_shape(rectangle)
        drawing_program.add_shape(triangle)

        # Replace a shape in the DrawingProgram
        new_square = ShapeFactory.create_square(5.0)
        drawing_program.set_shape(1, new_square)


        # Sort the shapes again
        drawing_program.sort_shapes()

        # Print the DrawingProgram after additional shapes and replacement
        print("\nDrawingProgram after adding, replacing, and sorting:")
        for shape in drawing_program:
            print(shape)


# Example usage:
# drawing_program = DrawingProgram()
# shape1 = ShapeFactory.create_shape("Circle", 2.0)
# shape2 = ShapeFactory.create_shape("Square", 3.0)
# shape3 = ShapeFactory.create_shape("Rectangle", 2.0, 4.0)
# shape4 = ShapeFactory.create_shape("Triangle", 3.0, 4.0, 5.0)
# drawing_program.add_shape(shape1)
# drawing_program.add_shape(shape2)
# drawing_program.add_shape(shape3)
# drawing_program.add_shape(shape4)

# circle = ShapeFactory.create_circle(2.0)
# square = ShapeFactory.create_square(3.0)
# rectangle = ShapeFactory.create_rectangle(2.0, 4.0)
# triangle = ShapeFactory.create_triangle(3.0, 4.0, 5.0)
# drawing_program.add_shape(circle)
# drawing_program.add_shape(square)
# drawing_program.add_shape(rectangle)
# drawing_program.add_shape(triangle)
#
# print("Original DrawingProgram:")
# print(drawing_program)
#
# print("\nDrawingProgram after sorting:")
# drawing_program.sort_shapes()
# print(drawing_program)
#
# print("\nDrawingProgramIterator:")
# for shape in drawing_program:
#     print(shape)

if __name__ == "__main__":
    DrawingProgramMain.run()
