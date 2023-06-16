from config import *
from gpt4all import GPT4All
from travel_plan_design import recommend_travel_plan
from restaurant_recommendation import recommend_restaurant
from activity_recommendation import recommend_activities
from destination_recommendation import recommend_destination
from hotel_recommendation import recommend_hotel
from travel_tip import recommend_travel_tips

if __name__ == "__main__":
    gptj = GPT4All(model_name, model_path)
    while True:
        function = input('''
This is travel helper to help you better plan your visit using local LLM.
Please enter a number to choose what function you want to use:
1. Design Travel Plan
2. Recommend Restaurants
3. Recommend Local Activities
4. Recommend Travel Destination
5. Recommend Acommodation
6. Get Some Travel Tips
You can enter 0 to quit.
''')
        if function.isdigit() and len(function) == 1:
            if function == '0':
                break
            if function == '1':
                recommend_travel_plan(gptj)
            elif function == '2':
                recommend_restaurant(gptj)
            elif function == '3':
                recommend_activities(gptj)
            elif function == '4':
                recommend_destination(gptj)
            elif function == '5':
                recommend_hotel(gptj)
            elif function == '6':
                recommend_travel_tips(gptj)
        else:
            print("Please enter as required.")