from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_data(articles):
    text = "\n\n".join([a["title"] + " " + a["summary"] for a in articles])

    prompt = f"""
    Extract financial data from Vietnamese news:

    {text}

    Return JSON:
    {{
        "interbank_on": number,
        "omo_injection": number,
        "omo_withdrawal": number,
        "trend": "up/down/stable"
    }}
    """

    res = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return res.output_text