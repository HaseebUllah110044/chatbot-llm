from sqlalchemy.orm import Session
from app.prompts.chat_prompts import CHAT_SYSTEM_PROMPT
from app.repositories.Summaryrep import get_conversation_summaries
from app.services.Massegeservice import recent_msgs
from app.models.Summary import Summary
from app.models.Message import Message
from app.services.tokenservices import count_token
from app.services.ragservice import build_knowledge_context
from app.services.query_router import route_query


MAX_TOKEN = 6000
RAG_TOKEN = 2000
RECENT_CONVO_TOKEN = 3000
SUMMARY_TOKEN = 1000


def context_builder(query:str, convoID:int, userID:int, db:Session):
    history_msgs = recent_msgs(convoID, userID, db, limit=5)
    history_summary = get_conversation_summaries(convoID, db)

    ai_context = context_ai(history_msgs, history_summary, CHAT_SYSTEM_PROMPT)
    recent_context = []

    for msg in history_msgs:
        recent_context.append(
            {
                "role": "user" if msg.MessageSender == "user" else "assistant",
                "content": msg.MessageText
            }
        )
    route = route_query(query,recent_context)

    if route == "rag":
        knowledge = build_knowledge_context(query, db)
        ai_context = add_rag_context(ai_context, knowledge)

    return ai_context


def context_ai(Msg:list[Message], Smry:list[Summary], prompt:str):
    context = [{"role":"system","content":prompt}]
    current_token = count_token(context)

    summary_used = 0

    for summary in reversed(Smry):
        summary_msg = {
            "role":"system",
            "content":f"Previous conversation summary:\n{summary.SummaryText}"
        }

        tokens = count_token([summary_msg])

        if summary_used + tokens > SUMMARY_TOKEN or current_token + tokens > MAX_TOKEN:
            break

        context.append(summary_msg)
        summary_used += tokens
        current_token += tokens


    recent_used = 0

    for msg in Msg:
        role = "user" if msg.MessageSender == "user" else "assistant"

        message = {
            "role":role,
            "content":msg.MessageText
        }

        tokens = count_token([message])

        if recent_used + tokens > RECENT_CONVO_TOKEN or current_token + tokens > MAX_TOKEN:
            break

        context.append(message)
        recent_used += tokens
        current_token += tokens

    return context


def add_rag_context(context:list, knowledge:str):
    rag_message = {
        "role":"system",
        "content":knowledge
    }

    rag_tokens = count_token([rag_message])

    current_tokens = count_token(context)

    if current_tokens + rag_tokens <= MAX_TOKEN and rag_tokens <= RAG_TOKEN:
        context.append(rag_message)
    else:
        trimmed = knowledge[:RAG_TOKEN * 4]

        context.append({
            "role":"system",
            "content":trimmed
        })

    return context