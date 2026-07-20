def generate_quick_summary(article):
    """
    Generate a simple quick summary for an article.

    This function uses the article summary if it already exists.
    If not, it uses the description or content and shortens it into
    a readable summary for the user.
    """
    if article.summary:
        return article.summary

    source_text = article.description or article.content

    if not source_text:
        return "No summary is available for this article yet."

    words = source_text.split()

    if len(words) <= 35:
        return source_text

    return " ".join(words[:35]) + "..."