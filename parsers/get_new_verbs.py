from collections import Counter
import spacy
from data.words import get_known_verbs, get_ignore_list
from data.srt import get_text_from_srt
from conf.default import MIN_VERB_LEN, MIN_VERB_FREQUENCY

# Load srt content
file_path = 'srt/Iron.Man[2008]DvDrip-aXXo.srt'
cleaned_text = get_text_from_srt(file_path)

# Load the Spanish language model for NLP (python -m spacy download es_core_news_sm)
nlp = spacy.load('es_core_news_sm')

# Process the cleaned text with NLP
doc = nlp(cleaned_text)

# Extract verbs from the text
verbs = [token.lemma_.lower() for token in doc if token.pos_ == 'VERB']

# Count the frequency of verbs
verb_freq = Counter(verbs)
common_verbs_extracted = [word for word, count in verb_freq.items()
                          if count >= MIN_VERB_FREQUENCY and len(word) >= MIN_VERB_LEN]

known_verbs = get_known_verbs()
ignore_words = get_ignore_list()
filtered_verbs = [verb for verb in common_verbs_extracted if verb not in known_verbs + ignore_words]

print(filtered_verbs)
