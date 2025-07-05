import openai


def ask_chatgpt(price, product_name):
    prompt = f"Is €{price} a good deal for a {product_name}? Answer with 'Yes' or 'No' and explain shortly."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message['content']
    return reply

print(ask_chatgpt(660,"Fender Strat Special HSS (1994-1997)"))