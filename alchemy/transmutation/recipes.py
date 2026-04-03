from alchemy.elements import create_air  # absolute import
from ..potions import strength_potion    # relative import


def lead_to_gold() -> str:
    from elements import create_fire     # absolute import (root)
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{create_fire()}'"
    )
