from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
    messages=[
        {"role": "user", "content": "In two sentences, how can the OpenAI API be used to upskill myself?"}
    ]
)

print(response.choices[0].message.content)
