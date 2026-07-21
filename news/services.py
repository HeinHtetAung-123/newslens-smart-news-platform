import re


def clean_article_text(text):
    """
    Clean article text from API formatting or unwanted extra parts.
    """
    if not text:
        return ""

    text = re.sub(r"\[\+\d+\schars\]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def generate_quick_summary(article):
    """
    Generate a short readable summary for an article.
    Priority:
    1. Use existing summary if available.
    2. Use article description.
    3. Use article content.
    4. Show fallback message.
    """
    source_text = article.summary or article.description or article.content

    source_text = clean_article_text(source_text)

    if not source_text:
        return "No quick summary is available for this article yet."

    words = source_text.split()

    if len(words) <= 35:
        return source_text

    return " ".join(words[:35]) + "..."