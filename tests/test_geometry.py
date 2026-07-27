from nakshpy.geometry import Point, Line

def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    assert p1.distance_to(p2) == 5


def test_line_length():
    line = Line(Point(0, 0), Point(3, 4))

    assert line.length() == 5
