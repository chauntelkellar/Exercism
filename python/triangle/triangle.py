def validate(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0


def equilateral(sides):
    if not validate(sides):
        return False

    a, b, c = sides
    return a == b and b == c and a ==c


def isosceles(sides):
    if not validate(sides):
        return False

    a, b, c = sorted(sides)

    # check degenerative triangle
    if a + b <= c:
        return False

    return a == b or b == c


def scalene(sides):
    if not validate(sides):
        return False

    a, b, c = sorted(sides)

    # check degenerative triangle
    if a + b <= c:
        return False

    return a != b and b != c
