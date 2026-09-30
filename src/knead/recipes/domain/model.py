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


@dataclass(frozen=True)
class IngredientType:
    name: str
    hydration: float = 0
    farinaceous: float = 0


WATER = IngredientType("water", 1)


@dataclass
class Ingredient:
    type: IngredientType
    quantity: Quantity


@dataclass
class Recipe:
    ingredients: list[Ingredient]

    @property
    def hydration(self):
        h = 0
        f = 0
        for ingredient in self.ingredients:
            mass = ingredient.quantity.to_grams().amount
            flour_mass = mass * ingredient.type.farinaceous
            hydrated_mass = mass * ingredient.type.hydration
            f += flour_mass
            h += hydrated_mass

        return h / f
