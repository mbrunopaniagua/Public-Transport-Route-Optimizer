import unittest
from public_transport_route_optimizer import PublicTransportMap


class TestPublicTransportRouteOptimizer(unittest.TestCase):

    def test_shortest_path_simple_graph_from_A_to_B(self):
        expected_path = ["A", "B", "E", "G"]
        expected_steps = 3

        public_transport_map = PublicTransportMap("simple_graph.json")
        path, steps = public_transport_map.shortest_path("A", "G")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_steps, steps)

    def test_shortest_path_complex_graph_from_REN_to_RED(self):
        expected_path = ["REN", "FAC", "RED"]
        expected_steps = 2

        public_transport_map = PublicTransportMap("complex_graph.json")
        path, steps = public_transport_map.shortest_path("REN", "RED")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_steps, steps)

    def test_shortest_path_complex_graph_from_SEA_to_RED(self):
        expected_path = ["SEA", "SOD", "FAC", "RED"]
        expected_distance = 3

        public_transport_map = PublicTransportMap("complex_graph.json")
        path, distance = public_transport_map.shortest_path("SEA", "RED")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_path_complex_graph_from_EAS_to_ISS(self):
        expected_path = ["EAS", "NOR", "RED", "ISS"]
        expected_distance = 3

        public_transport_map = PublicTransportMap("complex_graph.json")
        path, distance = public_transport_map.shortest_path("EAS", "ISS")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_distance, distance)

    def test_shortest_path_metro_from_Bambu_to_Alvarado(self):
        expected_path = ["Bambú", "Chamartín", "Plaza de Castilla", "Valdeacederas", "Tetuán", "Estrecho", "Alvarado"]
        expected_steps = 6

        public_transport_map = PublicTransportMap("metro_stations.json")
        path, steps = public_transport_map.shortest_path("Bambú", "Alvarado")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_steps, steps)

    def test_shortest_path_metro_from_Retiro_to_Anton_Martin(self):
        expected_path = ["Retiro", "Banco de España", "Sevilla", "Sol", "Tirso de Molina", "Antón Martín"]
        expected_steps = 5

        public_transport_map = PublicTransportMap("metro_stations.json")
        path, steps = public_transport_map.shortest_path("Retiro", "Antón Martín")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_steps, steps)

    def test_shortest_path_metro_from_Atocha_to_Embajadores(self):
        expected_path = ["Atocha", "Menéndez Pelayo", "Pacífico", "Méndez Álvaro", "Arganzuela-Planetario",
                         "Legazpi", "Embajadores"]
        expected_steps = 6

        public_transport_map = PublicTransportMap("metro_stations.json")
        path, steps = public_transport_map.shortest_path("Atocha", "Embajadores")

        self.assertEqual(expected_path, list(path))
        self.assertEqual(expected_steps, steps)


if __name__ == "__main__":
    unittest.main()
