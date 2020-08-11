from py2opt.helper import build_dist_matrix, open_file
from py2opt.routefinder import RouteFinder


def test_distance():
    v3 = "dataset.txt"
    cities_coordinates, cities_names, num_cities = open_file(v3)
    distance_matrix = build_dist_matrix(cities_names, cities_coordinates)
    route_finder = RouteFinder(distance_matrix, cities_names)
    best_distance, best_route, best_distances = route_finder.solve()
    assert best_distance < 90000


def test_pypi():
    nodes = ['A', 'B', 'C', 'D']
    dist_mat = [[0, 2, 5, 3], [2, 0, 7, 2], [5, 7, 0, 1], [3, 9, 1, 0]]
    route_finder = RouteFinder(dist_mat, nodes)
    best_distance, best_route, best_distances = route_finder.solve()
    print(best_distance)
    print(best_route)


test_pypi()