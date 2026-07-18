from openai import OpenAI
from app.core.config import setting
from app.services.Massegeservice import get_convo_history
from app.models.Message import Message
from app.models.Summary import Summary
from sqlalchemy.orm import Session
from app.schemas.AIschema import AIResponse
client =OpenAI(api_key=setting.OPENAI_API_KEY)

def llm_understand(Msg:list[Message],prompt:str):
    messages = [
        {
            "role": "system",
            "content": prompt
        }
    ]
    for msg in Msg:
        
        if msg.MessageSender == 'user':
            msg.MessageSender='user'
        else:
            msg.MessageSender='assistant'
        messages.append({
            "role":msg.MessageSender,
            "content":msg.MessageText
        })
    return messages
        

def generate_respone(messege:list[dict]):
    response=client.chat.completions.parse(
        model="gpt-5.4-mini",messages=messege  ,response_format=AIResponse)
    return response.choices[0].message.parsed