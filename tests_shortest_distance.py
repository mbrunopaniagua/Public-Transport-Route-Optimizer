import unittest
from public_transport_route_optimizer import PublicTransportMap


class TestPublicTransportRouteOptimizerShortestDistance(unittest.TestCase):

    def test_shortest_distance_simple_graph_from_A_to_B(self):
        expected_path = ["A", "D", "E", "G"]
        expected_distance = 11

        public_transport_map = PublicTransportMap("simple_graph.json")
        path, distance = public_transport_map.shortest_distance("A", "G")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_distance_complex_graph_from_REN_to_RED(self):
        expected_path = ["REN", "FAC", "BELL", "NOR", "RED"]
        expected_distance = 16

        public_transport_map = PublicTransportMap("complex_graph.json")
        path, distance = public_transport_map.shortest_distance("REN", "RED")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_distance_complex_graph_from_SEA_to_RED(self):
        expected_path = ["SEA", "EAS", "NOR", "RED"]
        expected_distance = 15

        public_transport_map = PublicTransportMap("complex_graph.json")
        path, distance = public_transport_map.shortest_distance("SEA", "RED")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_distance_complex_graph_from_EAS_to_ISS(self):
        expected_path = ["EAS", "SEA", "SOD", "FAC", "ISS"]
        expected_distance = 21

        public_transport_map = PublicTransportMap("complex_graph.json")
        path, distance = public_transport_map.shortest_distance("EAS", "ISS")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_distance_metro_from_Bambu_to_Alvarado(self):
        expected_path = ["Bambú", "Chamartín", "Plaza de Castilla", "Valdeacederas", "Tetuán", "Estrecho", "Alvarado"]
        expected_distance = 4930

        public_transport_map = PublicTransportMap("metro_stations.json")
        path, distance = public_transport_map.shortest_distance("Bambú", "Alvarado")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_distance_metro_from_Retiro_to_Anton_Martin(self):
        expected_path = ["Retiro", "Banco de España", "Sevilla", "Sol", "Tirso de Molina", "Antón Martín"]
        expected_distance = 2347

        public_transport_map = PublicTransportMap("metro_stations.json")
        path, distance = public_transport_map.shortest_distance("Retiro", "Antón Martín")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_distance_metro_from_Atocha_to_Embajadores(self):
        expected_path = ["Atocha", "Estación del Arte", "Antón Martín", "Tirso de Molina", "Sol",
                         "Lavapiés", "Embajadores"]
        expected_distance = 3510

        public_transport_map = PublicTransportMap("metro_stations.json")
        path, distance = public_transport_map.shortest_distance("Atocha", "Embajadores")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)


if __name__ == "__main__":
    unittest.main()
