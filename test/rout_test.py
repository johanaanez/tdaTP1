from unittest import TestCase

from route.route import Route


class TestRoutes(TestCase):

    # Ruta de ejemplo
    def test_route_covered_by_tree_antennas_with_overlap(self):
        #load file1
        route = Route(500)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 3)

    def test_route_covered_by_only_one_antenna(self):
        #load file1
        route = Route(15)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 1)

    def test_route_is_not_completely_covered_not_enough_antennas(self):
        #load file3
        route = Route(10)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 0)

    def test_route_covered_by_two_antennas_without_overlap(self):
        #load file4
        route = Route(300)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 2)

    def test_route_is_not_completely_covered(self):
        #load file5
        route = Route(100)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 0)

    def test_route_covered_by_three_antennas(self):
        #load file6
        route = Route(200)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 3)

    def test_route_is_not_covered(self):
        #load file6
        route = Route(300)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 0)

    def test_route_is_covered(self):
        #load file7
        route = Route(30)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 1)

    def test_route_is_covered(self):
        #load file8
        route = Route(160)
        result = route.calculateMinAntennas()

        self.assertEqual(result.size, 2)
