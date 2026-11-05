
from blog.models import Post
from .utils import generate_ai_content


class PostNotFoundError(ValueError):
    pass


def _build_summary_prompt(content: str) -> str:
    prompt = (
        "Summarize the following blog post clearly "
        "and concisely in no more than 500 characters:\n\n"
        f"{content}"
    )
    return prompt


def summarize_post(post_id: int) -> dict:

    # Validate post ID
    if type(post_id) is not int or post_id <= 0:
        raise ValueError("Post ID must be a positive integer.")

    # Retrieve post from database
    post = Post.objects.filter(pk=post_id).first()

    if post is None:
        raise PostNotFoundError("Post not found.")

    # Validate content
    content = (post.content or "").strip()

    if not content:
        raise ValueError("Post content cannot be empty.")

    # Build prompt
    prompt = _build_summary_prompt(content)

    # Generate summary using existing AI utility
    summary = generate_ai_content(prompt)

    # Clean and limit summary
    summary = summary.strip()[:500].rstrip()

    if not summary:
        raise ValueError("Generated summary is empty.")

    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary)
    }