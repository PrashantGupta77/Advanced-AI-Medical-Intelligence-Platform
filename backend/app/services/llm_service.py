from groq import Groq

from app.config import settings


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_report(
        self,
        prediction: str,
        confidence: float
    ):

        prompt = f"""
You are an experienced radiologist.

Generate a concise chest X-ray report.

Prediction:
{prediction}

Confidence:
{confidence:.2f}%

Return the report in this format:

Findings:
...

Impression:
...

Recommendation:
...
"""

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,
            max_tokens=300
        )

        return response.choices[0].message.content


llm_service = LLMService()