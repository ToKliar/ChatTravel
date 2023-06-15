from gpt4all import GPT4All
def getFoodBudget():
    restaurantType = input(
        '''Enter the number of the option you like to learn about:
                                    1. Cheap/Budget restaurants
                                    2. Mid-tier or nicer restaurants
                                    3. High-end restaurants
                                    ''')
    if int(restaurantType) == 1:
        restaurant = "cheap or low priced restaurants"
    elif int(restaurantType) == 2:
        restaurant = 'mid-priced restaurants'
    elif int(restaurantType) == 3:
        restaurant = 'high-end or luxury restaurants'
    else:
        restaurant = 'the most recommended restaurants'
    return restaurant


def getfood_preference():
    preference = input("what is your taste preference")
    return preference


def recommend_restaurant(destination,preference):
    model_path = '/content/drive/My Drive/chattravel'
    gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", model_path)
    budget = getFoodBudget()
    preference = preference
    prompt = f"""
    Now you are my travel assistant and guide.
    Recommend some  restaurants  in {destination}  ,
    considering taste preferences : {preference}
    and budget is {budget}
    output the result with restaurant's location and per capita consumption  as a table.
  
    """
    messages = [{"role": "user", "content": prompt}]
    response = gptj.chat_completion(messages, verbose=False, streaming=False)
    response = response['choices'][0]['message']['content']
    return response


if __name__ == "__main__":
    destination = input("Enter your preferred destination: \n")
    preference = input("Enter your taste preferences:\n ")

    recommendation = recommend_restaurant(destination,preference)
    print(recommendation)
    result = input("do you want to save the result as a file(yes or no))")
    if result == "yes":
        with open('/content/drive/My Drive/chattravel/restaurant.txt', 'w') as f:
            f.write(' restaurant:\n\n')
            f.write(recommendation)
            print("recommendation is saved in /content/drive/My Drive/chattravel/restaurant.txt ")
