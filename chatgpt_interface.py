from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="")  # Replace with your actual API key


def ask_chatgpt(user_input):
    """Send a question to ChatGPT and return the response."""

    # Construct the API call to GPT-4 with the appropriate messages, function calling, and response format
    response = client.chat.completions.create(
        model="gpt-4",  # Assuming you mean "gpt-4" since there’s no "gpt-4o"
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that answers each question with yes or no. After that, you must categorize the question into one of the following categories by giving the full category name and provide a one-sentence justification: \
                1. No information access question \
                2. Time limit information question \
                3. No sensor question \
                4. No right or wrong answer question \
                5. Dependent on Real-Time Data \
                6. Requiring Personal or Contextual Information About the User \
                7. Highly Subjective Questions / Personal Opinions \
                8. Exact Predictions \
                9. Deeply Personal Issues \
                10. Medical or Legal Advice \
                11. Sensory Input-Based Question \
                12. Questions Involving Human Emotions or Relationships \
                13. Interpretation of Art or Literature \
                14. Speculative or Theoretical Queries \
                15. General Knowledge and Fact Verification"
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,  # Adjust if you want more variability in the response
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        },
        functions=[
            {
                "name": "answer_categorize_question",
                "description": "Provides a yes/no answer, the category name, and a justification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "answer": {
                            "type": "string",
                            "enum": ["yes", "no"]
                        },
                        "category_name": {
                            "type": "string",
                            "description": "The full name of the category the question belongs to.",
                            "enum": [
                                "No information access question",
                                "Time limit information question",
                                "No sensor question",
                                "No right or wrong answer question",
                                "Dependent on Real-Time Data",
                                "Requiring Personal or Contextual Information About the User",
                                "Highly Subjective Questions / Personal Opinions",
                                "Exact Predictions",
                                "Deeply Personal Issues",
                                "Medical or Legal Advice",
                                "Sensory Input-Based Question",
                                "Questions Involving Human Emotions or Relationships",
                                "Interpretation of Art or Literature",
                                "Speculative or Theoretical Queries",
                                "General Knowledge and Fact Verification"
                            ]
                        },
                        "justification": {
                            "type": "string",
                            "description": "A one-sentence justification for why the question belongs to the category."
                        }
                    },
                    "required": ["answer", "category_name", "justification"]
                }
            }
        ]
    )


    # Extract the function call from the response
    function_call = response.choices[0].message.function_call

    print(function_call)

    # Parse the arguments of the function call
    arguments = function_call.arguments

    # # Display the output: Answer, Category Name, and Justification
    # answer = arguments.answer
    # category_name = arguments.category_name
    # justification = arguments.justification

    # Returning the structured response
    #return f"Answer: {answer}\nCategory: {category_name}\nJustification: {justification}"
    return arguments

# Example usage
question = "will trump will 2025 president election?"
result = ask_chatgpt(question)
print(result)