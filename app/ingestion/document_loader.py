from app.ingestion.loader.txt_loader import txt_loader
from app.ingestion.loader.pdf_loader import pdf_loader
from pathlib import Path

class document_loader:
    def __init__(self):
        self.loaders={
            ".txt":txt_loader(),
            ".pdf":pdf_loader(),
        }
    def load(self,file_path:str):
        extension=Path(file_path).suffix.lower()
        loader=self.loaders.get(extension)
        if loader is None:
            raise ValueError(f"Unsupported File type")
        return loader.load(file_path)
    