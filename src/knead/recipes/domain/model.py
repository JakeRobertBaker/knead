from dataclasses import dataclass


@dataclass(frozen=True)
class Unit:
    name: str
    in_grams: float


GRAMS = Unit("grams", 1)


@dataclass(frozen=True)
class Quantity:
    unit: Unit
    amount: float

    def to_grams(self) -> Quantity:
        return Quantity(GRAMS, self.amount * self.unit.in_grams)

    def __mul__(self, scalar: float):
        if isinstance(scalar, (float, int)):
            return Quantity(self.unit, self.amount * scalar)
        else:
            return NotImplementedError


@dataclass(frozen=True)
class IngredientType:
    name: str
    water_frac: float = 0
    flour_frac: float = 0

    def __post_init__(self):
        if not 0 <= self.water_frac <= 1:
            raise ValueError("water fraction must be between 0 and 1")

        if not 0 <= self.flour_frac <= 1:
            raise ValueError("flour fraction must be between 0 and 1")

        if self.water_frac + self.flour_frac > 1:
            raise ValueError("water and flour fractions cannot exceed total mass")


WATER = IngredientType("water", 1)


@dataclass(frozen=True)
class Ingredient:
    type: IngredientType
    quantity: Quantity

    def __mul__(self, scalar: float):
        if isinstance(scalar, (float, int)):
            Ingredient(self.type, self.quantity * scalar)
        else:
            return NotImplementedError


@dataclass
class Recipe:
    ingredients: list[Ingredient]

    @property
    def hydration(self) -> float:
        h = 0
        f = 0
        for ingredient in self.ingredients:
            mass = ingredient.quantity.to_grams().amount
            flour_mass = mass * ingredient.type.flour_frac
            hydrated_mass = mass * ingredient.type.water_frac
            f += flour_mass
            h += hydrated_mass

        # TODO: zero division error
        return h / f

    def __mul__(self, scalar: float):
        if isinstance(scalar, (float, int)):
            return Recipe([i * scalar for i in self.ingredients])
        else:
            return NotImplementedError
