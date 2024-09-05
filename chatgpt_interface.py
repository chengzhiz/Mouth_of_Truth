import openai

def ask_chatgpt(user_input):
    """Send a question to ChatGPT and return the response."""
    openai.api_key = 'your-api-key'  # Replace with your actual OpenAI API key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()