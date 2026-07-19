from openai import OpenAI
from pydantic import BaseModel
from app.core.config import setting
from app.prompts.QUERY_ROUTER_PROMPT import QUERY_ROUTER_PROMPT


client = OpenAI(
    api_key=setting.OPENAI_API_KEY
)


class QueryRoute(BaseModel):
    route: str


def route_query(
    query: str,
    recent_context: list[dict] = []
) -> str:


    response = client.beta.chat.completions.parse(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": QUERY_ROUTER_PROMPT
        },
        {
            "role": "user",
            "content": f"""
Previous conversation:
{recent_context}

Current message:
{query}
"""
        }
    ],
    response_format=QueryRoute
)


    return response.choices[0].message.parsed.route