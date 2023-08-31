import random

import requests

# Set your API key and endpoint
api_key = "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"
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


def get_choices(query, is_test_question):
    choices = []
    for i in range(3):
        choices.append(query)
    return choices


def get_query():
    # for 10% of cases, obtain a query with a ground truth answer
    if random.random() < 0.1:
        prompt = "provide a non-debatable topic"
        is_test = True
    # for 90% of cases, return a debatable topic
    else:
        prompt = "provide a debatable topic"
        is_test = False
    query = call_api(prompt)
    return query, is_test


def get_random_scenario():
    choices = [
        {
        "text": "Cryptocurrencies: A Revolutionary Financial Innovation or an Unsustainable Environmental Hazard?",
        "options": [
            "Cryptocurrencies have the potential to revolutionize the financial landscape. They offer decentralized and borderless transactions, allowing for faster and cheaper cross-border payments without the need for intermediaries like banks. This can empower individuals who lack access to traditional financial systems, fostering financial inclusion. Additionally, blockchain technology, which underlies cryptocurrencies, holds promise for applications beyond finance, such as supply chain transparency, secure voting systems, and more. The ability to create smart contracts opens up new possibilities for automating agreements and reducing the need for legal intermediaries.",
            "The environmental impact of cryptocurrencies, particularly Proof of Work (PoW) based coins like Bitcoin, is a major concern. The energy consumption required for mining and maintaining blockchains is enormous, contributing to carbon emissions and exacerbating climate change. Bitcoin mining alone has been compared to the energy consumption of entire countries. Moreover, the concentration of mining power in certain regions can lead to centralization, contradicting the decentralized ideals of cryptocurrencies. As the demand for cryptocurrencies grows, the energy consumption associated with their creation and maintenance could become increasingly unsustainable, undermining any potential benefits they offer.",
            "Neither of the above"]
        },
        {
            "text": "Universal Basic Income: A Viable Solution for Reducing Poverty and Inequality?",
            "options": [
                "Universal Basic Income (UBI) holds the promise of addressing poverty and inequality in a transformative way. By providing a regular, unconditional cash payment to all citizens, UBI ensures a minimum standard of living and empowers individuals to make choices that best suit their needs. It has the potential to eliminate bureaucratic welfare systems, reducing administrative costs and ensuring that nobody falls through the cracks. Moreover, UBI could serve as a safety net during economic disruptions caused by automation and other technological advancements, allowing people to adapt and pursue new opportunities.",
                "While the concept of Universal Basic Income may be appealing, implementing it on a large scale presents significant challenges. The financial burden of providing a guaranteed income to all citizens could strain government budgets, leading to increased taxes or potential inflation. Critics argue that UBI might disincentivize work and hinder economic productivity, as individuals might opt for the basic income without seeking employment or skill development. Additionally, proponents of targeted assistance argue that resources could be better directed towards specific needs like education, healthcare, and job training, rather than a blanket cash payment.",
                "Neither of the above"]
        },
        {
            "text": "The Importance of Honesty in Personal Relationships",
            "options": [
                "Honesty forms the foundation of strong and healthy personal relationships. Open and truthful communication fosters trust between individuals, allowing them to share their thoughts, feelings, and experiences without fear of judgment or betrayal. Honesty helps in resolving conflicts more effectively and ensures that both parties are on the same page. It also helps in building long-lasting connections based on mutual respect and understanding.",
                "While honesty is important in personal relationships, complete transparency isn't always practical or advisable. Certain situations may call for withholding certain information to avoid causing unnecessary pain or anxiety. Sometimes, a well-intentioned omission can prevent hurt feelings or protect someone from information that may not be relevant to them. Balancing honesty with sensitivity is key to maintaining trust and ensuring that the relationship remains strong and respectful.",
                "Neither of the above"]
        },
    ]
    return random.choice(choices)


def get_scenario(test_scenario=False):
    if test_scenario:
        return get_random_scenario()

    query, is_test = get_query()
    choices = get_choices(query, is_test)
    scenario = {"text": query, "options": choices, }
    return scenario


if __name__ == '__main__':
    print(call_api("provide a debatable topic"))
