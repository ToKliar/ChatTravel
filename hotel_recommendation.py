from prettytable import PrettyTable
from input_choose import *
from util import recommend

def get_hotel_prompt():
    destination = get_destination()
    date = get_start_date()
    duration = get_duration()
    people_num = get_people_num()
    budget = get_budget()
    accommodation_kind = get_accommodation_kind()
    accommodation_preference = get_accommodation_preference()
    prompt = f'''Now you are my travel assistant and guide.
I am planning a {duration}-day and {people_num}-people trip to {destination} starting from {date}, with a budget of ${budget} per person, living in the {accommodation_kind} with {accommodation_preference}.
Please give the recommended accommodation's name, location and price.
In addition, please recommend the appropriate mode of transportation based on the travel information and the distance between the main scenic spot and the accommodation.
Please output accommodation's name, accommodation's location, accommodation's price, accommodation's booking method, transportation around and the distance between the main scenic spot and the accommodation in table format.'''
    return prompt

def recommend_hotel(model):
    prompt = get_hotel_prompt()
    recommendation = recommend(model, prompt)
    name, loc, price, booking_method, distance_between_main_scenic_spot = recommendation.split(' || ')[2].split(' | ')    
    table = PrettyTable(['name','location','price','booking_method', 'distance_between_main_scenic_spot'])
    table.add_row([name, loc, price, booking_method, distance_between_main_scenic_spot])
    print(table)

    

if __name__ == '__main__':
    print("recommend of hotel")
    recommend_hotel()
    