from unittest import TestCase

from route.route import Route


class TestRoutes(TestCase):

    # Ruta de ejemplo
    def test_route_covered_by_tree_antennas_with_overlap(self):
        route = Route(550)
        file = './resources/route1.txt'
        route.add_antennas(file)
        result = route.calculate_minimun_antennas()

        self.assertEqual(len(result), 3)

    def test_route_covered_by_only_one_antenna(self):
        route = Route(15)
        file = './resources/route2.txt'
        route.add_antennas(file)
        result = route.calculate_minimun_antennas()

        self.assertEqual(len(result), 1)

    def test_route_is_not_completely_covered_not_enough_antennas(self):
        route = Route(100)
        file = './resources/route3.txt'
        route.add_antennas(file)
        result = route.calculate_minimun_antennas()

        self.assertEqual(len(result), 0)

    def test_route_covered_by_two_antennas_without_overlap(self):
        route = Route(300)
        file = './resources/route4.txt'
        route.add_antennas(file)
        result = route.calculate_minimun_antennas()

        self.assertEqual(2, len(result))


