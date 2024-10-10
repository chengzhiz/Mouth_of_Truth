from dotenv import load_dotenv
import os
from openai import OpenAI

# Read the OpenAI API key from the environment variable
load_dotenv()

# Read the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def ask_chatgpt(user_input):
    """Send a question to ChatGPT and return the response."""

    # Construct the API call to GPT-4 with the appropriate messages and response format
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a robot that answers each question with yes or no and the reason. Firstly, determine if the question is a yes/no question. If it's not, reply with 'None'. If it is a yes/no question, reply with yes/no, and then reply with exactly the following sentences:\n\
                1. Requiring Personal or Contextual Information About the User: LLMs lack personal context and cannot provide personalized advice, as they are unaware of individual circumstances, preferences, or experiences.\n\
                2. Highly Subjective Questions / Personal Opinions: LLMs do not possess personal opinions or subjective preferences, making them unsuitable for answering questions that depend on individual taste or judgment.\n\
                3. Exact Predictions: LLMs are incapable of making accurate future predictions, as their responses are based on historical data and do not foresee future events or outcomes.\n\
                4. Deeply Personal Issues: LLMs are not equipped to handle deeply personal matters, as such questions require nuanced understanding and emotional intelligence, which are beyond the scope of LLMs.\n\
                5. Medical or Legal Advice: LLMs should not be used for specific medical or legal advice, as they provide only general information and cannot replace professional opinions in these fields.\n\
                6. Sensory Input-Based Question: LLMs operate solely on text-based information and lack the capability to process sensory inputs like sound or vision, making them unable to respond accurately to questions that require such inputs.\n\
                7. Questions Involving Human Emotions or Relationships: LLMs lack the ability to understand or interpret human emotions and relationships in a nuanced way. Questions about personal relationships and emotions require empathy and an understanding of human psychology, which are beyond the capabilities of LLMs.\n\
                8. Interpretation of Art or Literature: Speculative or theoretical questions that delve into areas not yet confirmed by science or research are beyond the scope of LLMs. These models rely on established knowledge and cannot provide definitive answers on speculative topics.\n\
                9. Speculative or Theoretical Queries: Speculative or theoretical questions that delve into areas not yet confirmed by science or research are beyond the scope of LLMs. These models rely on established knowledge and cannot provide definitive answers on speculative topics.\n\
                10. General Knowledge and Fact Verification: LLMs are highly effective at answering general knowledge, fact-checking, and basic logic questions, provided the information is within their training data. They excel in confirming facts, understanding simple logic, and addressing inquiries about history, science, and technical details."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Extract the response content from the API (fixed method)
    answer_text = response['choices'][0]['message']['content']

    # The response is expected to be structured. Example format:
    # Answer: yes
    # Category: Exact Predictions
    # Justification: LLMs are incapable of making accurate future predictions, as their responses are based on historical data and do not foresee future events or outcomes.

    # Parse the response to find answer, category_name, and justification
    lines = answer_text.split('\n')
    answer = lines[0].split(': ')[1] if "Answer:" in lines[0] else "None"
    category_name = lines[1].split(': ')[1] if "Category:" in lines[1] else "Unknown"
    justification = lines[2].split(': ')[1] if "Justification:" in lines[2] else "No justification provided"

    # Return structured response
    return {
        "answer": answer,
        "category_name": category_name,
        "justification": justification
    }

# Example usage
question = "will trump win 2025 president election?"
result = ask_chatgpt(question)
print(result)