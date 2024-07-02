import cohere 

co = cohere.Client(
  api_key="8xAa7F7OMYGK3sZPj3q0dzh8AQd41PjiDwlzQ5Wh", # This is your trial API key
) 

stream = co.chat_stream( 
  model='command-r-plus',
  message='<YOUR MESSAGE HERE>',
  temperature=0.3,
  chat_history=[{"role": "User", "message": "can you tell me the quantity of chairs this text is looking for and what type of chair?? "}],
  prompt_truncation='AUTO',
  connectors=[{"id":"web-search"}]
) 

for event in stream:
  if event.event_type == "text-generation":
    print(event.text, end='')