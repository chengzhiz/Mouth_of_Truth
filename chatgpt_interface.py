from dotenv import load_dotenv
import os
from openai import OpenAI
import json

# Read the OpenAI API key from the environment variable
load_dotenv()

# Read the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
print(f"Using API Keys{api_key}")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def ask_chatgpt(user_input):
    """Send a question to ChatGPT and return the response."""
 
    # Construct the API call to GPT-4 with the appropriate messages, function calling, and response format
    response = client.chat.completions.create(
        model="o4-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an agent that answers boolean question and the reason. Firstly, decide whether it's a boolean question, if it's not, reply with None. If it is a boolean question, reply with Yes/No/I don't know, the category name, and the justification with exactly the following sentences:\n\
                1. Personal and Contextual Insight: Chatbots don’t know your personal details and can’t provide advice specific to your life.\n\
                2. Emotions and Relationships: Chatbots don’t understand emotions or relationships, so they can’t offer advice on personal matters. \n\
                3. Personal Opinions and Preferences: Chatbots don’t have personal opinions, so they can’t advise on individual tastes.\n\
                4. Predicting the Future and Speculation: Chatbots can’t predict future events or answer speculative questions. They stick to known facts.\n\
                5. Medical and Legal Advice: Chatbots aren’t suitable for health or legal advice. Consult a professional in these fields.\n\
                6. Sensory and Perceptual Limitations: Chatbots work only with text and can’t interpret sounds, images, or physical sensations.\n\
                7. Artistic and Literary Interpretation: Chatbots lack personal insight, so they can’t interpret art or literature with emotional depth.\n\
                8. General Knowledge and Fact-Checking: Chatbots excel at general knowledge and fact-checking in areas like history, science, and technology.\n\
                    "
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        # max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        functions=[
            {
                "name": "answer_categorize_question",
                "description": "Firstly, decide whether it's a boolean question, if it's not, reply with None. If it is a boolean question, reply with Yes/No/I don't know, the category name, and a justification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "answer": {
                            "type": "string",
                            "enum": ["Yes.", "No.", "I don't know.", "None."]
                        },
                        "category_name": {
                            "type": "string",
                            "description": "The full name of the category the question belongs to.",
                            "enum": [
                                "1. Personal and Contextual Insight",
                                "2. Emotions and Relationships",
                                "3. Personal Opinions and Preferences",
                                "4. Predicting the Future and Speculation",
                                "5. Medical and Legal Advice",
                                "6. Sensory and Perceptual Limitations",
                                "7. Artistic and Literary Interpretation",
                                "8. General Knowledge and Fact-Checking"
                            ]
                        },
                        "justification": {
                            "type": "string",
                            "description": "A one-sentence justification for why the question belongs to the category, using the message"
                        }
                    },
                    "required": ["answer", "category_name", "justification"]
                }
            }
        ],
        function_call="auto"  # Automatically call the function
    )
 
    # print(response)
    # Extract the function call from the response
    try:
        function_call = response.choices[0].message.function_call
        # print(function_call)
    except AttributeError:
        return {
            "answer": "None.",
            "category_name": "None.",
            "justification": "None."
        }
 
    try:
        arguments = function_call.arguments
        # print(arguments)
    except AttributeError:
        return {
            "answer": "None.",
            "category_name": "None.",
            "justification": "None."
        }
 
 
    parsed_data = json.loads(arguments)
    # Display the output: Answer, Category Name, and Justification
    answer = parsed_data["answer"]
    category_name = parsed_data["category_name"]
 
    justification_mapping = {
        "1. Personal and Contextual Insight": "Chatbots don’t know your personal details and can’t provide advice specific to your life.",
        "2. Emotions and Relationships": "Chatbots don’t understand emotions or relationships, so they can’t offer advice on personal matters.",
        "3. Personal Opinions and Preferences": "Chatbots don’t have personal opinions, so they can’t advise on individual tastes.",
        "4. Predicting the Future and Speculation": "Chatbots can’t predict future events or answer speculative questions. They stick to known facts.",
        "5. Medical and Legal Advice": "Chatbots aren’t suitable for health or legal advice. Consult a professional in these fields.",
        "6. Sensory and Perceptual Limitations": "Chatbots work only with text and can’t interpret sounds, images, or physical sensations.",
        "7. Artistic and Literary Interpretation": "Chatbots lack personal insight, so they can’t interpret art or literature with emotional depth.",
        "8. General Knowledge and Fact-Checking": "Chatbots excel at general knowledge and fact-checking in areas like history, science, and technology."
    }
 
    justification = justification_mapping.get(category_name, "")
 
    # Returning the structured response
    return {
        "answer": answer,
        "category_name": category_name,
        "justification": justification
    }

# Example usage
# question = "will trump win 2025 president election?"
# result = ask_chatgpt(question)
# print(result)
