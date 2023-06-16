from input_choose import *
from util import recommend
from prettytable import PrettyTable

def get_restaurant_prompt():
    budget = get_food_budget()
    taste_preference = get_taste_preference()
    destination = get_destination()
    prompt = f"""Now you are my travel assistant and guide.
Recommend some restaurants in {destination},
considering taste preferences : {taste_preference},
and budget is {budget}.
Please output restaurant's name, restaurant's location and per capita consumption in table format."""
    return prompt

def recommend_restaurant(model):
    prompt = get_restaurant_prompt()
    response = recommend(model, prompt)
    restaurants = response.split(":")[1].split(".")[:-2]
    table = PrettyTable(['restaurant', 'location', 'description'])
    for i in range(1, len(restaurants), 2):
        res = restaurants[i].strip()
        name = res.split(' - ')[0]
        location, description = res.split(' - ')[1].split(", ")
        table.add_row([name, location, description])
    print(table)

if __name__ == "__main__":
    print("recommend of restaurants")
    recommend_restaurant()
