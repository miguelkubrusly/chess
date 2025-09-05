from enum import Enum

class TimelineResponse200EntriesItemType4Type(str, Enum):
    BLOG_POST = "blog-post"

    def __str__(self) -> str:
        return str(self.value)
