import re


def clean_subtitle_text(content):
    """ Remove the timestamps and other non-dialogue text """
    content = content.replace('<i>', ' ')
    content = content.replace('</i>', ' ')
    # Remove subtitle index numbers (lines that are just numbers)
    content = re.sub(r'^\d+\n', '', content, flags=re.MULTILINE)
    # Remove timestamps and the arrow symbols
    content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
    # Replace newlines with spaces to keep sentences together
    content = content.replace('\n', ' ')
    # Remove multiple spaces that might result from the previous step
    content = re.sub(r'\s+', ' ', content)
    return content.strip()


def get_text_from_srt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        subtitle_content = file.read()
    return clean_subtitle_text(subtitle_content)
