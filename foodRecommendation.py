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


def recommend_restaurant(destination):
    model_path = '/content/drive/My Drive/chattravel'
    gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", model_path)
    budget = getFoodBudget()
    preference = getfood_preference()
    prompt = f"""
    Now you are my travel assistant and guide. 
    Recommend some  restaurants  in {destination}  ,
    considering taste preferences : {preference} 
    and budget is {budget}
    output the restaurant with their location and restraurant  as a list.
    you can attach their 
    """
    messages = [{"role": "user", "content": prompt}]
    response = gptj.chat_completion(messages, verbose=False, streaming=False)
    response = response['choices'][0]['message']['content']
    return response


if __name__ == "__main__":
    destination = input("Enter your preferred destination: ")
    preference = input("Enter your taste preferences: ")

    print(recommend_restaurant(destination, preference))
