import unittest
import circle as c
import pytest


class TestCircle(unittest.TestCase):
    def test_radius(self):
        """Test that the radium attribute is correct"""
        new_circle = c.Circle(4)  #create instance of circle with radius 4

        self.assertEqual(new_circle.radius, 4)

    def test_diameter(self):
        """Test that the diameter attribute is callable"""
        new_circle = c.Circle(4)

        self.assertEqual(new_circle.diameter, 8)

    def test_setter_dia(self):
        """Test the set method on diameter"""
        new_circle = c.Circle(4)
        new_circle.diameter = 3
        self.assertEqual(new_circle.diameter, 3)

    def test_setter_radius(self):
        """Test the set method on radius"""
        new_circle = c.Circle(4)
        new_circle.radius = 3
        self.assertEqual(new_circle.radius, 3)

    def test_diameter_to_radius(self):
        """Test that when the diameter is set, the radius is also updated"""
        new_circle = c.Circle(4)
        new_circle.diameter = 3
        self.assertEqual(new_circle.radius, 1.5)

    def test_radius_to_diameter(self):
        """Test that when the radius is set, the diameter is also updated"""
        new_circle = c.Circle(4)
        new_circle.radius = 100
        self.assertEqual(new_circle.diameter, 200)

    def test_area(self):
        """Test the area property"""
        new_circle = c.Circle(4)
        area = "{:.2f}".format(new_circle.area)
        self.assertEqual(area, '25.13')

    def test_set_area(self):
        """Test that the user cannot set the area. Raises a Valueerror"""
        new_circle = c.Circle(4)
        with self.assertRaises(ValueError):
            new_circle.area = 10

    def test_area_Radius_update(self):
        """Test the area is updated when the radius is updated"""
        new_circle = c.Circle(4)
        new_circle.radius = 10
        area = "{:.2f}".format(new_circle.area)
        self.assertEqual(area, '62.83')

    def test_area_diameter_update(self):
        """Test the area is updated when the diameter is updated"""
        new_circle = c.Circle(4)
        new_circle.diameter = 1
        area = "{:.2f}".format(new_circle.area)
        self.assertEqual(area, '3.14')

    def test_diameter_constructor(self):
        """Test that you can create a Circle instance with a diameter"""
        new_circle = c.Circle.from_diameter(50)
        self.assertEqual(new_circle.radius, 25)

    def test_string_method(self):
        """Test the string method, returns 'Circle with radius: 4.0000"""
        new_circle = c.Circle(4)
        expected_text ='Circle with radius: 4.0000'
        self.assertEqual(new_circle.__str__(), expected_text)


    def test_repr_method(self):
        """Test the string method, returns 'Circle with radius: 4.0000"""
        new_circle = c.Circle(4)
        expected_text ='Circle(4)'
        self.assertEqual(new_circle.__repr__(), expected_text)