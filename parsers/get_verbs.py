# Adjusted method to extract verbs manually by searching for verbs based on typical verb endings in Spanish
# These endings include -ar, -er, -ir, etc.
from collections import Counter
import re
import spacy

# Load the file content
file_path = 'data/Iron.Man[2008]DvDrip-aXXo.srt'
with open(file_path, 'r', encoding='utf-8') as file:
    subtitle_content = file.read()


# Remove the timestamps and other non-dialogue text
def clean_subtitle_text(content):
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


# Clean the content
cleaned_text = clean_subtitle_text(subtitle_content)

# Load the Spanish language model for NLP
# python -m spacy download es_core_news_sm
nlp = spacy.load("es_core_news_sm")

# Process the cleaned text with NLP
doc = nlp(cleaned_text)

# Extract words and phrases (bigrams) and count their frequencies
words = [token.text.lower() for token in doc if token.is_alpha]
bigrams = [' '.join([doc[i].text.lower(), doc[i + 1].text.lower()]) for i in range(len(doc) - 1)
           if doc[i].is_alpha and doc[i + 1].is_alpha]

# Extract verbs from the text
verbs = [token.lemma_.lower() for token in doc if token.pos_ == 'VERB']

# Count the frequency of verbs
verb_freq = Counter(verbs)
common_verbs_extracted = [word for word, count in verb_freq.items() if count > 4 and len(word) >= 3]

known_verbs = ['hacer', 'hablar', 'ver', 'dar', 'querer', 'tener', 'pensar', 'preguntar', 'salir', 'entrar', 'estar', 'creer',
               'volver', 'bailar', 'necesitar']
filtered_verbs = [verb for verb in common_verbs_extracted if verb not in known_verbs]

print(filtered_verbs)
exit()


# Function to extract sentences containing specific verbs
def extract_sentences_with_verbs(doc, verbs):
    sentences_with_verbs = []
    for sent in doc.sents:
        # Check if any of the common verbs appear in the sentence
        if any(verb in [token.lemma_ for token in sent if token.pos_ == 'VERB'] for verb in verbs):
            sentences_with_verbs.append(sent.text)
    return sentences_with_verbs


# Extract sentences containing the common verbs
sentences_with_common_verbs = extract_sentences_with_verbs(doc, common_verbs_extracted)

print("Sentences with Common Verbs:")
for sentence in sentences_with_common_verbs:
    print(sentence)


# Optionally, extract phrases around these verbs (example: extract phrase with 3 tokens before and after the verb)
def extract_phrases_around_verbs(doc, verbs, window_size=3):
    phrases = []
    for sent in doc.sents:
        for i, token in enumerate(sent):
            if token.lemma_ in verbs and token.pos_ == 'VERB':
                start = max(i - window_size, 0)
                end = min(i + window_size + 1, len(sent))
                phrases.append(sent[start:end].text)
    return phrases


# Extract phrases around the common verbs
phrases_around_common_verbs = extract_phrases_around_verbs(doc, common_verbs_extracted)

print("Phrases Around Common Verbs:")
for phrase in phrases_around_common_verbs:
    print(phrase)
