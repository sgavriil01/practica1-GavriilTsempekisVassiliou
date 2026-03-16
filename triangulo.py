def checktriangle(a, b, c):
    if (c < a + b) and (b < a + c) and (a < b + c):
        if a == b and a == c:
            return "Equilateral triangle"
        elif a == b or b == c or a == c:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"
    else:
        return "It is not a triangle"