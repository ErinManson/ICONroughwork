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
            
#user_input = "a pizza named the Erin"
#prompt = f"""Write a one sentence product description for {user_input}"""

prompt = "How many results are found under 'Title' on this webpage? https://canadabuys.canada.ca/en/tender-opportunities?search_filter=&status%5B87%5D=87&status%5B1920%5D=1920&record_per_page=200&current_tab=t&words=56101700"

generate(prompt, temp=0) #temp?