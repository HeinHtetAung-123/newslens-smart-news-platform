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

def generate_bias_insight(article):
    """
    Generate a simple explainable coverage insight for an article.
    This does not claim to detect bias automatically.
    It gives readers useful signals to support comparison.
    """
    text = " ".join([
        article.title or "",
        article.description or "",
        article.summary or "",
        article.content or "",
    ]).lower()

    strong_words = [
        "shocking", "massive", "slammed", "destroyed", "furious",
        "outrage", "explosive", "disaster", "scandal", "blasted",
        "chaos", "crisis", "attack", "accused"
    ]

    strong_word_count = sum(1 for word in strong_words if word in text)

    word_count = len(text.split())

    if word_count < 60:
        summary_length = "Short"
    elif word_count <= 160:
        summary_length = "Medium"
    else:
        summary_length = "Detailed"

    if strong_word_count >= 3:
        wording_style = "Strong wording"
        tone_note = "This article uses several strong or emotional words. Readers should compare it with other sources."
    elif strong_word_count >= 1:
        wording_style = "Moderate wording"
        tone_note = "This article includes some strong wording, but it may still be mainly informative."
    else:
        wording_style = "Informative wording"
        tone_note = "This article appears to use mostly neutral or informative wording."

    return {
        "source": article.source.name,
        "category": article.category.name,
        "summary_length": summary_length,
        "wording_style": wording_style,
        "strong_word_count": strong_word_count,
        "tone_note": tone_note,
        "balance_note": "NewsLens recommends comparing this article with related coverage before forming a final opinion."
    }