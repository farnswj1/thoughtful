from typing import Literal


STANDARD = "standard"
SPECIAL = "special"
REJECTED = "rejected"


def sort(
    width: float,
    height: float,
    length: float,
    mass: float
) -> Literal["standard", "special", "rejected"]:
    """Sorts a package based on its dimensions and mass.

    Args:
        width (float): The width of the package in centimeters.
        height (float): The height of the package in centimeters.
        length (float): The length of the package in centimeters.
        mass (float): The mass of the package in kilograms.

    Returns:
        Literal["standard", "special", "rejected"]: The stack category.
    """
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("The dimensions and mass must be a positive number.")

    volume = length * width * height
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return REJECTED
    elif bulky or heavy:
        return SPECIAL
    else:
        return STANDARD
