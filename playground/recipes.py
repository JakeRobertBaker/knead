from knead.recipes.domain.model import (
    GRAMS,
    Ingredient,
    IngredientType,
    Quantity,
    Recipe,
    WATER,
)

FLOUR = IngredientType("bread flour", flour_frac=1)

recipe = Recipe(
    [
        Ingredient(FLOUR, Quantity(GRAMS, 500)),
        Ingredient(WATER, Quantity(GRAMS, 350)),
    ]
)

print(recipe.hydration)
print(recipe.total_quantity)
print(recipe.to_total_quantity(1000))
