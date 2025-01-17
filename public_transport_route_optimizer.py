from collections import deque
from pathlib import Path
from collections import OrderedDict
from travel_mode import TravelMode
from type_of_transport import Transport
from menu_option import MenuOption
import json

INFINITY = float("inf")


class UnknownStationError(Exception):
    pass


class PublicTransportMap:
    def __init__(self, filename):
        data = PublicTransportMap.__get_data_from_file(filename)
        self.stations = PublicTransportMap.__get_all_stations(data)
        self.full_stations_map = PublicTransportMap.__get_full_stations_map(data)

    @staticmethod
    def __get_data_from_file(filename):
        path = Path(__file__).parent / "data" / filename
        with path.open("r") as file:
            data = json.load(file)
        return data

    @staticmethod
    def __get_full_stations_map(data):
        full_stations_map = {station["name"]: [] for line in data["lines"] for station in line["stations"]}
        for line in data["lines"]:
            for station in line["stations"]:
                for connection in station["connections"]:
                    full_stations_map[station["name"]].append((connection["to"], float(connection["distance"])))
        return full_stations_map

    @staticmethod
    def __get_all_stations(data):
        stations = []
        for line in data["lines"]:
            for station in line["stations"]:
                if station["name"] not in stations:
                    stations.append(station["name"])
        return stations

    def exists_station(self, station_name):
        return station_name in [station for station in self.stations]

    def shortest_path(self, start_station, end_station):
        return self.__calculate_path(start_station, end_station, TravelMode.FEWER_STATIONS)

    def shortest_distance(self, start_station, end_station):
        return self.__calculate_path(start_station, end_station, TravelMode.SHORTEST_DISTANCE)

    def __calculate_path(self, start_station, end_station, travel_mode):

        unvisited_stations = self.stations.copy()

        distance_from_start = self.__init_distance_from_start_station(start_station)

        previous_station = {station: None for station in self.stations}

        while unvisited_stations:
            current_station = min(unvisited_stations, key=lambda station: distance_from_start[station])
            unvisited_stations.remove(current_station)

            if distance_from_start[current_station] == INFINITY:
                break

            self.__calculate_path_by_travel_mode(current_station, distance_from_start, previous_station, travel_mode)

            if current_station == end_station:
                break

        path = deque()
        current_station = end_station
        while previous_station[current_station] is not None:
            path.appendleft(current_station)
            current_station = previous_station[current_station]
        path.appendleft(start_station)

        return path, distance_from_start[end_station]

    def __init_distance_from_start_station(self, start_station):
        distance_from_start = OrderedDict()
        for station in self.stations:
            if station == start_station:
                distance_from_start[station] = 0
            else:
                distance_from_start[station] = INFINITY
        return distance_from_start

    def __calculate_path_by_travel_mode(self, current_station, distance_from_start, previous_station, travel_mode):
        match travel_mode:
            case TravelMode.SHORTEST_DISTANCE:
                self.__calculate_distance(current_station, distance_from_start, previous_station)
            case TravelMode.FEWER_STATIONS:
                self.__calculate_path_with_fixed_distance(current_station, distance_from_start, previous_station)

    def __calculate_distance(self, current_station, distance_from_start, previous_station):
        for neighbor, distance in self.full_stations_map[current_station]:
            new_distance = distance_from_start[current_station] + distance
            if new_distance < distance_from_start[neighbor]:
                distance_from_start[neighbor] = new_distance
                previous_station[neighbor] = current_station

    def __calculate_path_with_fixed_distance(self, current_station, distance_from_start, previous_station):
        for neighbor, distance in self.full_stations_map[current_station]:
            new_distance = distance_from_start[current_station] + 1
            if new_distance < distance_from_start[neighbor]:
                distance_from_start[neighbor] = new_distance
                previous_station[neighbor] = current_station


def main():
    print('*** TRANSPORT ROUTE OPTIMIZER ***')
    __write_menu()


def __write_menu():
    while 1:
        __write_travel_mode_menu()
        travel_mode_option = __get_travel_mode_option()

        if travel_mode_option == MenuOption.EXIT.value:
            break

        while 1:
            try:
                start_station, end_station = __get_start_and_end_station()
                __find_path(travel_mode_option, start_station, end_station)
                break
            except UnknownStationError as e:
                print(f"\tERROR: {e}. Please type a correct station name\n")
                continue


def __find_path(travel_mode_option, start_station, end_station):
    public_transport_map = PublicTransportMap(Transport.METRO.file)

    if not public_transport_map.exists_station(start_station):
        raise UnknownStationError(f"Station '{start_station}' does not exist")

    if not public_transport_map.exists_station(end_station):
        raise UnknownStationError(f"Station '{end_station}' does not exist")

    match travel_mode_option:
        case TravelMode.SHORTEST_DISTANCE.value:
            path, distance = public_transport_map.shortest_distance(start_station, end_station)
            __write_path(path)
            print(f"\tDistance: {distance} meters")
        case TravelMode.FEWER_STATIONS.value:
            path, steps = public_transport_map.shortest_path(start_station, end_station)
            __write_path(path)
            print(f"\tTotal stations: {steps}")


def __write_travel_mode_menu():
    print('\n\t* Travel mode options *')
    print(f"\tOption {TravelMode.SHORTEST_DISTANCE}: {TravelMode.SHORTEST_DISTANCE.text} (meters)")
    print(f"\tOption {TravelMode.FEWER_STATIONS}: {TravelMode.FEWER_STATIONS.text}")
    print(f"\tOption {MenuOption.EXIT.value}: {MenuOption.EXIT.text}")


def __get_start_and_end_station():
    start_station = input("\tFrom station name: ")
    end_station = input("\tTo station name: ")

    return start_station, end_station


def __write_path(path):
    print("\tPath: ", end="")
    for station in path:
        if station == path[-1]:
            print(f"{station}")
        else:
            print(f"{station} -> ", end="")


def __get_travel_mode_option():
    while 1:
        try:
            travel_mode_option = int(input(f"\n\tEnter your travel mode option ({MenuOption.EXIT.value}-{TravelMode.FEWER_STATIONS}): "))
            if travel_mode_option < MenuOption.EXIT.value or travel_mode_option > TravelMode.FEWER_STATIONS.value:
                print(f"\tERROR: Invalid option. Please enter a value between {MenuOption.EXIT.value} and {TravelMode.FEWER_STATIONS}\n")
                continue
            else:
                return travel_mode_option
        except ValueError:
            print(f"\tERROR: Invalid option. Please enter a number between {MenuOption.EXIT.value} and {TravelMode.FEWER_STATIONS}\n")
            continue


if __name__ == "__main__":
    main()
