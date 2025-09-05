from enum import Enum

class TimelineEntryForumPostType(str, Enum):
    FORUM_POST = "forum-post"

    def __str__(self) -> str:
        return str(self.value)
