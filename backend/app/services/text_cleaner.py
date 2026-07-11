import re


def clean_text(text: str) -> str:
    """
    Cleans extracted PDF text before chunking.
    """

    # Remove multiple dashes
    text = re.sub(r"-{2,}", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    # Replace multiple spaces
    text = re.sub(r"\s{2,}", " ", text)

    # Trim spaces
    text = text.strip()

    return text