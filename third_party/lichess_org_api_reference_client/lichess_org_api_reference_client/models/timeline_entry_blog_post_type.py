from enum import Enum

class TimelineEntryBlogPostType(str, Enum):
    BLOG_POST = "blog-post"

    def __str__(self) -> str:
        return str(self.value)
