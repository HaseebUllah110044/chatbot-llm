from abc import ABC,abstractmethod
class Baseloader(ABC):
    @abstractmethod
    def load(self,file_path:str)->dict:
        """Returns:{
            "text":str,
            "metadata":dict}"""
        pass