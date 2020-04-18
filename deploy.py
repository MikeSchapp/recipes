import os

import yaml


class RecipeRenderer:
    def __init__(self):
        with open("mkdocs.yml") as mkdocs:
            self.mkdocs_config = yaml.load(mkdocs.read())
        self.recipe_type_map = {
            "appetizers": "Appetizers",
            "dessert": "Dessert",
            "dinner": "Dinner",
            "gluten_free": "Gluten Free",
            "sauces": "Sauces",
            "smoked_foods": "Smoked Foods"
        }
        self.rendered_recipe = []

    def render_recipe_type(self, recipe_type):
        recipe_dict = {self.recipe_type_map[recipe_type]: []}
        for recipe in os.listdir(f"docs/{recipe_type}"):
            recipe_name = recipe.split('.md')[0]
            recipe_directory = f"{recipe_type}/{recipe}"
            recipe_dict[self.recipe_type_map[recipe_type]].append({
                recipe_name: recipe_directory})
        return recipe_dict

    def render_all_recipes(self):
        for recipe_type in self.recipe_type_map.keys():
            recipe_dict = self.render_recipe_type(recipe_type)
            self.rendered_recipe.append(recipe_dict)
        self.mkdocs_config["nav"][1]["Recipes"] = self.rendered_recipe

    def write_new_mkdoc_config(self):
        with open("mkdocs.yml", "w") as mkdocs:
            mkdocs.write(yaml.dump(self.mkdocs_config))


if __name__ == "__main__":
    render = RecipeRenderer()
    render.render_all_recipes()
    render.write_new_mkdoc_config()
