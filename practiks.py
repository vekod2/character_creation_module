from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
        'квадратного корня из заданного числа'

print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number) -> str:
    
    if your_number <= 0:
        return sqrt(your_number)

    print(f"Мы вычислили квадратный корень из введённого вами числа.\
           Это будет: {CalculateSquareRoot(your_number)}")


calc(your_number=120)
