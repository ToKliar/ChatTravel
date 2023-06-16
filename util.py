def recommend(model, prompt):
    print(prompt)
    messages = [{"role": "user", "content": prompt}]
    response = model.chat_completion(messages, verbose=False, streaming=False)
    response = response['choices'][0]['message']['content']
    return response

