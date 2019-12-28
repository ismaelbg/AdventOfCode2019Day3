import csv


directions = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}


def calculate_points(path):
    current_point = (0,0)
    visited_points = []
    for subpath in path:
        direction = subpath[0]
        for _ in range(int(subpath[1:])):
            current_point = tuple(map(lambda x, y: x + y, current_point, directions[direction]))
            visited_points.append(current_point)
    return visited_points


def calculate_steps_to_intersections(path, intersection_points, length_until_inters_points):
    current_point = (0,0)
    counter = 0
    for subpath in path:
        direction = subpath[0]
        for _ in range(int(subpath[1:])):
            current_point = tuple(map(lambda x, y: x + y, current_point, directions[direction]))
            counter = counter + 1
            if current_point in intersection_points:
                length_until_inters_points[current_point] = length_until_inters_points[current_point] + counter


with open("inputExercise3", 'r') as f:
    paths = list(csv.reader(f))

visited_points_wire1 = calculate_points(paths[0])
visited_points_wire2 = calculate_points(paths[1])

intersection_points = list(set(visited_points_wire1).intersection(set(visited_points_wire2)))
length_until_intersection_points = {i : 0 for i in intersection_points}

calculate_steps_to_intersections(paths[0], intersection_points, length_until_intersection_points)
calculate_steps_to_intersections(paths[1], intersection_points, length_until_intersection_points)

print("Result 1:", min([abs(point[0]) + abs(point[1]) for point in intersection_points]))
print("Result 2:", min(length_until_intersection_points.values()))

