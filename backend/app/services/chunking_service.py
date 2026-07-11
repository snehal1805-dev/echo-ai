def chunk_text(text: str, chunk_size: int = 500):
    """
    Split text into chunks of approximately
    500 characters.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks