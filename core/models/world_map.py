from typing import Dict, List

from core.enums.color_enum import ColorEnum
from core.models.city import City
from core.models.route import Route
from core.models.route_variant import RouteVariant
from core.static.city_names import CityNames
from utils.file_utils import FileUtils


class WorldMap:
    FIELD_CITIES_KEY = 'cities'
    FIELD_ROUTES_KEY = 'routes'

    def __init__(self, cities: Dict[str, City], routes: List[Route]):
        self.cities: Dict[str, City] = cities if cities else {}
        self.routes: List[Route] = routes if routes else []

    @staticmethod
    def create_default() -> 'WorldMap':
        cities = {city_name: city for city_name, city in CityNames.CITIES.items()}
        routes = [
            Route(CityNames.get(CityNames.CITY_AMSTERDAM), CityNames.get(CityNames.CITY_BRUXELLES), variants=[
                RouteVariant(ColorEnum.BLACK, 1)
            ]),
            Route(CityNames.get(CityNames.CITY_AMSTERDAM), CityNames.get(CityNames.CITY_ESSEN), variants=[
                RouteVariant(ColorEnum.YELLOW, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_AMSTERDAM), CityNames.get(CityNames.CITY_FRANKFURT), variants=[
                RouteVariant(ColorEnum.WHITE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_AMSTERDAM), CityNames.get(CityNames.CITY_LONDON), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_ANGORA), CityNames.get(CityNames.CITY_CONSTANTINOPLE), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_ANGORA), CityNames.get(CityNames.CITY_ERZURUM), variants=[
                RouteVariant(ColorEnum.BLACK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_ANGORA), CityNames.get(CityNames.CITY_SMYRNA), variants=[
                RouteVariant(ColorEnum.ORANGE, 3, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_ATHINA), CityNames.get(CityNames.CITY_BRINDISI), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4, locomotives=1)
            ]),
            Route(CityNames.get(CityNames.CITY_ATHINA), CityNames.get(CityNames.CITY_SARAJEVO), variants=[
                RouteVariant(ColorEnum.GREEN, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_ATHINA), CityNames.get(CityNames.CITY_SMYRNA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, locomotives=1)
            ]),
            Route(CityNames.get(CityNames.CITY_ATHINA), CityNames.get(CityNames.CITY_SOFIA), variants=[
                RouteVariant(ColorEnum.PINK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_BARCELONA), CityNames.get(CityNames.CITY_MADRID), variants=[
                RouteVariant(ColorEnum.YELLOW, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BARCELONA), CityNames.get(CityNames.CITY_MARSEILLE), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_BARCELONA), CityNames.get(CityNames.CITY_PAMPLONA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_BERLIN), CityNames.get(CityNames.CITY_DANZIG), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_BERLIN), CityNames.get(CityNames.CITY_ESSEN), variants=[
                RouteVariant(ColorEnum.BLUE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BERLIN), CityNames.get(CityNames.CITY_FRANKFURT), variants=[
                RouteVariant(ColorEnum.RED, 3),
                RouteVariant(ColorEnum.BLACK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_BERLIN), CityNames.get(CityNames.CITY_WARSZAWA), variants=[
                RouteVariant(ColorEnum.YELLOW, 4),
                RouteVariant(ColorEnum.PINK, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_BERLIN), CityNames.get(CityNames.CITY_WIEN), variants=[
                RouteVariant(ColorEnum.GREEN, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_BREST), CityNames.get(CityNames.CITY_DIEPPE), variants=[
                RouteVariant(ColorEnum.ORANGE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BREST), CityNames.get(CityNames.CITY_PAMPLONA), variants=[
                RouteVariant(ColorEnum.PINK, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_BREST), CityNames.get(CityNames.CITY_PARIS), variants=[
                RouteVariant(ColorEnum.BLACK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_BRINDISI), CityNames.get(CityNames.CITY_PALERMO), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 3, locomotives=1)
            ]),
            Route(CityNames.get(CityNames.CITY_BRINDISI), CityNames.get(CityNames.CITY_ROMA), variants=[
                RouteVariant(ColorEnum.WHITE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BRUXELLES), CityNames.get(CityNames.CITY_DIEPPE), variants=[
                RouteVariant(ColorEnum.GREEN, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BRUXELLES), CityNames.get(CityNames.CITY_FRANKFURT), variants=[
                RouteVariant(ColorEnum.BLUE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BRUXELLES), CityNames.get(CityNames.CITY_PARIS), variants=[
                RouteVariant(ColorEnum.YELLOW, 2),
                RouteVariant(ColorEnum.RED, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_BUCURESTI), CityNames.get(CityNames.CITY_BUDAPEST), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_BUCURESTI), CityNames.get(CityNames.CITY_CONSTANTINOPLE), variants=[
                RouteVariant(ColorEnum.YELLOW, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_BUCURESTI), CityNames.get(CityNames.CITY_KYIV), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_BUCURESTI), CityNames.get(CityNames.CITY_SEVASTOPOL), variants=[
                RouteVariant(ColorEnum.WHITE, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_BUCURESTI), CityNames.get(CityNames.CITY_SOFIA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_BUDAPEST), CityNames.get(CityNames.CITY_KYIV), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 6, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_BUDAPEST), CityNames.get(CityNames.CITY_SARAJEVO), variants=[
                RouteVariant(ColorEnum.PINK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_BUDAPEST), CityNames.get(CityNames.CITY_WIEN), variants=[
                RouteVariant(ColorEnum.WHITE, 1),
                RouteVariant(ColorEnum.RED, 1)
            ]),
            Route(CityNames.get(CityNames.CITY_BUDAPEST), CityNames.get(CityNames.CITY_ZAGRAB), variants=[
                RouteVariant(ColorEnum.ORANGE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_CADIZ), CityNames.get(CityNames.CITY_LISBOA), variants=[
                RouteVariant(ColorEnum.BLUE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_CADIZ), CityNames.get(CityNames.CITY_MADRID), variants=[
                RouteVariant(ColorEnum.ORANGE, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_CONSTANTINOPLE), CityNames.get(CityNames.CITY_SEVASTOPOL), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4, locomotives=2)
            ]),
            Route(CityNames.get(CityNames.CITY_CONSTANTINOPLE), CityNames.get(CityNames.CITY_SMYRNA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_CONSTANTINOPLE), CityNames.get(CityNames.CITY_SOFIA), variants=[
                RouteVariant(ColorEnum.BLUE, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_DANZIG), CityNames.get(CityNames.CITY_RIGA), variants=[
                RouteVariant(ColorEnum.BLACK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_DANZIG), CityNames.get(CityNames.CITY_WARSZAWA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_DIEPPE), CityNames.get(CityNames.CITY_LONDON), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, 1),
                RouteVariant(ColorEnum.TRANSPARENT, 2, 1),
            ]),
            Route(CityNames.get(CityNames.CITY_DIEPPE), CityNames.get(CityNames.CITY_PARIS), variants=[
                RouteVariant(ColorEnum.PINK, 1)
            ]),
            Route(CityNames.get(CityNames.CITY_EDINBURGH), CityNames.get(CityNames.CITY_LONDON), variants=[
                RouteVariant(ColorEnum.ORANGE, 4),
                RouteVariant(ColorEnum.BLACK, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_ERZURUM), CityNames.get(CityNames.CITY_SEVASTOPOL), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4, locomotives=2)
            ]),
            Route(CityNames.get(CityNames.CITY_ERZURUM), CityNames.get(CityNames.CITY_SOCHI), variants=[
                RouteVariant(ColorEnum.RED, 3, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_ESSEN), CityNames.get(CityNames.CITY_FRANKFURT), variants=[
                RouteVariant(ColorEnum.GREEN, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_ESSEN), CityNames.get(CityNames.CITY_KOBENHAVN), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 3, locomotives=1),
                RouteVariant(ColorEnum.TRANSPARENT, 3, locomotives=1)
            ]),
            Route(CityNames.get(CityNames.CITY_FRANKFURT), CityNames.get(CityNames.CITY_MUNCHEN), variants=[
                RouteVariant(ColorEnum.PINK, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_FRANKFURT), CityNames.get(CityNames.CITY_PARIS), variants=[
                RouteVariant(ColorEnum.WHITE, 3),
                RouteVariant(ColorEnum.ORANGE, 3),
            ]),
            Route(CityNames.get(CityNames.CITY_KHARKOV), CityNames.get(CityNames.CITY_KYIV), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_KHARKOV), CityNames.get(CityNames.CITY_MOSKVA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_KHARKOV), CityNames.get(CityNames.CITY_ROSTOV), variants=[
                RouteVariant(ColorEnum.GREEN, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_KOBENHAVN), CityNames.get(CityNames.CITY_STOCKHOLM), variants=[
                RouteVariant(ColorEnum.WHITE, 3),
                RouteVariant(ColorEnum.YELLOW, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_KYIV), CityNames.get(CityNames.CITY_SMOLENSK), variants=[
                RouteVariant(ColorEnum.RED, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_KYIV), CityNames.get(CityNames.CITY_WARSZAWA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_KYIV), CityNames.get(CityNames.CITY_WILNO), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_LISBOA), CityNames.get(CityNames.CITY_MADRID), variants=[
                RouteVariant(ColorEnum.PINK, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_MADRID), CityNames.get(CityNames.CITY_PAMPLONA), variants=[
                RouteVariant(ColorEnum.WHITE, 3, defensive=True),
                RouteVariant(ColorEnum.BLACK, 3, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_MARSEILLE), CityNames.get(CityNames.CITY_PAMPLONA), variants=[
                RouteVariant(ColorEnum.RED, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_MARSEILLE), CityNames.get(CityNames.CITY_PARIS), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_MARSEILLE), CityNames.get(CityNames.CITY_ROMA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_MARSEILLE), CityNames.get(CityNames.CITY_ZURICH), variants=[
                RouteVariant(ColorEnum.PINK, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_MOSKVA), CityNames.get(CityNames.CITY_PETROGRAD), variants=[
                RouteVariant(ColorEnum.WHITE, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_MOSKVA), CityNames.get(CityNames.CITY_SMOLENSK), variants=[
                RouteVariant(ColorEnum.ORANGE, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_MUNCHEN), CityNames.get(CityNames.CITY_VENEZIA), variants=[
                RouteVariant(ColorEnum.BLUE, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_MUNCHEN), CityNames.get(CityNames.CITY_WIEN), variants=[
                RouteVariant(ColorEnum.ORANGE, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_MUNCHEN), CityNames.get(CityNames.CITY_ZURICH), variants=[
                RouteVariant(ColorEnum.YELLOW, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_PALERMO), CityNames.get(CityNames.CITY_ROMA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4, locomotives=1)
            ]),
            Route(CityNames.get(CityNames.CITY_PALERMO), CityNames.get(CityNames.CITY_SMYRNA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 6, locomotives=2)
            ]),
            Route(CityNames.get(CityNames.CITY_PAMPLONA), CityNames.get(CityNames.CITY_PARIS), variants=[
                RouteVariant(ColorEnum.BLUE, 4),
                RouteVariant(ColorEnum.GREEN, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_PARIS), CityNames.get(CityNames.CITY_ZURICH), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 3, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_PETROGRAD), CityNames.get(CityNames.CITY_RIGA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_PETROGRAD), CityNames.get(CityNames.CITY_STOCKHOLM), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 8, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_PETROGRAD), CityNames.get(CityNames.CITY_WILNO), variants=[
                RouteVariant(ColorEnum.BLUE, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_RIGA), CityNames.get(CityNames.CITY_WILNO), variants=[
                RouteVariant(ColorEnum.GREEN, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_ROMA), CityNames.get(CityNames.CITY_VENEZIA), variants=[
                RouteVariant(ColorEnum.BLACK, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_ROSTOV), CityNames.get(CityNames.CITY_SEVASTOPOL), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_ROSTOV), CityNames.get(CityNames.CITY_SOCHI), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_SARAJEVO), CityNames.get(CityNames.CITY_SOFIA), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_SARAJEVO), CityNames.get(CityNames.CITY_ZAGRAB), variants=[
                RouteVariant(ColorEnum.RED, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_SEVASTOPOL), CityNames.get(CityNames.CITY_SOCHI), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2, locomotives=1)
            ]),
            Route(CityNames.get(CityNames.CITY_SMOLENSK), CityNames.get(CityNames.CITY_WILNO), variants=[
                RouteVariant(ColorEnum.YELLOW, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_VENEZIA), CityNames.get(CityNames.CITY_ZAGRAB), variants=[
                RouteVariant(ColorEnum.TRANSPARENT, 2)
            ]),
            Route(CityNames.get(CityNames.CITY_VENEZIA), CityNames.get(CityNames.CITY_ZURICH), variants=[
                RouteVariant(ColorEnum.GREEN, 2, defensive=True)
            ]),
            Route(CityNames.get(CityNames.CITY_WARSZAWA), CityNames.get(CityNames.CITY_WIEN), variants=[
                RouteVariant(ColorEnum.BLUE, 4)
            ]),
            Route(CityNames.get(CityNames.CITY_WARSZAWA), CityNames.get(CityNames.CITY_WILNO), variants=[
                RouteVariant(ColorEnum.RED, 3)
            ]),
            Route(CityNames.get(CityNames.CITY_WIEN), CityNames.get(CityNames.CITY_ZAGRAB), variants=[
            RouteVariant(ColorEnum.TRANSPARENT, 2)
        ])
        ]
        return WorldMap(cities, routes)

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'WorldMap':
        cities = data.get(WorldMap.FIELD_CITIES_KEY, {})
        routes = data.get(WorldMap.FIELD_ROUTES_KEY, [])

        return WorldMap(
            cities={key: City.from_dict(city) for key, city in cities.items()},
            routes=[Route.from_dict(route) for route in routes]
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_CITIES_KEY: {key: city.to_dict() for key, city in self.cities.items()},
            self.FIELD_ROUTES_KEY: [route.to_dict() for route in self.routes],
        }

    @staticmethod
    def load_from_file(file_path: str) -> 'WorldMap':
        if not FileUtils.file_exists(file_path):
            raise Exception(f'File \"{file_path}\" not found.')

        world_map = FileUtils.read_json(file_path)
        return WorldMap.from_dict(world_map)

    def save_to_file(self, file_path: str):
        if not FileUtils.is_valid_file_path(file_path):
            raise Exception(f'Invalid file path \"{file_path}\".')

        FileUtils.ensure_folder_for_file(file_path)
        FileUtils.save_json(file_path, self.to_dict())

    # endregion
