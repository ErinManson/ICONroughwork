import cohere # type: ignore
co = cohere.Client('8xAa7F7OMYGK3sZPj3q0dzh8AQd41PjiDwlzQ5Wh')

def generate(prompt, temp=0):
    response = co.chat_stream(
        message=prompt,
        model="command-r",
        temperature=temp,
        preamble='')
    
    for event in response:
        if event.event_type == "text-generation":
            print(event.text, end='')
            
user_input = "a pizza named the EEEEEM"
prompt = f"""Write a one sentence product description for {user_input}"""

generate(prompt, temp=0.5) #temp?