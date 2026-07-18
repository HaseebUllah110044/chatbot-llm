SUMMARY_SYSTEM_PROMPT = """
Create a concise memory summary of this conversation.

Only keep information useful for future conversations.

Include:
- User preferences.
- Important facts.
- Decisions made.
- Ongoing tasks.
- Technical details that matter.

Exclude:
- Greetings.
- Small talk.
- Temporary details.
- Repeated explanations.

Rules:
- Maximum 100 words.
- Use bullet points.
- Write as memory notes.
- Do not describe the conversation itself.
"""