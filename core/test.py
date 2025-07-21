from core.models.world_map import WorldMap
from core.routes_generator import RoutesGenerator
from utils.print_helper import PrintHelper


if __name__ == '__main__':
    HEADERS = ['City A', 'City B', 'Colors', 'Length', 'Locomotives', 'Defensive']

    world_map = WorldMap.create_default()
    routes_generator = RoutesGenerator(world_map)

    generated_routes = [
        routes_generator.generate_primary_route(),
        routes_generator.generate_route(),
        routes_generator.generate_route(),
        routes_generator.generate_route()
    ]

    for route in generated_routes:
        PrintHelper.print_block(f'{route.city_a} -> {route.city_b}', 1, print_bottom_line=False)
        content = [[p.city_a, p.city_b, p.get_colors_str(), p.length, p.locomotives, p.defensive] for p in route.parts]
        PrintHelper.print_table(HEADERS, content)
        print('')
