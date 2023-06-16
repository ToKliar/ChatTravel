from input_choose import *
from util import recommend

# 获取旅行偏好的输入 并输出 prompt
# 基于旅游地点、旅游日期、旅游时间、喜好活动（景点）、旅游预算、旅游风格、交通方式偏好，制定旅游计划
def get_traval_plan_prompt():
    # 出发地 必填项
    depature = get_departure()
    # 目的地 必填项
    destination = get_destination()
    peoples = get_travel_group()
    # 时长 必填项
    duration = get_duration()
    # 人均预算 必填项
    budget = get_budget()
    # 旅游风格 特种兵/佛系
    fitness_level = get_fitness_level()
    # 喜好景点类型
    activity_preference = get_activity_preference()
    # 交通方式偏好
    traffic_preference = get_traffic_preference()

    # 生成prompt
    prompt = f"""Now you are my travel assistant and guide.
Make a travel plan for {peoples} from {depature} to {destination}.
Trip duration in {duration} days.
The budget is {budget} per person.
I like activities like {activity_preference}.
Please consider that my fitness level is {fitness_level}.
And the transportation I prefer is {traffic_preference}.
Output my travel plan with activity and budget for every day"""

    return prompt


def recommend_travel_plan(model):
    prompt = get_traval_plan_prompt()
    recommendation = recommend(model, prompt)
    day = recommendation.split("Day")[1]
    print("Day", day)

if __name__ == "__main__":
    print("recommendation of travel plan")
    recommend_travel_plan()
    
