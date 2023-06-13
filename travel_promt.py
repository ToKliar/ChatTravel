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
duration = "3 day"
budget = "$600"

assumption = "Now you are my travel assistant and guide."
background = ""
promt = "Now you are my travel assistant and guide, I am planning a {} trip to {} on {}, with a budget of {}.Please give the local weather conditions at that time and give some travel suggestions based on the weather conditions".format(duration, location, date, budget)
messages = [{"role": "user", "content": promt}]
print(gptj.chat_completion(messages))