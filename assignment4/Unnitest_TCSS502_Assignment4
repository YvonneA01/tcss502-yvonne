import unittest
from assignment4 import Circle, Square, Rectangle, Triangle, DrawingProgram, ShapeFactory


class TestDrawingProgram(unittest.TestCase):
    def test_add_remove_shape(self):
        drawing_program = DrawingProgram()
        circle = Circle(radius=2.0)
        square = Square(side=3.0)

        # Test adding shapes
        drawing_program.add_shape(circle)
        self.assertEqual(len(drawing_program.shapes), 1)
        self.assertIn(circle, drawing_program.shapes)

        # Test removing shapes
        removed_count = drawing_program.remove_shape(circle)
        self.assertEqual(removed_count, 1)
        self.assertEqual(len(drawing_program.shapes), 0)

        def test_sort_shapes_empty_list(self):
            # Test sorting an empty list of shapes
            drawing_program = DrawingProgram()
            drawing_program.sort_shapes()
            self.assertEqual(len(drawing_program.shapes), 0)

        def test_sort_shapes_one_shape(self):
            # Test sorting a list with one shape
            drawing_program = DrawingProgram()
            circle = Circle(radius=2.0)
            drawing_program.add_shape(circle)
            drawing_program.sort_shapes()
            self.assertEqual(len(drawing_program.shapes), 1)

        def test_sort_shapes_ascending_order(self):
            # Test sorting multiple shapes in ascending order
            drawing_program = DrawingProgram()
            circle = Circle(radius=2.0)
            square = Square(side=3.0)
            rectangle = Rectangle(length=4.0, width=2.0)

            drawing_program.add_shape(square)
            drawing_program.add_shape(circle)
            drawing_program.add_shape(rectangle)

            drawing_program.sort_shapes()
            sorted_shapes = list(map(str, drawing_program.shapes))
            expected_order = ["Circle, area: 12.566370614359172, perimeter: 12.566370614359172",
                              "Rectangle, area: 8.0, perimeter: 12.0",
                              "Square, area: 9.0, perimeter: 12.0"]
            self.assertEqual(sorted_shapes, expected_order)

            # Test sorting in descending order
            drawing_program.sort_shapes()
            sorted_shapes_desc = list(map(str, drawing_program.shapes))
            expected_order_desc = ["Square, area: 9.0, perimeter: 12.0",
                                   "Circle, area: 12.566370614359172, perimeter: 12.566370614359172"]
            self.assertEqual(sorted_shapes_desc, expected_order_desc)

            # Test sorting with random order
            drawing_program.add_shape(Rectangle(length=4.0, width=2.0))
            drawing_program.sort_shapes()
            self.assertEqual(len(drawing_program.shapes), 3)

    if __name__ == '__main__':
        unittest.main()

    def test_add_remove_shape(self):
        drawing_program = DrawingProgram()
        circle = Circle(radius=2.0)
        square = Square(side=3.0)

        drawing_program.add_shape(circle)
        drawing_program.add_shape(square)

        self.assertEqual(len(drawing_program.shapes), 2)
        self.assertEqual(drawing_program.remove_shape(circle), 1)
        self.assertEqual(len(drawing_program.shapes), 1)

    def test_sort_shapes(self):
        drawing_program = DrawingProgram()
        circle = Circle(radius=2.0)
        square = Square(side=3.0)

        drawing_program.add_shape(square)
        drawing_program.add_shape(circle)

        drawing_program.sort_shapes()
        sorted_shapes = list(map(str, drawing_program.shapes))
        expected_order = [
            "Circle, area: 12.566370614359172, perimeter: 12.566370614359172",
            "Square, area: 9.0, perimeter: 12.0"
        ]

        # Extracting string representations from the shapes for comparison
        sorted_shape_strings = [str(shape) for shape in drawing_program.shapes]

        self.assertEqual(sorted_shape_strings, expected_order)


class TestDrawingProgramIterator(unittest.TestCase):
    def test_iterator_empty_list(self):
        # Test iterator with a DrawingProgram that has no shapes
        drawing_program = DrawingProgram()
        for shape in drawing_program:
            self.fail("Should not iterate over an empty list of shapes")

    def test_iterator_one_shape(self):
        # Test iterator with a DrawingProgram that has one shape
        drawing_program = DrawingProgram()
        circle = Circle(radius=2.0)
        drawing_program.add_shape(circle)

        shapes_iterated = [shape for shape in drawing_program]
        self.assertEqual(len(shapes_iterated), 1)
        self.assertEqual(shapes_iterated[0], circle)

    def test_iterator_multiple_shapes(self):
        # Test iterator with a DrawingProgram that has 5 shapes
        drawing_program = DrawingProgram()
        circle = Circle(radius=2.0)
        square = Square(side=3.0)
        rectangle = Rectangle(length=4.0, width=2.0)

        drawing_program.add_shape(square)
        drawing_program.add_shape(circle)
        drawing_program.add_shape(rectangle)

        shapes_iterated = [shape for shape in drawing_program]
        self.assertEqual(len(shapes_iterated), 3)
        self.assertIn(circle, shapes_iterated)
        self.assertIn(square, shapes_iterated)
        self.assertIn(rectangle, shapes_iterated)

    # Add more tests for other scenarios


class TestShapeFunctionality(unittest.TestCase):

    def test_circle_area_perimeter(self):
        circle = Circle(5.0)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)
        self.assertAlmostEqual(circle.perimeter(), 31.42, places=2)

    def test_square_area_perimeter(self):
        square = Square(4.0)
        self.assertEqual(square.area(), 16.0)
        self.assertEqual(square.perimeter(), 16.0)

    def test_rectangle_area_perimeter(self):
        rectangle = Rectangle(3.0, 5.0)
        self.assertEqual(rectangle.area(), 15.0)
        self.assertEqual(rectangle.perimeter(), 16.0)

    def test_triangle_area_perimeter(self):
        triangle = Triangle(3.0, 4.0, 5.0)
        self.assertEqual(triangle.area(), 6.0)
        self.assertEqual(triangle.perimeter(), 12.0)

    def test_shape_name(self):
        circle = Circle(5.0)
        square = Square(4.0)
        rectangle = Rectangle(3.0, 5.0)
        triangle = Triangle(3.0, 4.0, 5.0)

        self.assertEqual(circle.name, "Circle")
        self.assertEqual(square.name, "Square")
        self.assertEqual(rectangle.name, "Rectangle")
        self.assertEqual(triangle.name, "Triangle")


class TestShapeFactoryFunctionality(unittest.TestCase):
    def test_create_circle(self):
        shape_factory = ShapeFactory()
        circle = shape_factory.create_circle(5.0)
        self.assertIsInstance(circle, Circle)
        self.assertEqual(circle.name, "Circle")
        self.assertAlmostEqual(circle.area(), 78.54, places=2)
        self.assertAlmostEqual(circle.perimeter(), 31.42, places=2)

    def test_create_square(self):
        shape_factory = ShapeFactory()
        square = shape_factory.create_square(4.0)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.name, "Square")
        self.assertEqual(square.area(), 16.0)
        self.assertEqual(square.perimeter(), 16.0)

    def test_create_rectangle(self):
        shape_factory = ShapeFactory()
        rectangle = shape_factory.create_rectangle(3.0, 5.0)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.name, "Rectangle")
        self.assertEqual(rectangle.area(), 15.0)
        self.assertEqual(rectangle.perimeter(), 16.0)

    def test_create_triangle(self):
        shape_factory = ShapeFactory()
        triangle = shape_factory.create_triangle(3.0, 4.0, 5.0)
        self.assertIsInstance(triangle, Triangle)
        self.assertEqual(triangle.name, "Triangle")
        self.assertEqual(triangle.area(), 6.0)
        self.assertEqual(triangle.perimeter(), 12.0)


if __name__ == '__main__':
    unittest.main()
