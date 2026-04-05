from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    words = ingredients.lower().split()
    is_valid = any(word in allowed for word in words)
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
