from enum import Enum


class Unit(str,Enum):
    cup = "cup"
    tablespoon = "tbsp"
    teaspoon = "tsp"
    ounce = "oz"
    pound = "lb"
    gram = "g"
    kilogram = "kg"
    milliliter = "ml"
    liter = "l"
    piece = "piece"