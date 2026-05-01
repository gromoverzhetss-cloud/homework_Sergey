import math
def square(side):
    return math.ceil(side * side)
nam_side = int(input("Сторона:"))
print(f"Площадь равна: {square(nam_side)}")

