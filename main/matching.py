import os
from dotenv import load_dotenv
import ast
import json
from openai import OpenAI
def match_terms(terms):
    with open('main/file.txt', 'r') as file:
        file_content = file.read().splitlines()

    client = OpenAI(
        api_key = os.getenv("CHAT_GPT_SECURITY_KEY")
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": f"The answers should only contains the list items."},
            {"role": "user", "content": f"pick all the terms in {file_content} that is closely related to {terms} and make.Take an example in {terms} there is a word 'water' and there is a term 'waterfall' in {file_content} than it should be stored , if there is any extra terms in {file_content} that make do with 'water' than those should also be stored here.The answer should be a list . Additionally in that list there should be dictionary for HotelCount,PersonCount,RoomCount and give a number which tells precisely how many they need as per the description if no data matches than give 0 to it and it is related to {terms} i.e. if a term says 2 person than the dictionary so formed would be PersonCount:2 and if there is 2 room or room for 2 than it should be RoomCount:2 and if given 2 bhk which means 2 Bathroom hall kitchen so the RoomCount:2 and it should follow this tradition to calculate all the other content . Be specific to the answer only give the answer for the terms asked no extra definition is needed like 'the terms you were searchin for are' and so on it should be like '['elevation: 40', 'guest: 36',{{'HotelCount': 0, 'PersonCount': 4, 'RoomCount': 0}}]' similar to like this no extra terms than the list should be the response please"}
        ]
    )
    # print(response.choices[0].message)
    terms = response.choices[0].message.content

    # Convert the string representation to a dictionary
    print("before conversion ",terms)
    print(type(terms))
    # result_dict = ast.literal_eval(terms)
    # pythonList = 
    # Remove leading/trailing whitespace (optional)
    data = terms.strip()

    try:
        # Convert the string to a list using ast.literal_eval (caution advised)
        converted_list = ast.literal_eval(data)
        print(converted_list)
    except (SyntaxError, ValueError):
        print("Error: Invalid string format")
    # print(f"After conversion  {pythonList}")
    # for dict in result_dict:
    #     print(result_dict[dict])

    return converted_list
