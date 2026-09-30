from dataclasses import dataclass


@dataclass
class Unit:
    name: str
    in_grams: float


GRAMS = Unit("grams", 1)


@dataclass
class Quantity:
    unit: Unit
    amount: float

    def to_grams(self) -> Quantity:
        return Quantity(GRAMS, self.amount * self.unit.in_grams)


@dataclass
class Ingredient:
    name: str
    quantity: Quantity
    hydration: float = 0.0


class Water(Ingredient):
    def __init__(self, quantity):
        self.name = "water"
        self.quantity = quantity
        self.hydration = 1.0


@dataclass
class Recipie:
    ingredients: list[Ingredient]

    @property
    def hydration(self):
        h = 0
        for ingredient in self.ingredients:
            q_grams = 
            h += ingredient.quantity * ingredient.hydration
