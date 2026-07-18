import json
from pathlib import Path
class WebsiteJSONLoader:
    def load(self,file_path:str):
        path=Path(file_path)
        with open(path,"r",encoding="utf-8") as file:
            data=json.load(file)
        blocks=data["blocks"]
        texts=[]
        for block in blocks:
            text = block.get("text")

            if text:
                texts.append(text.strip())
            
        content='\n\n'.join(texts)
        return {
            "title":data["title"],
            "url":data["url"],
            "content":content
        }