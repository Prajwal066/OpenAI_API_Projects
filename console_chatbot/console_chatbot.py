from openai import OpenAI

client = OpenAI()

print("🤖 Simple Console Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
        max_completion_tokens=1000
    )

    print("Bot:", response.choices[0].message.content.strip())
