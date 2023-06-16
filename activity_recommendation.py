from input_choose import *
from util import recommend

def get_activity_prompt():
    destination = get_destination()
    activity_type = get_activity_type()
    duration = get_duration()
    grouptype = get_travel_group()
    budget = get_budget()
    prompt = f"""Now you are my travel assistant and guide. 
Recommend top 3 activities about {activity_type} in {destination},
trip duration in {duration} days.
the budget is ${budget} per person,
the trip is {grouptype}
output theses activities as a list"""
    return prompt


def recommend_activities(model):
    prompt = get_activity_prompt()
    recommendation = recommend(model, prompt)
    first_index = recommendation.find("1.")
    second_index = recommendation.find("2.")
    third_index = recommendation.find("3.")
    if second_index != -1:
        print(recommendation[first_index:second_index])
        if third_index != -1:
            print(recommendation[second_index:third_index])
    else:
        print(recommendation[first_index:])

if __name__ == "__main__":
    print("recommendation of activities")
   
    recommend_activities()

