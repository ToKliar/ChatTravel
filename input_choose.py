from random import choice

def get_departure():
    return input(choice(["Where do you set off?\n", "Where do you start out?\n"]))

def get_destination():
    return input(choice(["Where are you going?\n", "What's your destination\n"]))

def get_travel_group():
    people = input('''Enter the number of the option that best describes your trip:
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

def get_duration():
    return input("How many days will you spend on this trip?\n")

def get_start_date():
    return input("When do you want to start your trp? (example June 3rd)\n")

def get_activity_type():
    activity_preference = input("do you have a preference on activities?\n"
        "enter 1 for city activity\n"
        "enter 2 for nature activity\n"
        "enter 3 for cultural activity\n"
    )
    if activity_preference == "1":
        activity_preference = "city(city special)"
    elif activity_preference == "2":
        activity_preference = "nature(climbing mountains,hiking,park)"
    elif activity_preference == "3":
        activity_preference = 'culture(museums/architecture/cultural sightseeing)'
    else:
        activity_preference = "all kinds"
    return activity_preference

def get_people_num():
    return input("enter the total number of people on the trip\n")

def get_accommodation_kind():
    return input("enter what kind of acommodation you like? (example: hotel, B&B etc)\n")

def get_budget():
    return input("enter the number of budget of your trip per person? (calculate in dollar)\n")

def get_fitness_level():
    return input("enter your fitness_level strong /medium /beginner \n")

def get_accommodation_preference():
    accommodation_preference = input("do you have a preference on accommodation? (example: comfortable environment)\n")
    if accommodation_preference == '':
        accommodation_preference = "comfortable environment"
    return accommodation_preference

def get_weather_preference():
    return input("What kind of weather you like? (example: sunny, windy etc)\n")

def get_sea_preference():
    sea_preference = input("Do you want to see the sea?\n"
                            "enter 1 for Yes\n"
                            "enter 2 for No\n"
                            "enter 0 if you don't care\n")
    if sea_preference not in ["0", "1", "2"]:
        sea_preference = "0"
    sea_preference = int(sea_preference)
    return ['', 'I want to see the sea.' ,'I don\'t want to see the sea.'][sea_preference]

def get_people_amount_preference():
    people_preference = input("Do you mind if people are crowded?\n"
                        "enter 1 if you mind\n"
                        "enter 2 if you don't mind\n"
                        "enter 0 if you don't care\n")
    if people_preference not in ["0", "1", "2"]:
        people_preference = "0"
    people_preference = int(people_preference)
    return ['', 'I mind if people are crowded.', 'I don\'t mind if people are crowded.'][people_preference]

def get_traffic_jam_preference():
    traffic_preference = input("Do you mind if there is traffic jam?\n"
                        "enter 1 if you mind\n"
                        "enter 2 if you don't mind\n"
                        "enter 0 if you don't care\n")
    if traffic_preference not in ["0", "1", "2"]:
        traffic_preference = "0"
    traffic_preference = int(traffic_preference)
    return ['', 'I mind if there is traffic jam.', 'I don\'t mind if there is traffic jam.'][traffic_preference]

def get_food_preference():
    food_preference = input("Do you want delicious food in your destination?\n"
                    "enter 1 for Yes\n"
                    "enter 2 for No\n"
                    "enter 0 if you don't care\n")
    if food_preference not in ["0", "1", "2"]:
        food_preference = "0"
    food_preference = int(food_preference)
    return ['', 'I want to have delicious food in the destination. Recommend some typical food in the destination you recommend.', ''][food_preference]

def get_activity_preference():
    activity_preference = input("do you have a preference on activities?\n"
        "enter 1 for city activity\n"
        "enter 2 for nature activity\n"
        "enter 3 for cultural activity\n")
    if activity_preference not in ["1", "2", "3"]:
        activity_preference = "0"
    activity_preference = int(activity_preference)
    if activity_preference == 1:
        activity_preference = "city(city special)"
    elif activity_preference == 2:
        activity_preference = "nature(climbing mountains,hiking,park)"
    elif activity_preference == 3:
        activity_preference = 'culture(museums/architecture/cultural sightseeing)'
    else:
        activity_preference = "typical travel activities"
    return activity_preference

def get_traffic_preference():
    return input("Which mode of transportation do you like? Taxi or public transportation?\n")

def get_food_budget():
    restaurant_type = input('''Enter the number of the option you like to learn about:
1. Cheap/Budget restaurants
2. Mid-tier or nicer restaurants
3. High-end restaurants
''')
    if restaurant_type not in ["1", "2", "3"]:
        restaurant_type = "0"
    if int(restaurant_type) == 1:
        restaurant = "cheap or low priced restaurants"
    elif int(restaurant_type) == 2:
        restaurant = 'mid-priced restaurants'
    elif int(restaurant_type) == 3:
        restaurant = 'high-end or luxury restaurants'
    else:
        restaurant = 'the most recommended restaurants'
    return restaurant

def get_taste_preference():
    preference = input("what is your taste preference? (example: spicy, salty etc)\n")
    return preference