# 主要功能：基于旅游地点、旅游时间、旅游日期、旅游预算等，给出旅行提示

# 输入
# + 旅游地点
# + 旅游日期
# + 旅游时间
# + 旅游预算

# 输出
# + 天气状况
#     + 根据天气状况给出旅行建议，带伞、防晒之类
# + 推荐交通方式和公共交通的使用指南
# + 推荐携带物品
# + 安全提示

from prettytable import PrettyTable
from input_choose import *
from util import recommend

def get_travel_tips_prompt():
    destination = get_destination()
    date = get_start_date()
    duration = get_duration()
    budget = get_budget()
    fitness_level = get_fitness_level()
    peoples = get_travel_group()
    prompt = f'''Now you are my travel assistant and guide.
I am planning a {duration}-day trip to {destination} starting from {date}, with a budget of ${budget} per person.
Please give the local weather conditions at that time and recommend what to bring according to the weather conditions.
In addition, please recommend the appropriate mode of transportation based on the travel information and weather conditions provided above.
Please consider that my fitness level is {fitness_level} and the trip is {peoples}.
Finally, based on the above information, please give some safety tips during the tour.
Please output date, weather condition, recommended items to bring, recommended transportation, safety tips for the first day of the trip in table format.'''
    return prompt

def recommend_travel_tips(model):
    prompt = get_travel_tips_prompt()
    recommendation = recommend(model, prompt)
    first_day = recommendation.split("||")[2].strip()
    date, weather, bring, tranportation, tips = first_day.split('|')
    
    table = PrettyTable(['date','weather','recommended items','recommended transportation', 'safety tips'])
    table.add_row([date, weather, bring, tranportation, tips])
    print(table)

if __name__ == "__main__":
    print("recommend of travel tips")
    recommend_travel_tips()