import os

from py2opt.constants import TEST_DIR
from py2opt.routefinder import RouteFinder
from py2opt.utils import GeographicalPositionTest


def test_gpt():
    gpt = GeographicalPositionTest(file_name=os.path.join(TEST_DIR, 'dataset.txt'))
    cities_coordinates, cities_names, num_cities = gpt.open_file()
    distance_matrix = gpt.build_dist_matrix(cities_names, cities_coordinates)
    route_finder = RouteFinder(distance_matrix, cities_names)
    best_distance, best_route = route_finder.solve()
    assert best_distance < 90000


def test_smoke():
    cities_names = ['A', 'B', 'C', 'D']
    dist_mat = [[0, 29, 15, 35], [29, 0, 57, 42], [15, 57, 0, 61], [35, 42, 61, 0]]
    route_finder = RouteFinder(dist_mat, cities_names, iterations=10, verbose=True)
    best_distance, best_route = route_finder.solve()
    assert best_distance == 114

def test_return_to_begin():
    cities_names = ['A', 'B', 'C', 'D']
    dist_mat = [[0, 29, 15, 35], [29, 0, 57, 42], [15, 57, 0, 61], [35, 42, 61, 0]]
    route_finder = RouteFinder(dist_mat, cities_names, iterations=10, return_to_begin=True, verbose=False)
    best_distance_1, _ = route_finder.solve()
    route_finder = RouteFinder(dist_mat, cities_names, iterations=10, return_to_begin=False, verbose=False)
    best_distance_2, _ = route_finder.solve()
    assert best_distance_1 > best_distance_2
