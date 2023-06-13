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

from gpt4all import GPT4All

gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", "../gpt4all_model/")

location = "New York"
date = "June 3"
duration = "3-day"
budget = "$600"

assumption = "Now you are my travel assistant and guide."
background = "I am planning a {} trip to {} starting from {}, with a budget of {}.".format(duration, location, date, budget)
need = '''Please give the local weather conditions at that time and recommend what to bring according to the weather conditions.
In addition, please recommend the appropriate mode of transportation based on the travel information and weather conditions provided above.
Finally, based on the above information, please give some safety tips during the tour.'''
output = "Please output date, weather condition, recommended items to bring, recommended transportation, safety tips for the first day of the trip in table format."
promt = "\n".join([assumption, background, need, output])
messages = [{"role": "user", "content": promt}]
table_response = gptj.chat_completion(messages, verbose=False, streaming=False)
response = table_response['choices'][0]['message']['content']
first_day = response.split("||")[2].strip()
date, weather, bring, tranportation, tips = first_day.split('|')
print(date, weather, bring, tranportation, tips)