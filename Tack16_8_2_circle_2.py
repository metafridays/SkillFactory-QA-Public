from Task16_8_2_circle import Rectangle, Square, Circle

#   Create two rectangles

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

#   Print square of two rectangles

print(rect_1.get_area())
print(rect_2.get_area())

#   Create two squares

square_1 = Square(5)
square_2 = Square(10)

#   Print square of two Squares

print(square_1.get_area_square(),
      square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circle_1 = Circle(3)
circle_2 = Circle(7)
print("Circle area:")
print(circle_1.get_area_circle(), circle_2.get_area_circle())