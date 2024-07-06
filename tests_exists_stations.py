import unittest
from public_transport_route_optimizer import PublicTransportMap


class TestPublicTransportRouteOptimizerExistsStation(unittest.TestCase):

    def test_lowercase(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("portazgo"))

    def test_uppercase(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("PORTAZGO"))

    def test_spaces_and_lowercase(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("puente de vallecas"))

    def test_spaces_and_uppercase(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("PUENTE DE VALLECAS"))

    def test_spaces_upper_and_lowercase(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("Puente DE ValleCAS"))

    def test_with_underscores(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("puente_de_vallecas"))

    def test_with_wrong_accent_mark(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("Miguel Hérnandez"))

    def test_without_accent_mark(self):
        public_transport_map = PublicTransportMap("metro_stations.json")

        self.assertFalse(public_transport_map.exists_station("Miguel Hernandez"))


if __name__ == '__main__':
    unittest.main()
