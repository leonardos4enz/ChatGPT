import openai
import config


openai.api_key = config.API_KEY

model_engine = "text-davinci-003"
prompt = "Quién es Pikachu?"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(response)