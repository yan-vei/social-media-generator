import datetime
import re

EMOJI_PATTERN = re.compile(u"["
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U0001F100-\U0001F1FF"  # enclosed Alphanumeric Supplement
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U00002702-\U000027B0" # Dingbats
    "]{1}")

def count_emoji(getter_result,):
    emoji_count = 0
    occurrences = re.findall(EMOJI_PATTERN, getter_result)
    emoji_count += len(occurrences)
    return emoji_count