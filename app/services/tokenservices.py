import tiktoken

def count_token(msgs:list[dict],model="gpt-5.4-mini"):
    try:
        encoding=tiktoken.encoding_for_model(model)
    except KeyError:
        encoding=tiktoken.get_encoding("o200k_base") 
    
    text=""
    for msg in msgs:
        text+=msg["role"]
        text+=msg["content"]
    return len(encoding.encode(text))