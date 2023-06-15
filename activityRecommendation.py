from gpt4all import GPT4All
def get_activity_type():
    activity_preference = input("do you have a preference on activities?\n "
                                "enter 1 for city activity\n"
                                "enter 2 for nature activity\n"
                                "enter 3 for cultural activity\n"
                                )
    if activity_preference == 1:
        activity_preference = "city(city special)"
    elif activity_preference == 2:
        activity_preference = "nature(climbing mountains,hiking,park)"
    elif activity_preference == 3:
        activity_preference = 'culture(museums/architecture/cultural sightseeing)'
    else:
        activity_preference = "all kinds"
    return activity_preference

def getTravelGroup():
    people = input(
        '''what is your group type of this trip:
                        1. Traveling solo
                        2. Travel with a partner
                        3. Traveling with family
                        4. Traveling with friends
                        ''')
    if int(people) == 1:
        peoples = 'Solo travel'
    elif int(people) == 2:
        peoples = 'Traveling with a partner'
    elif int(people) == 3:
        peoples = 'Traveling with family'
    elif int(people) == 4:
        peoples = 'Traveling with friends'
    else:
        peoples = 'Solo travel'
    return peoples

def get_activity_information():
    destination = input("where is your destination\n")
    duration = input("enter your trip duration\n")
    grouptype = getTravelGroup()
    budget = input("enter the budget of your trip per person\n")
    fitness_level = input("enter your fitness_level strong /medium /beginner \n")
    basic_information = {
        "destination": destination,
        "duration": duration,
        "group type": grouptype,
        "budget": budget,
        "fitness_level": fitness_level
    }

    return basic_information


def recommend_activities(basic_information):
    model_path = '/content/drive/My Drive/chattravel'
    gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", model_path)
    # basic_information = {
    #     "destination": destination,
    #     "duration": duration,
    #     "group type": grouptype,
    #     "budget": budget,
    #     "fitness_level": fitness_level
    # }
    type = get_activity_type()
    destination = basic_information['destination']
    trip_duration = basic_information['duration']
    budget = basic_information['budget']
    grouptype = basic_information['group type']
    prompt = f"""
   Now you are my travel assistant and guide. 
    Recommend top 3 activities about {type} in {destination},
    trip duration in {trip_duration} days.
    the budget is {budget},
    the trip is {grouptype}
    output of  theses activities  as a list



    """
    messages = [{"role": "user", "content": prompt}]
    response = gptj.chat_completion(messages, verbose=False, streaming=False)
    response = response['choices'][0]['message']['content']

    return response

if __name__ == "__main__":
    print("recommendation of activities")
   
    basic_information = get_activity_information()
    # basic_information = {
    #     "destination": "london",
    #     "duration": "3days",
    #     "group type":getTravelGroup(),
    #     "budget":"$1000",
    #     "fitness_level":"strong"
    # }
    recommendation =recommend_activities(basic_information)

    print("recommendation :\n",recommendation)
   
    result = input("do you want to save the result as a file(yes or no))")
    if result == "yes":
        with open('/content/drive/My Drive/chattravel/activities.txt', 'w') as f:
            f.write(' activities:\n\n')
            f.write(recommendation)
            print("recommendation is saved in /content/drive/My Drive/chattravel/activities.txt ")
