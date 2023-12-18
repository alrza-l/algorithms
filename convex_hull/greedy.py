class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(current, next, r):
    val = (next.y - current.y) * (r.x - next.x) - (next.x - current.x) * (r.y - next.y)
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def convexHull(points, n):
    if n < 3:
        return

    hull = []

    left_most = 0
    for i in range(1, n):
        if points[i].x < points[left_most].x:
            left_most = i

    current = left_most
    next = 0
    while True:
        hull.append(points[current])

        next = (current + 1) % n
        for i in range(n):
            if orientation(points[current], points[i], points[next]) == -1:
                next = i

        current = next

        if current == left_most:
            break

    for point in hull:
        print("(", point.x, ",", point.y, ")")


points = [
    Point(0, 3),
    Point(2, 3),
    Point(1, 1),
    Point(2, 1),
    Point(3, 0),
    Point(0, 0),
    Point(3, 3),
]
n = len(points)
convexHull(points, n)
