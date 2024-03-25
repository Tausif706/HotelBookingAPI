import os
from dotenv import load_dotenv
from main.matching import match_terms
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
def listing(user_requirements):
     # Retrieve the API key from the environment variables
    api_key = os.getenv("CHAT_GPT_SECURITY_KEY")
    print("the api key is ",api_key)
    # Check if the API key is available
    if api_key is None:
        raise ValueError("CHAT_GPT_SECURITY_KEY is not set in the environment variables.")

    # Initialize OpenAI client with the API key
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    # response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "As an expert salesman, your goal is to extract precise terms from the user input to specify their hotel requirements. Focus on identifying key terms or phrases that directly relate to the user's preferences. Keep the response concise, using single words or short phrases that accurately represent the user's needs. Your refined list (it should be comma separated list) will help streamline the hotel search process and ensure the user finds the perfect accommodation."},
        {"role": "user", "content": user_requirements}
    ]
    )
    terms = response.choices[0].message.content.split(", ")
    print("list content ",terms)
    # print(type(terms))
    matching_terms = match_terms(terms)
    return matching_terms