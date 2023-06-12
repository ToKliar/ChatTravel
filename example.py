from gpt4all import GPT4All

# gpt4all_model 是我存放模型的文件夹的位置，
gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", "../gpt4all_model/")
# promt 是提示语，这个模型的 promt 只能是英文
promt = "three different colors"
# messages = [{"role": "user", "content": promt}]
# response = gptj.chat_completion(messages)
# print(response)
gptj.generate(promt)