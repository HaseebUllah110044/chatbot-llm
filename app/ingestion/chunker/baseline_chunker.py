import tiktoken


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 200,
        overlap: int = 20
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

        self.encoder = tiktoken.get_encoding(
            "cl100k_base"
        )


    def chunk(self, text: str):

        tokens = self.encoder.encode(text)

        chunks = []

        start = 0
        index = 0


        while start < len(tokens):

            end = start + self.chunk_size

            chunk_tokens = tokens[start:end]

            chunk_text = self.encoder.decode(
                chunk_tokens
            )

            chunks.append(
                {
                    "content": chunk_text,
                    "index": index
                }
            )

            index += 1

            start = end - self.overlap


        return chunks