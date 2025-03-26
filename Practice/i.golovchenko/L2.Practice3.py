class Tanks:
    origin_name = 'Тигр'
    color = 'grey'

    def __init__(self, origin_name, color, rotating):
        self.origin_name = origin_name
        self.color = color
        self.rotating = rotating

    def print_about(self):
        print(f"{self.origin_name}, {self.color}, тип башни: {self.rotating}")


class Route:
    route = 'mountains'

    def __init__(self, route):
        self.route = route

    def print_route(self):
        print(f"{self.route}")


tank1 = Tanks('T-34', 'grey', 'swivel')
tank1.print_about()
tank1 = Route('desert')
tank1.print_route()

tank2 = Tanks('САУ', '', 'non-reversible ')
tank2.print_about()

tank3 = Tanks('BT-5', 'green', '-')
tank3.print_about()
tank3 = Route('forest')
tank3.print_route()
