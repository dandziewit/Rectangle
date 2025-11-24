"""
Rectangle Calculator - simple console program for class lab
"""

class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = int(height)
        self.width = int(width)

    def perimeter(self) -> int:
        return 2 * (self.height + self.width)

    def area(self) -> int:
        return self.height * self.width

    def draw(self) -> None:
        h = self.height
        w = self.width
        if h <= 0 or w <= 0:
            print("(nothing to draw)")
            return
        if h == 1:
            print(('* ' * w).rstrip())
            return
        if w == 1:
            for _ in range(h):
                print('*')
            return
        print(('* ' * w).rstrip())
        for _ in range(h - 2):
            interior = '  ' * (w - 2)
            print('* ' + interior + '*')
        print(('* ' * w).rstrip())


def get_positive_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v <= 0:
                print('Please enter a positive integer.')
                continue
            return v
        except ValueError:
            print('Please enter an integer value (e.g. 5).')


def main():
    while True:
        print('\nRectangle Calculator\n')
        height = get_positive_int('Height: ')
        width = get_positive_int('Width: ')

        rect = Rectangle(height, width)

        print(f'Perimeter: {rect.perimeter()}')
        print(f'Area: {rect.area()}')
        print()
        rect.draw()
        print()

        choice = input('Continue? (y/n): ').strip().lower()
        if choice != 'y':
            break


if __name__ == '__main__':
    main()
