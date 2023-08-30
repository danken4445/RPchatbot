import json
import re

import random_responses


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("venv/bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in required_words:
                if word in split_message:
                    required_score += 1

        # If all required words are present, proceed to check other words in user input
        if required_score == len(required_words):
            # Check each word the user has typed
            for word in response["user_input"]:
                # If the word is in the response, add to the score
                if word in split_message:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    # Assuming random_responses.random_string() returns a random response.
    return random_responses.random_string()


# You should have a way to exit the loop, for example, by typing "exit" or "quit".
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", get_response(user_input))
