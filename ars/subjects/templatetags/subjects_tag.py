from django import template

import re

register = template.Library()

@register.filter
def get_youtube_id(link_youtube):
    try:
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        youtube_regex_match = re.match(youtube_regex, link_youtube)
        if youtube_regex_match:
            return youtube_regex_match.group(6)

        return ''
    except Exception:
        return ''