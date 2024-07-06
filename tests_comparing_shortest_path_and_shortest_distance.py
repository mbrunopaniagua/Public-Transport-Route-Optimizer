import unittest
from public_transport_route_optimizer import PublicTransportMap


class TestPublicTransportRouteOptimizer(unittest.TestCase):

    def test_shortest_path_basic_graph_from_A_to_D(self):
        expected_path = ["A", "B", "D"]
        expected_steps = 2

        public_transport_map = PublicTransportMap("basic_graph.json")
        path, steps = public_transport_map.shortest_path("A", "D")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_steps, steps)

    def test_shortest_distance_basic_graph_from_A_to_D(self):
        expected_path = ["A", "B", "C", "D"]
        expected_distance = 6

        public_transport_map = PublicTransportMap("basic_graph.json")
        path, distance = public_transport_map.shortest_distance("A", "D")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)


if __name__ == "__main__":
    unittest.main()
