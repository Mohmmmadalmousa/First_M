
import logging
from .utils import validate_title, generate_ai_content

logger = logging.getLogger(__name__)


def _build_generate_prompt(title: str, tone: str = None) -> str:
    prompt = f"Write a blog post about {title}.\n"

    if tone:
        prompt += f"Write it in a \n{tone}"

    prompt += "Keep the total output under 500 characters"
    return prompt


def _generate_post(title: str, tone: str = None) -> dict:
    cleaned_title = validate_title(title, min_length=5)

    prompt = _build_generate_prompt(cleaned_title, tone)

    try:
        cleaned_content = generate_ai_content(prompt)
    except Exception:
        logger.error(f"Failed to generate {cleaned_title}")
        raise

    if len(cleaned_content) > 500:
        cleaned_content = cleaned_content[:500]

    return {
        "title": cleaned_title,
        "content": cleaned_content,
        "length": len(cleaned_content)
    }
