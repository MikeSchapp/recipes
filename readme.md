# Recipes Collection

A repository of family recipes that can be updated, modified, forked, or branched to create delicious variants. This site is built using MkDocs to display recipes in an organized, searchable format.

## Project Structure

Recipes are organized by category in the `docs` directory:

- `appetizers`: Dips, starters, and small bites
- `breakfast`: Morning meals and brunch items
- `dessert`: Sweet treats and confections
- `dinner`: Main courses and entrees
- `gluten_free`: Recipes without gluten
- `sauces`: Dressings, sauces, and condiments
- `side_dishes`: Accompaniments and side dishes
- `smoked_foods`: Smoked and cured recipes

## Adding a Recipe

To add a new recipe:

1. Create a markdown (.md) file in the appropriate category folder
2. Use a clear, descriptive name for the file (e.g., `Chocolate Chip Cookies.md`)
3. Follow the recipe template format below

### Recipe Template

```markdown
# Recipe Name

## Description
A brief description of the dish, its origins, or special notes.

## Ingredients
- 2 cups ingredient one
- 1 tsp ingredient two
- 3 tbsp ingredient three

## Instructions
1. First step in the process
2. Second step in the process
3. Continue with numbered steps

## Notes (optional)
- Preparation time: 20 minutes
- Cooking time: 45 minutes
- Serves: 4 people
- Any substitutions or variations
```

## Markdown Guide

Markdown formatting reference:

```markdown
# Main Heading

## Subheading

### Smaller Heading

- Bulleted list item
- Another bullet point

1. Numbered list item
2. Second numbered item

*Italic text*
**Bold text**

[Link text](https://example.com)

> Blockquote for notes or tips
```

## Running the Site Locally

1. Install the requirements: `pip install -r requirements.txt`
2. Run the development server: `mkdocs serve`
3. Open your browser to `http://127.0.0.1:8000/`

## Deploying the Site

Use the included deploy script: `python deploy.py`
