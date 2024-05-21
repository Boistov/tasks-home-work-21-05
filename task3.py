class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_a(self):
        return 3.14 * self.radius ** 2

    def calculate_num(self):
        return 2 * 3.14 * self.radius

radius = float(input("enter"))
circle = Circle(radius)
area = circle.calculate_a()
perimeter = circle.calculate_num()

print(area)
print(perimeter)
22
