#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # If the # of ingredients available is less than the number needed for a recipe than return 0
    if len(recipe) > len(ingredients):
        batches = 0
    else:
        result = [ingredients[k]/recipe[k] for k in recipe if k in ingredients]
        # Divide the amount of ingredients available by the amount needed for a recipe
        # 280/60 = 4, 51/25 =2 , 51/20 =2
        batches = math.floor(min(result))  
        # The number of batches is the minimum amount of times you can get the amount needed for a recipe from the available ingredients
        # Minimum Batches = 2
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 60, 'butter': 25, 'flour': 20}
    ingredients = {'milk': 280, 'butter': 51, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
