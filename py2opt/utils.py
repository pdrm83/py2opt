import numpy as np
from math import sin, cos, sqrt, atan2, radians


class GeographicalPositionTest:
    def __init__(self, file_name):
        self.file_name = file_name

    def build_dist_matrix(self, cities_names, cities_coordinates):
        """
        This function creates a matrix containing pair distance among all cities in kilometers. Distance between each
        city by itself is equal to zero.
        """
        num_cities = len(cities_names)
        distance_matrix = np.zeros([num_cities, num_cities])
        for city_departure in cities_names:
            for city_arrival in cities_names:
                i = cities_names.index(city_departure)
                j = cities_names.index(city_arrival)
                co_i = cities_coordinates[city_departure]
                co_j = cities_coordinates[city_arrival]
                distance_matrix[i][j] = self.calculate_pair_dist(co_i, co_j)
        return distance_matrix

    def open_file(self):
        city_names = []
        cities_coordinates = {}
        with open(self.file_name, "r") as file_stream:
            num_line = 0
            for line in file_stream:
                num_line += 1
                current_line = line.split(",")
                if self.is_valid(current_line):
                    city_name = current_line[0]
                    city_latitude = float(
                        "{0:.2f}".format(float(current_line[1]) + float(current_line[2]) / 60))
                    city_longitude = float(
                        "{0:.2f}".format(float(current_line[3]) + float(current_line[4]) / 60))

                    cities_coordinates[city_name] = [city_latitude, city_longitude]
                    city_names.append(city_name)
                else:
                    print('This line', num_line, 'does not pass our test.')

            num_cities = len(city_names)

        return cities_coordinates, city_names, num_cities

    @staticmethod
    def calculate_pair_dist(coordinates_1, coordinates_2):
        """
        This function calculates distance between two cities in kilometers given geographical coordinates of two cities.
        """
        latitude_first, longitude_first = coordinates_1
        latitude_second, longitude_second = coordinates_2

        r = 6373.0
        a = (sin(radians(latitude_second - latitude_first) / 2)) ** 2 + \
            cos(radians(latitude_first)) * cos(radians(latitude_second)) * \
            (sin(radians(longitude_second - longitude_first) / 2)) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance_kilometer = float("{0:.2f}".format(r * c))

        return distance_kilometer

    @staticmethod
    def is_valid(line):
        """
        This boolean function check each line in the imported file to have exact 5 components. Moreover, it checks
        whether latitude and longitude degrees are between -180 and 180, and its corresponding minutes are between
        0 and 60.
        """
        if len(line) == 5:
            latitude_degree = float(line[1])
            latitude_minute = float(line[2])
            longitude_degree = float(line[3])
            longitude_minute = float(line[4])

            if -180 <= latitude_degree <= 180 and 0 <= latitude_minute <= 60 and \
                    -180 <= longitude_degree <= 180 and 0 <= longitude_minute <= 60:
                return True
        else:
            return False
