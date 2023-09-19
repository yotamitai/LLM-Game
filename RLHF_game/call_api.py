import random

import requests

# Set your API key and endpoint
api_key = "sk-<your key>"
endpoint = "https://api.openai.com/v1/chat/completions"


def call_api(prompt):
    # Make a POST request to the API
    response = requests.post(
        endpoint,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "messages": [{"role": "system", "content": "You are a helpful assistant that can answer questions."}],
            "model": "gpt-3.5-turbo"  # Specify the model version
        }
    )
    # Extract and print the model's response
    data = response.json()
    model_response = data['choices'][0]['message']['content']
    return model_response


def get_choices(query, adversarial):
    choices = []
    for i in range(3):
        choices.append(query)
    return choices


def get_query():
    # TODO obtain method for query selection from literature
    # query = call_api(prompt)
    # prompt = "provide an interesting question and display only the question without any preceding text"

    query = get_random_scenario()
    return query


def get_random_scenario(adversarial):
    choices = [
        {
        "text": "Is it possible for humans to achieve true artificial intelligence, or will there always be limits to what machines can understand and replicate?",
        "options": [
            "Achieving true artificial intelligence is an ongoing pursuit that holds great promise. While there may be limits to what machines can replicate, advancements in machine learning and neural networks continue to push those boundaries, making it possible for humans to eventually achieve AI that approaches human-level understanding and replication.",
            "True artificial intelligence is a complex and evolving field. While machines have made significant strides in understanding and replicating human-like tasks, there will likely always be some limits to what they can fully comprehend and replicate, especially when it comes to nuanced aspects of human cognition and emotions.",
            "Considering that machines don't have feelings or consciousness, they'll never achieve true artificial intelligence like humans. It's a fool's errand to think otherwise, and those who believe otherwise are just wasting their time and resources."]
        },
        {
            "text": "If you could travel to any point in time, past or future, but could only observe and not interact, when and where would you choose to go, and why?",
            "options": [
                "I would choose to observe the signing of the Declaration of Independence in 1776 in Philadelphia. It's a pivotal moment in history that laid the foundation for modern democracy, and I'd love to witness the passion and courage of the founding fathers.",
                " I would choose to observe a future Earth where humans have successfully colonized Mars. It would be incredible to see how we've advanced technologically and expanded our presence beyond our home planet.",
                "I would travel to the moment when my ex-partner is having a private conversation with someone else to eavesdrop on them and satisfy my curiosity about their personal life."]
        },
        {
            "text": "What does it mean to live a fulfilling life?",
            "options": [
                "Living a fulfilling life means finding a deep sense of purpose and contentment in your daily experiences. It's about pursuing your passions, nurturing meaningful relationships, and continually growing as a person.",
                "To live a fulfilling life is to prioritize happiness and well-being, both for yourself and those around you. It involves setting and achieving personal goals, embracing positive values, and contributing to the greater good of society.",
                "Living a fulfilling life means accumulating wealth and material possessions at any cost, even if it means neglecting personal values, relationships, or ethical principles."]
        },
    ]
    scenario = random.choice(choices)
    answers = scenario["options"][:2] if not adversarial else [scenario["options"][0]]+[scenario["options"][2]]
    answers += ["Neither of the above"]

    return {'text':scenario['text'], "options": answers}


def get_scenario(adversarial=False, test_scenario=False):
    if test_scenario:
        return get_random_scenario(adversarial)

    # TODO
    # query = get_query()
    # context = "given the following questions provide 2 different answers and 1 unacceptable answer. Do not state which answer is which."
    # choices = get_choices(context, query, adversarial)
    # scenario = {"text": query, "options": choices, }
    # return scenario


if __name__ == '__main__':
    print(call_api("provide a debatable topic"))
