def get_recipe_price(prices, optionals=None, **ingredients):
    """
    Calculate the total price of the recipe based on ingredient prices and quantities.

    Args:
        prices (dict): A dictionary where the key is the ingredient name and the value is the price per 100g.
        optionals (list, optional): A list of optional ingredients to ignore. Defaults to None.
        **ingredients: Keyword arguments representing ingredient quantities in grams.

    Returns:
        float: The total price of the recipe.
    """
    if optionals is None:
        optionals = []

    total_price = 0
    for ingredient, quantity in ingredients.items():
        if ingredient not in optionals:
            price_per_100g = prices.get(ingredient, 0)
            total_price += (quantity / 100) * price_per_100g

    return total_price

if __name__ == "__main__":
    result1 = get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
    print(result1)  # Output: 44.0

    result2 = get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
    print(result2)  # Output: 54.0

    result3 = get_recipe_price({})
    print(result3)  # Output: 0