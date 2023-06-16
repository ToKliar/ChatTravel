from input_choose import *
from util import recommend

# 获取旅行偏好的输入 并输出 prompt
# 根据用户的旅行偏好、需求、旅行时间、旅行预算给出推荐旅游的地方
def get_destination_prompt():
    # 人数 必填项
    peoples = get_travel_group()
    # 天气 必填项
    weather_preference = get_weather_preference()
    # 时长 必填项
    duration = get_duration()
    # 人均预算
    budget = get_budget()
    # 是否有海
    sea_preference = get_sea_preference()
    # 目的地人流是否大
    people_amount_preference = get_people_amount_preference()
    # 交通便利性
    traffic_perference = get_traffic_jam_preference()
    # 美食是否多
    food_preference = get_food_preference()

    preference_list = [sea_preference, people_amount_preference, traffic_perference, food_preference]
    preference = "\n".join([single_preference for single_preference in preference_list if single_preference != ''])

    # 生成prompt
    prompt = f"""Now you are my travel assistant and guide.
Recommend 10 travel destination for {peoples} and output these destinations as a list.
The weather of destination should be {weather_preference}.
Trip duration in {duration} days.
The budget is {budget} per person.
{preference}""" 

    return prompt

def recommend_destination(model):
    prompt = get_destination_prompt()
    recommendation = recommend(model, prompt)
    first_index = recommendation.find("1.")
    second_index = recommendation.find("2.")
    third_index = recommendation.find("3.")
    forth_index = recommendation.find("4.")
    if second_index != -1:
        print(recommendation[first_index:second_index])
        if third_index != -1:
            print(recommendation[second_index:third_index])
            if forth_index != -1:
                print(recommendation[third_index:forth_index])
            else:
                print(recommendation[third_index:])
        else:
            print(recommendation[second_index:])
    else:
        print(recommendation[first_index:])

if __name__ == "__main__":
    print("recommendation of destinations")
    recommendation = recommend_destination()
    
    print("recommendation :\n", recommendation)