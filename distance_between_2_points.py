def distance_between_points(a, b):
    a_x, a_y, b_x, b_y = a[0], a[1], b[0], b[1]
    distance = ((b_x - a_x)**2 + (b_y - a_y)**2) ** 0.5
    return distance

print(distance_between_points((1,6), (4,2)))

