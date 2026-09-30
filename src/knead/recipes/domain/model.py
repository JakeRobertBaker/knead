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
    water_frac: float = 0
    flour_frac: float = 0

    def __post_init__(self):
        if not 0 <= self.water_frac <= 1:
            raise ValueError("hydration must be between 0 and 1")

        if not 0 <= self.flour_frac <= 1:
            raise ValueError("farinaceous must be between 0 and 1")

        if self.water_frac + self.flour_frac > 1:
            raise ValueError(
                "hydration and farinaceous fractions cannot exceed total mass"
            )


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
            flour_mass = mass * ingredient.type.flour_frac
            hydrated_mass = mass * ingredient.type.water_frac
            f += flour_mass
            h += hydrated_mass

        return h / f
